import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';

import 'package:deu_mppt/shared/menu_top.dart';

import 'package:deu_mppt/provide/data.dart';
import 'package:provider/provider.dart';

final snackBarKeyA = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyB = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyC = GlobalKey<ScaffoldMessengerState>();
final Map<DeviceIdentifier, ValueNotifier<bool>> isConnectingOrDisconnecting =
    {};

class FindDevicesScreen2 extends StatefulWidget {
  const FindDevicesScreen2({Key? key}) : super(key: key);

  @override
  State<FindDevicesScreen2> createState() => _FindDevicesScreen2State();
}

class _FindDevicesScreen2State extends State<FindDevicesScreen2> {
  @override
  Widget build(BuildContext context) {
    final deviceData = Provider.of<DeviceId>(context);

    return ScaffoldMessenger(
      key: snackBarKeyB,
      child: Scaffold(
        appBar: const MenuTop(),
        body: RefreshIndicator(
          onRefresh: () {
            setState(() {});

            //스캔중이 아니라면 스캔시작
            if (FlutterBluePlus.isScanningNow == false) {
              FlutterBluePlus.startScan(
                  timeout: const Duration(seconds: 15),
                  androidUsesFineLocation: false);
            }

            return Future.delayed(const Duration(milliseconds: 500));
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
                                //연결 상태에 따라서 연결 표시 전환
                                stream: d.connectionState,
                                initialData:
                                    BluetoothConnectionState.disconnected,
                                builder: (c, snapshot) {
                                  //이미 연결되어 있다면
                                  if (snapshot.data ==
                                      BluetoothConnectionState.connected) {
                                    deviceData.setDevice(d);
                                    return ElevatedButton(
                                      child: const Text('Already'),
                                      onPressed: () => Navigator.of(context)
                                          .push(MaterialPageRoute(
                                              builder: (context) =>
                                                  DeviceScreen(device: d),
                                              settings: const RouteSettings(
                                                  name: '/deviceScreen'))),
                                    );
                                  }

                                  //디바이스에 연결되어 있지않다면
                                  if (snapshot.data ==
                                      BluetoothConnectionState.disconnected) {
                                    return ElevatedButton(
                                        child: const Text('CONNECT'),
                                        onPressed: () {
                                          deviceData.setDevice(d);
                                          Navigator.of(context).push(
                                              MaterialPageRoute(
                                                  builder: (context) {
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
                                      deviceData.setDevice(r.device);
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

  late Timer timer;

  late BluetoothCharacteristic myc;

  Future<bool> connect() async {
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
                      //print("RECIVE : $value");
                      //int vl = value.length;
                      //print("LENGTH : $vl");
                      bluetoothData.addData(value);
                    },
                  );
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
            const Duration(seconds: 1),
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
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white.withOpacity(0.3),
      body: AlertDialog(
        backgroundColor:
            Colors.white.withOpacity(0.9), // Adjust the opacity here
        shape:
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
        title: const Text('연결이 완료 되었습니다!'),
        key: snackBarKeyC,
        content: const Text('연결이 완료 되었습니다!'),
        actions: <Widget>[
          TextButton(
            child: const Text("OK"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      ),
    );
  }
}

class ScanResultTile extends StatelessWidget {
  const ScanResultTile({Key? key, required this.result, this.onTap})
      : super(key: key);

  final ScanResult result;
  final VoidCallback? onTap;

  Widget _buildTitle(BuildContext context) {
    if (result.device.localName.isNotEmpty) {
      return Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text(
            result.device.localName,
            overflow: TextOverflow.ellipsis,
          ),
          Text(
            result.device.remoteId.toString(),
            style: Theme.of(context).textTheme.bodySmall,
          )
        ],
      );
    } else {
      return Text(result.device.remoteId.toString());
    }
  }

  Widget _buildAdvRow(BuildContext context, String title, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 4.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text(title, style: Theme.of(context).textTheme.bodySmall),
          const SizedBox(
            width: 12.0,
          ),
          Expanded(
            child: Text(
              value,
              style: Theme.of(context)
                  .textTheme
                  .bodySmall
                  ?.apply(color: Colors.black),
              softWrap: true,
            ),
          ),
        ],
      ),
    );
  }

  String getNiceHexArray(List<int> bytes) {
    return '[${bytes.map((i) => i.toRadixString(16).padLeft(2, '0')).join(', ')}]'
        .toUpperCase();
  }

  String getNiceManufacturerData(Map<int, List<int>> data) {
    if (data.isEmpty) {
      return 'N/A';
    }
    List<String> res = [];
    data.forEach((id, bytes) {
      res.add(
          '${id.toRadixString(16).toUpperCase()}: ${getNiceHexArray(bytes)}');
    });
    return res.join(', ');
  }

  String getNiceServiceData(Map<String, List<int>> data) {
    if (data.isEmpty) {
      return 'N/A';
    }
    List<String> res = [];
    data.forEach((id, bytes) {
      res.add('${id.toUpperCase()}: ${getNiceHexArray(bytes)}');
    });
    return res.join(', ');
  }

  @override
  Widget build(BuildContext context) {
    return ExpansionTile(
      title: _buildTitle(context),
      leading: Text(result.rssi.toString()),
      trailing: /* IconButton(
        icon: Icon(Icons.arrow_forward,
            color: result.advertisementData.connectable
                ? Colors.black
                : Colors.grey),
        onPressed: () {
          if (result.advertisementData.connectable) {
            onTap;
            print("!");
          }
        },
      ), */
          ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.black,
          foregroundColor: Colors.white,
        ),
        onPressed: (result.advertisementData.connectable) ? onTap : null,
        child: const Icon(Icons.arrow_forward), //SCAN시 나오는 연결표시
      ),
      children: <Widget>[
        _buildAdvRow(
            context, 'Complete Local Name', result.advertisementData.localName),
        _buildAdvRow(context, 'Tx Power Level',
            '${result.advertisementData.txPowerLevel ?? 'N/A'}'),
        _buildAdvRow(context, 'Manufacturer Data',
            getNiceManufacturerData(result.advertisementData.manufacturerData)),
        _buildAdvRow(
            context,
            'Service UUIDs',
            (result.advertisementData.serviceUuids.isNotEmpty)
                ? result.advertisementData.serviceUuids.join(', ').toUpperCase()
                : 'N/A'),
        _buildAdvRow(context, 'Service Data',
            getNiceServiceData(result.advertisementData.serviceData)),
      ],
    );
  }
}

SnackBar snackBarGood(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.blue);
}

SnackBar snackBarFail(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.red);
}

String prettyException(String prefix, dynamic e) {
  if (e is FlutterBluePlusException) {
    return "$prefix ${e.description}";
  } else if (e is PlatformException) {
    return "$prefix ${e.message}";
  }
  return prefix + e.toString();
}
