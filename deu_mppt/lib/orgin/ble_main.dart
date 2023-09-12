import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';
import 'package:deu_mppt/shared/menu_top.dart';
import 'ble_widgets.dart';

import 'package:deu_mppt/provide/data.dart';
import 'package:provider/provider.dart';

final snackBarKeyA = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyB = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyC = GlobalKey<ScaffoldMessengerState>();
final Map<DeviceIdentifier, ValueNotifier<bool>> isConnectingOrDisconnecting =
    {};

class FindDevicesScreen extends StatefulWidget {
  const FindDevicesScreen({Key? key}) : super(key: key);

  @override
  State<FindDevicesScreen> createState() => _FindDevicesScreenState();
}

class _FindDevicesScreenState extends State<FindDevicesScreen> {
  @override
  Widget build(BuildContext context) {
    return ScaffoldMessenger(
      key: snackBarKeyB,
      child: Scaffold(
        appBar: const MenuTop(),
        body: RefreshIndicator(
          onRefresh: () {
            setState(() {}); // force refresh of connectedSystemDevices
            if (FlutterBluePlus.isScanningNow == false) {
              FlutterBluePlus.startScan(
                  timeout: const Duration(seconds: 15),
                  androidUsesFineLocation: false);
            }
            return Future.delayed(
                const Duration(milliseconds: 500)); // show refresh icon breifly
          },
          child: SingleChildScrollView(
            child: Column(
              children: <Widget>[
                StreamBuilder<List<BluetoothDevice>>(
                  stream:
                      Stream.fromFuture(FlutterBluePlus.connectedSystemDevices),
                  initialData: const [],
                  builder: (c, snapshot) => Column(
                    children: (snapshot.data ?? [])
                        .map((d) => ListTile(
                              title: Text(d.localName),
                              subtitle: Text(d.remoteId.toString()),
                              trailing: StreamBuilder<BluetoothConnectionState>(
                                stream: d.connectionState,
                                initialData:
                                    BluetoothConnectionState.disconnected,
                                builder: (c, snapshot) {
                                  if (snapshot.data ==
                                      BluetoothConnectionState.connected) {
                                    return ElevatedButton(
                                      child: const Text('OPEN'),
                                      onPressed: () => Navigator.of(context)
                                          .push(MaterialPageRoute(
                                              builder: (context) =>
                                                  DeviceScreen(device: d),
                                              settings: const RouteSettings(
                                                  name: '/deviceScreen'))),
                                    );
                                  }
                                  //앞전에 연결한 디바이스가 끊겨있을때 오픈하는 버튼
                                  if (snapshot.data ==
                                      BluetoothConnectionState.disconnected) {
                                    return ElevatedButton(
                                        child: const Text('CONNECT!!!!!'),
                                        onPressed: () {
                                          print(d);
                                          Navigator.of(context).push(
                                              MaterialPageRoute(
                                                  builder: (context) {
                                                    //d.discoverServices();

                                                    isConnectingOrDisconnecting[
                                                            d.remoteId] ??=
                                                        ValueNotifier(true);
                                                    isConnectingOrDisconnecting[
                                                            d.remoteId]!
                                                        .value = true;
                                                    d
                                                        .connect(
                                                            timeout:
                                                                const Duration(
                                                                    seconds:
                                                                        35))
                                                        .catchError((e) {
                                                      final snackBar =
                                                          snackBarFail(
                                                              prettyException(
                                                                  "Connect Error:",
                                                                  e));
                                                      snackBarKeyC.currentState
                                                          ?.removeCurrentSnackBar();
                                                      snackBarKeyC.currentState
                                                          ?.showSnackBar(
                                                              snackBar);
                                                    }).then((v) {
                                                      isConnectingOrDisconnecting[
                                                              d.remoteId] ??=
                                                          ValueNotifier(false);
                                                      isConnectingOrDisconnecting[
                                                              d.remoteId]!
                                                          .value = false;
                                                    });
                                                    return DeviceScreen(
                                                        device: d);
                                                  },
                                                  settings: const RouteSettings(
                                                      name: '/deviceScreen')));
                                        });
                                  }
                                  return Text(snapshot.data
                                      .toString()
                                      .toUpperCase()
                                      .split('.')[1]);
                                },
                              ),
                            ))
                        .toList(),
                  ),
                ),
                StreamBuilder<List<ScanResult>>(
                  stream: FlutterBluePlus.scanResults,
                  initialData: const [],
                  builder: (c, snapshot) => Column(
                    children: (snapshot.data ?? [])
                        .map(
                          (r) => ScanResultTile(
                            result: r,
                            onTap: () => Navigator.of(context).push(
                                MaterialPageRoute(
                                    builder: (context) {
                                      isConnectingOrDisconnecting[r.device
                                          .remoteId] ??= ValueNotifier(true);
                                      isConnectingOrDisconnecting[
                                              r.device.remoteId]!
                                          .value = true;
                                      r.device
                                          .connect(
                                              timeout:
                                                  const Duration(seconds: 35))
                                          .catchError((e) {
                                        final snackBar = snackBarFail(
                                            prettyException(
                                                "Connect Error:", e));
                                        snackBarKeyC.currentState
                                            ?.removeCurrentSnackBar();
                                        snackBarKeyC.currentState
                                            ?.showSnackBar(snackBar);
                                      }).then((v) {
                                        isConnectingOrDisconnecting[r.device
                                            .remoteId] ??= ValueNotifier(false);
                                        isConnectingOrDisconnecting[
                                                r.device.remoteId]!
                                            .value = false;
                                      });
                                      return DeviceScreen(device: r.device);
                                    },
                                    settings: const RouteSettings(
                                        name: '/deviceScreen'))),
                          ),
                        )
                        .toList(),
                  ),
                ),
              ],
            ),
          ),
        ),
        floatingActionButton: StreamBuilder<bool>(
          stream: FlutterBluePlus.isScanning,
          initialData: false,
          builder: (c, snapshot) {
            if (snapshot.data ?? false) {
              return FloatingActionButton(
                onPressed: () async {
                  try {
                    FlutterBluePlus.stopScan();
                  } catch (e) {
                    final snackBar =
                        snackBarFail(prettyException("Stop Scan Error:", e));
                    snackBarKeyB.currentState?.removeCurrentSnackBar();
                    snackBarKeyB.currentState?.showSnackBar(snackBar);
                  }
                },
                backgroundColor: Colors.red,
                child: const Icon(Icons.stop),
              );
            } else {
              return FloatingActionButton(
                  child: const Text("SCAN"),
                  onPressed: () async {
                    try {
                      if (FlutterBluePlus.isScanningNow == false) {
                        FlutterBluePlus.startScan(
                            timeout: const Duration(seconds: 15),
                            androidUsesFineLocation: false);
                      }
                    } catch (e) {
                      final snackBar =
                          snackBarFail(prettyException("Start Scan Error:", e));
                      snackBarKeyB.currentState?.removeCurrentSnackBar();
                      snackBarKeyB.currentState?.showSnackBar(snackBar);
                    }
                    setState(() {}); // force refresh of connectedSystemDevices
                  });
            }
          },
        ),
      ),
    );
  }
}

