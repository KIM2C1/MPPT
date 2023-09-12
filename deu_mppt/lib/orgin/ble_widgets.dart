import 'dart:async';
import 'dart:typed_data';
import 'package:flutter/material.dart';

import 'package:provider/provider.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';

import 'package:deu_mppt/provide/result.dart';

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
      trailing: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.black,
          foregroundColor: Colors.white,
        ),
        onPressed: (result.advertisementData.connectable) ? onTap : null,
        child: const Text('CONNECT'),
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

class ServiceTile extends StatelessWidget {
  final BluetoothService service;
  final List<CharacteristicTile> characteristicTiles;

  const ServiceTile(
      {Key? key, required this.service, required this.characteristicTiles})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (characteristicTiles.isNotEmpty) {
      return ExpansionTile(
        title: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            const Text('Service'),
            Text('0x${service.serviceUuid.toString().toUpperCase()}',
                style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                    color: Theme.of(context).textTheme.bodySmall?.color))
          ],
        ),
        children: characteristicTiles,
      );
    } else {
      return ListTile(
        title: const Text('Service'),
        subtitle: Text('0x${service.serviceUuid.toString().toUpperCase()}'),
      );
    }
  }
}

class CharacteristicTile extends StatefulWidget {
  final BluetoothCharacteristic characteristic;
  final List<DescriptorTile> descriptorTiles;
  final Future<void> Function()? onReadPressed;
  final Future<void> Function()? onWritePressed;
  final Future<void> Function()? onAutoPressed;
  final Future<void> Function()? onNotificationPressed;

  const CharacteristicTile(
      {Key? key,
      required this.characteristic,
      required this.descriptorTiles,
      this.onReadPressed,
      this.onWritePressed,
      this.onAutoPressed,
      this.onNotificationPressed})
      : super(key: key);

  @override
  State<CharacteristicTile> createState() => _CharacteristicTileState();
}

class _CharacteristicTileState extends State<CharacteristicTile> {
  List<int> buff = [];
  List<int> buffer = [];
  List<int> checkSumData = [];
  List<int> decoDedata = [];
  List<int> animalchar = [];
  List<int> ranchar = [];

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<List<int>>(
      stream: widget.characteristic.onValueReceived,
      initialData: widget.characteristic.lastValue,
      builder: (context, snapshot) {
        final List<int>? value = snapshot.data;

        Uint8List bytes;
        Uint8List decodeBytes;

        String result = '';
        int buffsum = 0;

        checkSumData = [];
        decoDedata = [];

        print(
            "<-------------------------------------- Process 1 !!! -------------------------------------->");
        if (value != null) {
          buff.addAll(value);
          for (int i = 0; i < buff.length; i++) {
            buffsum += buff[i];
          }
          print("buffsum is : $buffsum");

          if (buffsum != 0) {
            print("Recive value is = $value");

            //Check value length
            int valueLength = value.length;
            print("valuelenghth = $valueLength");

            //받은 데이터의 길이를 알기 위해서
            bytes = Uint8List.fromList(value);
            ByteData byteData = ByteData.sublistView(bytes);
            const int byteLength = 172;

            //Create XOR Check Sum
            int calculateChecksum8Mod256(List<int> data) {
              int sum = 0;
              for (int i = 0; i < data.length; i++) {
                sum += data[i];
              }
              int checksum = sum % 256;
              return checksum;
            }

            //8bit bool calculation
            bool bitcal(int value) {
              return (value & 0x80) != 0;
            }

            //Add value to buffer
            if ((buffer.length < byteLength) && (value != null)) {
              buffer.addAll(value);
              if (buffer.length <= 44) {
                buffer = [];
              }

              //print(buffer);
            }
            if (buffer.length >= byteLength) {
              print(
                  "<-------------------------------------- Process 2 !!! -------------------------------------->");
              print("Buffer is : $buffer");

              //buffer에서 checksum과 decode할 데이터 분리
              for (int i = 0; i < buffer.length; i++) {
                if (i < buffer.length - 4) {
                  checkSumData.add(buffer[i]);
                }

                if (i < buffer.length - 4) {
                  decoDedata.add(buffer[i]);
                }
              }
              decodeBytes = Uint8List.fromList(decoDedata);
              ByteData decodeBytedata = ByteData.sublistView(decodeBytes);

              int checkSumDatalength = checkSumData.length;
              int decoDedatalength = decoDedata.length;

              print(
                  "<-------------------------------------- Process 3 !!! -------------------------------------->");
              print("checkSumData : $checkSumData");
              print("checkSumData_length : $checkSumDatalength");
              print(
                  "<------------------------------------------------------------------------------------------->");
              print("decoDedata : $decoDedata");
              print("decoDedata_length : $decoDedatalength");
              print(
                  "<------------------------------------------------------------------------------------------->");
              int check = calculateChecksum8Mod256(checkSumData);
              print("checksum = $check");

              print(
                  "<-------------------------------------- Process 4 !!! -------------------------------------->");
              //디코드 시작
              if (decodeBytedata.lengthInBytes > 0) {
                {
                  for (var i = 0;
                      i <= decodeBytedata.lengthInBytes - 24;
                      i += 24) {
                    int short2byteInt =
                        decodeBytedata.getInt16(i, Endian.little);
                    if (short2byteInt < 0) {
                      short2byteInt = 65536 + short2byteInt;
                    }
                    result += '$short2byteInt, ';

                    double sin4byteFloat =
                        decodeBytedata.getFloat32(i + 2, Endian.little);
                    String sinFloat = sin4byteFloat.toStringAsFixed(2);
                    result += '$sinFloat, ';

                    double cos4byteFloat =
                        decodeBytedata.getFloat32(i + 6, Endian.little);
                    String cosFloat = cos4byteFloat.toStringAsFixed(2);
                    result += '$cosFloat, ';

                    for (int j = i + 10; j <= i + 12; j++) {
                      animalchar.add(decodeBytes[j]);
                    }
                    result += String.fromCharCodes(animalchar);
                    result += ',';
                    animalchar = [];

                    int byte2Int1 =
                        decodeBytedata.getInt16(i + 13, Endian.little);
                    result += '$byte2Int1, ';

                    int byte2Int2 =
                        decodeBytedata.getInt16(i + 15, Endian.little);
                    result += '$byte2Int2, ';

                    int byte2Int3 =
                        decodeBytedata.getInt16(i + 17, Endian.little);
                    result += '$byte2Int3, ';

                    int byte1Int1 = decodeBytedata.getInt8(i + 19);
                    if (bitcal(byte1Int1) == true) {
                      result += '$byte1Int1, ';
                    } else {
                      byte1Int1 = byte1Int1;
                      result += '$byte1Int1, ';
                    }

                    for (int j = i + 20; j <= i + 22; j++) {
                      ranchar.add(decodeBytes[j]);
                    }
                    result += String.fromCharCodes(ranchar);
                    result += ',';
                    ranchar = [];

                    int byte1Int2 = decodeBytedata.getInt8(i + 23);
                    if (bitcal(byte1Int2) == true) {
                      result += '$byte1Int2,';
                    } else {
                      byte1Int2 = byte1Int2;
                      result += '$byte1Int2 ';
                    }
                  }
                }

                print(
                    "<-------------------------------------- Result !!! -------------------------------------->");
                //결과 출력및 버퍼 초기화
                print("result = $result");
                context.read<ResultProvider>().updateResult(result);

                buffer = [];
                checkSumData = [];
                decoDedata = [];
                decodeBytes = Uint8List.fromList(decoDedata);
                decodeBytedata = ByteData.sublistView(decodeBytes);
              }
            }
          } else {
            print(
                "<-------------------------------------- buffsum is 0! -------------------------------------->");
          }
          buff = [];
          buffsum = 0;
          print(
              "<-------------------------------------- RECIVE END !!! -------------------------------------->");
        }
        return ExpansionTile(
          title: ListTile(
            title: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  const Text('Characteristic'),
                  Text(
                    '0x${widget.characteristic.characteristicUuid.toString().toUpperCase()}',
                    style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: Theme.of(context).textTheme.bodySmall?.color),
                  ),
                  Column(
                    children: [
                      Row(
                        children: [
                          if (widget.characteristic.properties.read)
                            TextButton(
                                child: const Text("Read"),
                                onPressed: () async {
                                  await widget.onReadPressed!();
                                  setState(() {});
                                }),
                          if (widget.characteristic.properties.write)
                            TextButton(
                                child: Text(widget.characteristic.properties
                                        .writeWithoutResponse
                                    ? "WriteNoResp"
                                    : "Write"),
                                onPressed: () async {
                                  await widget.onWritePressed!();
                                  setState(() {});
                                }),
                          if (widget.characteristic.properties.notify ||
                              widget.characteristic.properties.indicate)
                            TextButton(
                                child: Text(widget.characteristic.isNotifying
                                    ? "Unsubscribe"
                                    : "Subscribe"),
                                onPressed: () async {
                                  await widget.onNotificationPressed!();
                                  setState(() {});
                                }),
                        ],
                      ),
                    ],
                  )
                ],
              ),
            ),
            subtitle: Text(result.toString()),
            contentPadding: const EdgeInsets.all(0.0),
          ),
          children: widget.descriptorTiles,
        );
      },
    );
  }
}

