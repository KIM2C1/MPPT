import 'dart:io';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'package:flutter_blue_plus/flutter_blue_plus.dart';

import 'package:deu_mppt/shared/menu_top.dart';
import 'package:provider/provider.dart';

final snackBarKeyA = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyB = GlobalKey<ScaffoldMessengerState>();
final snackBarKeyC = GlobalKey<ScaffoldMessengerState>();
final Map<DeviceIdentifier, ValueNotifier<bool>> isConnectingOrDisconnecting =
    {};

class SwitchExample extends StatefulWidget {
  const SwitchExample({super.key});

  @override
  State<SwitchExample> createState() => _SwitchExampleState();
}

class _SwitchExampleState extends State<SwitchExample> {
  bool light1 = false;

  final MaterialStateProperty<Icon?> thumbIcon =
      MaterialStateProperty.resolveWith<Icon?>(
    (Set<MaterialState> states) {
      if (states.contains(MaterialState.selected)) {
        return const Icon(Icons.check);
      }
      return const Icon(Icons.close);
    },
  );

  @override
  void initState() {
    super.initState();
    // Check the Bluetooth status when the widget initializes
    checkBluetoothStatus();
  }

  Future<void> checkBluetoothStatus() async {
    final isBluetoothAvailable = await FlutterBluePlus.isAvailable;
    setState(() {
      light1 = isBluetoothAvailable;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Switch(
          thumbIcon: thumbIcon,
          value: light1,
          onChanged: (bool value) async {
            setState(() {
              light1 = value;
            });
            if (value) {
              try {
                if (Platform.isAndroid) {
                  await FlutterBluePlus.turnOn();
                  print("clicked!");
                }
              } catch (e) {
                final snackBar =
                    snackBarFail(prettyException("Error Turning On:", e));
                snackBarKeyA.currentState?.removeCurrentSnackBar();
                snackBarKeyA.currentState?.showSnackBar(snackBar);
              }
            } else {
              //await FlutterBluePlus.turnOff();
            }
          },
        ),
      ],
    );
  }
}

class DeviceScreenMy extends StatefulWidget {
  const DeviceScreenMy({Key? key}) : super(key: key);

  @override
  State<DeviceScreenMy> createState() => _DeviceScreenMyState();
}

class _DeviceScreenMyState extends State<DeviceScreenMy> {
  @override
  Widget build(BuildContext context) {
    final testProvider = Provider.of<Testprovide>(context);

    return ScaffoldMessenger(
      //key: snackBarKeyB,
      child: Scaffold(
        appBar: const MenuTop(),
        body: RefreshIndicator(
          //backgroundColor: Colors.transparent,
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
                                  //이미 연결되어 있다면
                                  if (snapshot.data ==
                                      BluetoothConnectionState.connected) {
                                    return ElevatedButton(
                                        child: const Text('연결됨'),
                                        onPressed: () {
                                          testProvider.devicet = d;
                                          print("--------------------------");
                                          print(testProvider.devicet);
                                        } /* => Navigator.of(context)
                                          .push(MaterialPageRoute(
                                              builder: (context) =>
                                                  Test(device: d),
                                              settings: const RouteSettings(
                                                  name: '/deviceScreen'))), */
                                        );
                                  }
                                  //연결되어 있지 않다면
                                  if (snapshot.data ==
                                      BluetoothConnectionState.disconnected) {
                                    return ElevatedButton(
                                        child: const Text('연결하기'),
                                        onPressed: () {
                                          testProvider.devicet = d;
                                          print("--------------------------");
                                          print(testProvider.devicet);
                                          isConnectingOrDisconnecting[
                                                  d.remoteId] ??=
                                              ValueNotifier(true);
                                          isConnectingOrDisconnecting[
                                                  d.remoteId]!
                                              .value = true;
                                          d
                                              .connect(
                                                  timeout: const Duration(
                                                      seconds: 35))
                                              .catchError((e) {
                                            final snackBar = snackBarFail(
                                                prettyException(
                                                    "Connect Error:", e));
                                            snackBarKeyC.currentState
                                                ?.removeCurrentSnackBar();
                                            snackBarKeyC.currentState
                                                ?.showSnackBar(snackBar);
                                          }).then((v) {
                                            isConnectingOrDisconnecting[
                                                    d.remoteId] ??=
                                                ValueNotifier(false);
                                            isConnectingOrDisconnecting[
                                                    d.remoteId]!
                                                .value = false;
                                            setState(() {});
                                          });
                                          /* Navigator.of(context).push(
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
                                                    return Test(device: d);
                                                  },
                                                  settings: const RouteSettings(
                                                      name: '/deviceScreen'))); */
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
                              onTap: () async {
                                testProvider.devicet = r.device;
                                print("r--------------------------");
                                print(testProvider.devicet);
                                isConnectingOrDisconnecting[
                                    r.device.remoteId] ??= ValueNotifier(true);
                                isConnectingOrDisconnecting[r.device.remoteId]!
                                    .value = true;
                                r.device
                                    .connect(
                                        timeout: const Duration(seconds: 35))
                                    .catchError((e) {
                                  final snackBar = snackBarFail(
                                      prettyException("Connect Error:", e));
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
                                  setState(() {});
                                });
                              } /* =>
                                Navigator.of(context).push(MaterialPageRoute(
                              builder: (context) {
                                isConnectingOrDisconnecting[
                                    r.device.remoteId] ??= ValueNotifier(true);
                                isConnectingOrDisconnecting[r.device.remoteId]!
                                    .value = true;
                                r.device
                                    .connect(
                                        timeout: const Duration(seconds: 35))
                                    .catchError((e) {
                                  final snackBar = snackBarFail(
                                      prettyException("Connect Error:", e));
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
                                print("Clicked!");
                                return Test(device: r.device);
                              },
                              /* settings: const RouteSettings(
                                        name: '/deviceScreen') */
                            )), */
                              ),
                        )
                        .toList(),
                  ),
                ),
              ],
            ),
          ),
        ),
        /* bottomNavigationBar: ClipRRect(
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(25),
            topRight: Radius.circular(25),
          ),
          child: BottomAppBar(
              height: 72,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  const SwitchExample(),
                  TextButton(onPressed: () {}, child: const Text("SCAN")),
                ],
              )),
        ), */
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

String prettyException(String prefix, dynamic e) {
  if (e is FlutterBluePlusException) {
    return "$prefix ${e.description}";
  } else if (e is PlatformException) {
    return "$prefix ${e.message}";
  }
  return prefix + e.toString();
}

SnackBar snackBarGood(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.blue);
}

SnackBar snackBarFail(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.red);
}

class Test extends StatelessWidget {
  final BluetoothDevice device;

  const Test({Key? key, required this.device}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const ScaffoldMessenger(child: Text("!"));
  }
}

class Testprovide extends ChangeNotifier {
  BluetoothDevice? devicet;
  @override
  notifyListeners();
  //Testprovide(this.device_t);
}