class DeviceScreen extends StatefulWidget {
  final BluetoothDevice device;

  const DeviceScreen({Key? key, required this.device}) : super(key: key);

  @override
  State<DeviceScreen> createState() => _DeviceScreenState();
}

class _DeviceScreenState extends State<DeviceScreen> {
  String stateText = 'Connecting';

  List<BluetoothService> bluetoothService = [];

  Map<String, List<int>> notifyDatas = {};

  bool isAutoEnabled = false;

  late Timer timer;

  late BluetoothCharacteristic myc;

  List<int> _getRandomBytes() {
    final math = Random();
    return [
      math.nextInt(255),
      math.nextInt(255),
      math.nextInt(255),
      math.nextInt(255)
    ];
  }

  List<Widget> _buildServiceTiles(
      BuildContext context, List<BluetoothService> services) {
    return services
        .map(
          (s) => ServiceTile(
            service: s,
            characteristicTiles: s.characteristics
                .map(
                  (c) => CharacteristicTile(
                    characteristic: c,
                    onReadPressed: () async {
                      try {
                        await c.read();
                        final snackBar = snackBarGood("Read: Success");
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      } catch (e) {
                        final snackBar =
                            snackBarFail(prettyException("Read Error:", e));
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      }
                    },
                    onWritePressed: () async {
                      try {
                        await c.write(
                            [0x23, 0x52, 0x45, 0x51, 0x30, 0x31, 0x40],
                            withoutResponse: c.properties.writeWithoutResponse);
                        final snackBar = snackBarGood("Write: Success");
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                        if (c.properties.read) {
                          //await c.read();
                        }
                        print("WritePressed!!");
                      } catch (e) {
                        final snackBar =
                            snackBarFail(prettyException("Write Error:", e));
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      }
                    },
                    onNotificationPressed: () async {
                      try {
                        String op =
                            c.isNotifying == false ? "Subscribe" : "Unubscribe";
                        await c.setNotifyValue(c.isNotifying == false);
                        final snackBar = snackBarGood("$op : Success");
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                        if (c.properties.read) {
                          await c.read();
                        }
                      } catch (e) {
                        final snackBar = snackBarFail(
                            prettyException("Subscribe Error:", e));
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      }
                    },
                    descriptorTiles: c.descriptors
                        .map(
                          (d) => DescriptorTile(
                            descriptor: d,
                            onReadPressed: () async {
                              try {
                                await d.read();
                                final snackBar = snackBarGood("Read: Success");
                                snackBarKeyC.currentState
                                    ?.removeCurrentSnackBar();
                                snackBarKeyC.currentState
                                    ?.showSnackBar(snackBar);
                              } catch (e) {
                                final snackBar = snackBarFail(
                                    prettyException("Read Error:", e));
                                snackBarKeyC.currentState
                                    ?.removeCurrentSnackBar();
                                snackBarKeyC.currentState
                                    ?.showSnackBar(snackBar);
                              }
                            },
                            onWritePressed: () async {
                              try {
                                await d.write(_getRandomBytes());
                                final snackBar = snackBarGood("Write: Success");
                                snackBarKeyC.currentState
                                    ?.removeCurrentSnackBar();
                                snackBarKeyC.currentState
                                    ?.showSnackBar(snackBar);
                              } catch (e) {
                                final snackBar = snackBarFail(
                                    prettyException("Write Error:", e));
                                snackBarKeyC.currentState
                                    ?.removeCurrentSnackBar();
                                snackBarKeyC.currentState
                                    ?.showSnackBar(snackBar);
                              }
                            },
                          ),
                        )
                        .toList(),
                  ),
                )
                .toList(),
          ),
        )
        .toList();
  }