class DescriptorTile extends StatelessWidget {
  final BluetoothDescriptor descriptor;
  final VoidCallback? onReadPressed;
  final VoidCallback? onWritePressed;

  const DescriptorTile(
      {Key? key,
      required this.descriptor,
      this.onReadPressed,
      this.onWritePressed})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          const Text('Descriptor'),
          Text('0x${descriptor.descriptorUuid.toString().toUpperCase()}',
              style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                  color: Theme.of(context).textTheme.bodySmall?.color))
        ],
      ),
      subtitle: StreamBuilder<List<int>>(
        stream: descriptor.onValueReceived,
        initialData: descriptor.lastValue,
        builder: (c, snapshot) => Text(snapshot.data.toString()),
      ),
      trailing: Row(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          IconButton(
            icon: Icon(
              Icons.file_download,
              color: Theme.of(context).iconTheme.color?.withOpacity(0.5),
            ),
            onPressed: onReadPressed,
          ),
          IconButton(
            icon: Icon(
              Icons.file_upload,
              color: Theme.of(context).iconTheme.color?.withOpacity(0.5),
            ),
            onPressed: onWritePressed,
          )
        ],
      ),
    );
  }
}

class AdapterStateTile extends StatelessWidget {
  const AdapterStateTile({Key? key, required this.adapterState})
      : super(key: key);

  final BluetoothAdapterState adapterState;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.redAccent,
      child: ListTile(
        title: Text(
          'Bluetooth adapter is ${adapterState.toString().split(".").last}',
          style: Theme.of(context).primaryTextTheme.titleSmall,
        ),
        trailing: Icon(
          Icons.error,
          color: Theme.of(context).primaryTextTheme.titleSmall?.color,
        ),
      ),
    );
  }
}

SnackBar snackBarGood(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.blue);
}

SnackBar snackBarFail(String message) {
  return SnackBar(content: Text(message), backgroundColor: Colors.red);
}