  Future<bool> connect() async {
    //List<int> buff = [];
    List<int> buffer = [];

    Future<bool>? returnValue;
    setState(() {
      stateText = 'Connecting';
    });
    await widget.device
        .connect(autoConnect: false)
        .timeout(const Duration(milliseconds: 15000), onTimeout: () {
      //타임아웃 발생
      //returnValue를 false로 설정
      returnValue = Future.value(false);
      debugPrint('timeout failed');

      //연결 상태 disconnected로 변경
      //setBleConnectionState(BluetoothDeviceState.disconnected);
    }).then((data) async {
      bluetoothService.clear();
      if (returnValue == null) {
        //returnValue가 null이면 timeout이 발생한 것이 아니므로 연결 성공
        debugPrint('connection successful');
        print('start discover service');
        List<BluetoothService> bleServices =
            await widget.device.discoverServices();
        setState(() {
          bluetoothService = bleServices;
        });
        // 각 속성을 디버그에 출력
        for (BluetoothService service in bleServices) {
          print('============================================');
          print('Service UUID: ${service.uuid}');
          for (BluetoothCharacteristic c in service.characteristics) {
            if (c.properties.write) {
              myc = c;
              print("linked is :$c");
            }

            print('\tcharacteristic UUID: ${c.uuid.toString()}');
            print('\t\twrite: ${c.properties.write}');
            print('\t\tread: ${c.properties.read}');
            print('\t\tnotify: ${c.properties.notify}');
            print('\t\tisNotifying: ${c.isNotifying}');
            print(
                '\t\twriteWithoutResponse: ${c.properties.writeWithoutResponse}');
            print('\t\tindicate: ${c.properties.indicate}');

            // notify나 indicate가 true면 디바이스에서 데이터를 보낼 수 있는 캐릭터리스틱이니 활성화 한다.
            // 단, descriptors가 비었다면 notify를 할 수 없으므로 패스!
            if (c.properties.notify && c.descriptors.isNotEmpty) {
              // 진짜 0x2902 가 있는지 단순 체크용!
              for (BluetoothDescriptor d in c.descriptors) {
                print('BluetoothDescriptor uuid ${d.uuid}');
                if (d.uuid == BluetoothDescriptor.cccd) {
                  print('d.lastValue: ${d.lastValue}');
                }
              }

              // notify가 설정 안되었다면...
              if (!c.isNotifying) {
                final bluetoothData =
                    Provider.of<BluetoothData>(context, listen: false);
                try {
                  print("THIS!!!!");
                  print('\t\twrite: ${c.properties.write}');
                  await c.setNotifyValue(true);
                  await Future.delayed(const Duration(milliseconds: 200));
                  await widget.device.requestMtu(200);
                  c.value.listen(
                    (value) {
                      print("RECIVE : $value");
                      int vl = value.length;
                      print("LENGTH : $vl");
                      bluetoothData.addData(value);
                    },
                  );
                  //await Future.delayed(const Duration(milliseconds: 500));

                  //toggleAuto();
                  /*  // 받을 데이터 변수 Map 형식으로 키 생성
                  notifyDatas[c.uuid.toString()] = List.empty();
                  c.value.listen((value) {
                    // 데이터 읽기 처리!
                    print('${c.uuid}: $value');
                    setState(() {
                      // 받은 데이터 저장 화면 표시용
                      notifyDatas[c.uuid.toString()] = value;
                    });
                  }); */

                  // 설정 후 일정시간 지연
                  await Future.delayed(const Duration(milliseconds: 500));
                } catch (e) {
                  print('error ${c.uuid} $e');
                }
              }
            }
          }
        }
        try {
          Timer.periodic(
            const Duration(seconds: 5),
            (timer) async {
              await myc.write([0x23, 0x52, 0x45, 0x51, 0x30, 0x31, 0x40],
                  withoutResponse: myc.properties.writeWithoutResponse);
            },
          );
        } catch (e) {}
        returnValue = Future.value(true);
      }
    });

    return returnValue ?? Future.value(false);
  }

  @override
  void initState() {
    super.initState();
    connect();
    /* timer = Timer.periodic(const Duration(milliseconds: 1000), (timer) {
      if (isAutoEnabled) {
        //widget.onWritePressed?.call();
      }
    }); */
  }

  /*  @override
  void dispose() {
    timer.cancel();
    super.dispose();
  }

  void toggleAuto() {
    setState(() {
      isAutoEnabled = !isAutoEnabled;
    });
  } */

  @override
  Widget build(BuildContext context) {
    return ScaffoldMessenger(
      key: snackBarKeyC,
      child: Scaffold(
        appBar: AppBar(
          title: Text(widget.device.localName),
          actions: <Widget>[
            StreamBuilder<BluetoothConnectionState>(
              stream: widget.device.connectionState,
              initialData: BluetoothConnectionState.connecting,
              builder: (c, snapshot) {
                VoidCallback? onPressed;
                String text;
                switch (snapshot.data) {
                  case BluetoothConnectionState.connected:
                    onPressed = () async {
                      isConnectingOrDisconnecting[widget.device.remoteId] ??=
                          ValueNotifier(true);
                      isConnectingOrDisconnecting[widget.device.remoteId]!
                          .value = true;
                      try {
                        await widget.device.disconnect();
                        final snackBar = snackBarGood("Disconnect: Success");
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      } catch (e) {
                        final snackBar = snackBarFail(
                            prettyException("Disconnect Error:", e));
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      }
                      isConnectingOrDisconnecting[widget.device.remoteId] ??=
                          ValueNotifier(false);
                      isConnectingOrDisconnecting[widget.device.remoteId]!
                          .value = false;
                    };
                    text = 'DISCONNECT';
                    break;
                  case BluetoothConnectionState.disconnected:
                    onPressed = () async {
                      isConnectingOrDisconnecting[widget.device.remoteId] ??=
                          ValueNotifier(true);
                      isConnectingOrDisconnecting[widget.device.remoteId]!
                          .value = true;
                      try {
                        await widget.device
                            .connect(timeout: const Duration(seconds: 35));
                        final snackBar = snackBarGood("Connect: Success");
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      } catch (e) {
                        final snackBar =
                            snackBarFail(prettyException("Connect Error:", e));
                        snackBarKeyC.currentState?.removeCurrentSnackBar();
                        snackBarKeyC.currentState?.showSnackBar(snackBar);
                      }
                      isConnectingOrDisconnecting[widget.device.remoteId] ??=
                          ValueNotifier(false);
                      isConnectingOrDisconnecting[widget.device.remoteId]!
                          .value = false;
                    };
                    text = 'CONNECT';
                    break;
                  default:
                    onPressed = null;
                    text =
                        snapshot.data.toString().split(".").last.toUpperCase();
                    break;
                }

                return ValueListenableBuilder<bool>(
                    valueListenable:
                        isConnectingOrDisconnecting[widget.device.remoteId]!,
                    builder: (context, value, child) {
                      isConnectingOrDisconnecting[widget.device.remoteId] ??=
                          ValueNotifier(false);
                      if (isConnectingOrDisconnecting[widget.device.remoteId]!
                              .value ==
                          true) {
                        // Show spinner when connecting or disconnecting
                        return const Padding(
                          padding: EdgeInsets.all(14.0),
                          child: AspectRatio(
                            aspectRatio: 1.0,
                            child: CircularProgressIndicator(
                              backgroundColor: Colors.black12,
                              color: Colors.black26,
                            ),
                          ),
                        );
                      } else {
                        return TextButton(
                            onPressed: onPressed,
                            child: Text(
                              text,
                              style: Theme.of(context)
                                  .primaryTextTheme
                                  .labelLarge
                                  ?.copyWith(color: Colors.white),
                            ));
                      }
                    });
              },
            ),
          ],
        ),
        body: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              StreamBuilder<BluetoothConnectionState>(
                stream: widget.device.connectionState,
                initialData: BluetoothConnectionState.connecting,
                builder: (c, snapshot) => Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text('${widget.device.remoteId}'),
                    ),
                    ListTile(
                      leading: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          snapshot.data == BluetoothConnectionState.connected
                              ? const Icon(Icons.bluetooth_connected)
                              : const Icon(Icons.bluetooth_disabled),
                          snapshot.data == BluetoothConnectionState.connected
                              ? StreamBuilder<int>(
                                  stream: rssiStream(maxItems: 1),
                                  builder: (context, snapshot) {
                                    return Text(
                                        snapshot.hasData
                                            ? '${snapshot.data}dBm'
                                            : '',
                                        style: Theme.of(context)
                                            .textTheme
                                            .bodySmall);
                                  })
                              : Text('',
                                  style: Theme.of(context).textTheme.bodySmall),
                        ],
                      ),
                      title: Text(
                          'Device is ${snapshot.data.toString().split('.')[1]}.'),
                      trailing: StreamBuilder<bool>(
                        stream: widget.device.isDiscoveringServices,
                        initialData: false,
                        builder: (c, snapshot) => IndexedStack(
                          index: (snapshot.data ?? false) ? 1 : 0,
                          children: <Widget>[
                            TextButton(
                              child: const Text("Get Services"),
                              onPressed: () async {
                                try {
                                  await widget.device.discoverServices();
                                  print(widget.device);
                                  /* final snackBar = snackBarGood(
                                      "Discover Services: Success");
                                  snackBarKeyC.currentState
                                      ?.removeCurrentSnackBar();
                                  snackBarKeyC.currentState
                                      ?.showSnackBar(snackBar); */
                                } catch (e) {
                                  /* final snackBar = snackBarFail(prettyException(
                                      "Discover Services Error:", e));
                                  snackBarKeyC.currentState
                                      ?.removeCurrentSnackBar();
                                  snackBarKeyC.currentState
                                      ?.showSnackBar(snackBar); */
                                }
                              },
                            ),
                            const IconButton(
                              icon: SizedBox(
                                width: 18.0,
                                height: 18.0,
                                child: CircularProgressIndicator(
                                  valueColor:
                                      AlwaysStoppedAnimation(Colors.grey),
                                ),
                              ),
                              onPressed: null,
                            )
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              StreamBuilder<int>(
                stream: widget.device.mtu,
                initialData: 200,
                builder: (c, snapshot) => ListTile(
                  title: const Text('MTU Size'),
                  subtitle: Text('${snapshot.data} bytes'),
                  trailing: IconButton(
                      icon: const Icon(Icons.edit),
                      onPressed: () async {
                        try {
                          await widget.device.requestMtu(200);
                          final snackBar = snackBarGood("Request Mtu: Success");
                          snackBarKeyC.currentState?.removeCurrentSnackBar();
                          snackBarKeyC.currentState?.showSnackBar(snackBar);
                        } catch (e) {
                          final snackBar = snackBarFail(
                              prettyException("Change Mtu Error:", e));
                          snackBarKeyC.currentState?.removeCurrentSnackBar();
                          snackBarKeyC.currentState?.showSnackBar(snackBar);
                        }
                      }),
                ),
              ),
              StreamBuilder<List<BluetoothService>>(
                stream: widget.device.servicesStream,
                initialData: const [],
                builder: (c, snapshot) {
                  return Column(
                    children: _buildServiceTiles(context, snapshot.data ?? []),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Stream<int> rssiStream(
      {Duration frequency = const Duration(seconds: 5), int? maxItems}) async* {
    var isConnected = true;
    final subscription = widget.device.connectionState.listen((v) {
      isConnected = v == BluetoothConnectionState.connected;
    });
    int i = 0;
    while (isConnected && (maxItems == null || i < maxItems)) {
      try {
        yield await widget.device.readRssi();
      } catch (e) {
        print("Error reading RSSI: $e");
        break;
      }
      await Future.delayed(frequency);
      i++;
    }
    // Device disconnected, stopping RSSI stream
    subscription.cancel();
  }
}

String prettyException(String prefix, dynamic e) {
  if (e is FlutterBluePlusException) {
    return "$prefix ${e.description}";
  } else if (e is PlatformException) {
    return "$prefix ${e.message}";
  }
  return prefix + e.toString();
}
