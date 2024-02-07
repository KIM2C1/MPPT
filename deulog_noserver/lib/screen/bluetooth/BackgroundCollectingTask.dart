import 'dart:async';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:deulog_noserver/provider/mppt_data.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';

class BackgroundCollectingTask extends Model {
  List<int> buffersum = [];

  static BackgroundCollectingTask of(
    BuildContext context, {
    bool rebuildOnChange = false,
  }) =>
      ScopedModel.of<BackgroundCollectingTask>(
        context,
        rebuildOnChange: rebuildOnChange,
      );

  final BluetoothConnection _connection;
  final List<int> _buffer = List<int>.empty(growable: true);

  bool inProgress = false;

  BackgroundCollectingTask._fromConnection(this._connection, context) {
    final mppt = Provider.of<MpptData>(context, listen: false);

    List<int> intlist = [];
    List<int> buff = [];
    List<int> buffer = [];
    List<int> checkSumData = [];
    List<int> decoDedata = [];
    List<int> strchar = [];
    List<String> strchar1 = [];

    String intTostr(int input) {
      if (input == 0.toInt()) {
        return '$input';
      } else {
        final iterable = [input];
        return String.fromCharCodes(iterable);
      }
    }

    _connection.input!.listen((data) {
      buffersum.addAll(data);

      if (buffersum.length == 200) {
        int tf = buffersum.length;
        print("Buffer is : $buffersum");
        print("Buffer Length is : $tf");

        Uint8List bytes;
        Uint8List decodeBytes;
        String combinedString = "";
        String result = '';
        int buffsum = 0;
        checkSumData = [];
        decoDedata = [];
        print(
            "<-------------------------------------- Process 1 !!! -------------------------------------->");
        buff.addAll(buffersum);
        for (int i = 0; i < buff.length; i++) {
          buffsum += buff[i];
        }
        print("buffsum is : $buffsum");

        if (buffsum != 0) {
          print("Recive value is = $buffersum");

          //Check value length
          int valueLength = buffersum.length;
          print("valuelenghth = $valueLength");

          //받은 데이터의 길이를 알기 위해서
          bytes = Uint8List.fromList(buffersum);
          //ByteData byteData = ByteData.sublistView(bytes);
          const int byteLength = 200;

          //8bit bool calculation
          bool bitcal(int value) {
            return (value & 0x80) != 0;
          }

          //Add value to buffer
          if ((buffer.length < byteLength) /* && (additionalData != null) */) {
            buffer.addAll(buffersum);
            if (buffer.length <= 95) {
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
              if (i < buffer.length - 2) {
                checkSumData.add(buffer[i]);
              }

              if (i < buffer.length - 2) {
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
            print(
                "<-------------------------------------- Process 4 !!! -------------------------------------->");
            //디코드 시작
            if (decodeBytedata.lengthInBytes > 0) {
              {
                // start decoding
                for (int i = 0; i <= 6; i++) {
                  strchar.add(decodeBytes[i]);
                  result += String.fromCharCodes(strchar);
                  strchar = [];
                }

                result += ",";

                strchar1.add(decodeBytes[7].toString());
                result += decodeBytes[7].toString();
                result += ",";
                print("Complete......................[1/17]");
                strchar1 = [];

                // grid_vol, V
                for (int i = 8; i <= 11; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }

                int combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                //summation(3, intlistBuff);
                result += "V";
                result += ",";
                print("Complete......................[2/17]");

                // grid_freq,Hz
                for (int i = 12; i <= 14; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }

                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "Hz";
                result += ",";
                print("Complete......................[3/17]");

                // ac_out_vol, V
                // 십진수 0
                for (int i = 15; i <= 18; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString; //string 필요
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "V";
                result += ",";
                print("Complete......................[4/17]");

                // ac_out_freq,Hz
                for (int i = 19; i <= 21; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString; //string 필요
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "Hz";
                result += ",";
                print("Complete......................[5/17]");

                // ac_out_app_pow
                for (int i = 22; i <= 25; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "W";
                result += ",";
                print("Complete......................[6/17]");

                // ac_out_act_pow
                for (int i = 26; i <= 29; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "W";
                result += ",";
                print("Complete......................[7/17]");

                //out_load_percent
                for (int i = 30; i <= 32; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "%";
                result += ",";
                print("Complete......................[8/17]");

                // bat_vol
                for (int i = 33; i <= 35; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "V";
                result += ",";
                print("Complete......................[9/17]");

                // bat_charg_cur
                for (int i = 36; i <= 38; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "A";
                result += ",";
                print("Complete......................[10/17]");

                // bat_discharg_cur
                for (int i = 39; i <= 43; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "A";
                result += ",";
                print("Complete......................[11/17]");

                // bat_capacity
                for (int i = 44; i <= 46; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "%";
                result += ",";
                print("Complete......................[12/17]");

                // pv_in_curr
                for (int i = 47; i <= 50; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "A";
                result += ",";
                print("Complete......................[13/17]");

                // pv_in_vol
                for (int i = 51; i <= 54; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "V";
                result += ",";
                print("Complete......................[14/17]");

                // pv_charge_power
                for (int i = 55; i <= 59; i++) {
                  String trString =
                      intTostr(decodeBytes[i]); // 받은 데이터를 string으로 변환, null도
                  combinedString += trString;
                  result += trString;
                }
                combinedInt = int.parse(combinedString);
                intlist.add(combinedInt);
                combinedString = "";
                result += "W";
                result += ",";

                /* int byteint = decodeBytedata.getInt8(60);
            result += "$byteint";
            result += ","; */

                print("Complete......................[15/17]");

                //can_node_data

                for (int i = 0; i <= 73; i += 24) {
                  //Raw voltage in 0.1V
                  int highByte = decodeBytedata.getInt8(60 + i);
                  int lowByte = decodeBytedata.getInt8(61 + i);

                  // Account for potential sign issues with getInt8 for values >= 128.
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;

                  int combinedValue = (highByte << 8) + lowByte;
                  intlist.add(combinedValue);
                  double voltage = combinedValue / 10.0;

                  result += "$voltage";
                  result += "V";
                  result += ",";

                  int highByteMost = decodeBytedata.getInt8(62 + i);
                  highByte = decodeBytedata.getInt8(63 + i);
                  lowByte = decodeBytedata.getInt8(64 + i);
                  int lowByteLeast = decodeBytedata.getInt8(65 + i);

                  if (highByteMost < 0) highByteMost += 256;
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;
                  if (lowByteLeast < 0) lowByteLeast += 256;

                  combinedValue = (highByteMost << 24) |
                      (highByte << 16) |
                      (lowByte << 8) |
                      lowByteLeast;
                  intlist.add(combinedValue);
                  double current = combinedValue / 1000.0;

                  result += "$current";
                  result +=
                      "A"; // It's current, so using 'A' (for Amperes) instead of 'V' (Volts)
                  result += ",";

                  //Raw Frequency in 0.1Hz
                  highByte = decodeBytedata.getInt8(66 + i);
                  lowByte = decodeBytedata.getInt8(67 + i);

                  // Account for potential sign issues with getInt8 for values >= 128.
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;

                  combinedValue = (highByte << 8) + lowByte;
                  intlist.add(combinedValue);
                  voltage = combinedValue / 10.0;

                  result += "$voltage";
                  result += "Hz";
                  result += ",";

                  //Raw Raw power in 0.1W
                  highByteMost = decodeBytedata.getInt8(68 + i);
                  highByte = decodeBytedata.getInt8(69 + i);
                  lowByte = decodeBytedata.getInt8(70 + i);
                  lowByteLeast = decodeBytedata.getInt8(71 + i);

                  // Account for potential sign issues with getInt8 for values >= 128.
                  if (highByteMost < 0) highByteMost += 256;
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;
                  if (lowByteLeast < 0) lowByteLeast += 256;

                  combinedValue = (highByteMost << 24) |
                      (highByte << 16) |
                      (lowByte << 8) |
                      lowByteLeast;
                  intlist.add(combinedValue);
                  double power = combinedValue / 10.0;

                  result += "$power";
                  result += "W"; // It's power, so using 'W' (for Watts)
                  result += ",";

                  //Raw Raw Energy in 1Wh
                  highByteMost = decodeBytedata.getInt8(72 + i);
                  highByte = decodeBytedata.getInt8(73 + i);
                  lowByte = decodeBytedata.getInt8(74 + i);
                  lowByteLeast = decodeBytedata.getInt8(75 + i);

                  if (highByteMost < 0) highByteMost += 256;
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;
                  if (lowByteLeast < 0) lowByteLeast += 256;

                  combinedValue = (highByteMost << 24) |
                      (highByte << 16) |
                      (lowByte << 8) |
                      lowByteLeast;
                  intlist.add(combinedValue);
                  current = combinedValue / 1000.0;

                  result += "$current";
                  result +=
                      "Wh"; // It's current, so using 'A' (for Amperes) instead of 'V' (Volts)
                  result += ",";

                  //Raw pf in 0.01
                  highByte = decodeBytedata.getInt8(76 + i);
                  lowByte = decodeBytedata.getInt8(77 + i);

                  // Account for potential sign issues with getInt8 for values >= 128.
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;

                  combinedValue = (highByte << 8) + lowByte;
                  intlist.add(combinedValue);
                  voltage = combinedValue / 10.0;

                  result += "$voltage";
                  result += ",";

                  //Raw alarm value
                  highByte = decodeBytedata.getInt8(78 + i);
                  lowByte = decodeBytedata.getInt8(79 + i);

                  // Account for potential sign issues with getInt8 for values >= 128.
                  if (highByte < 0) highByte += 256;
                  if (lowByte < 0) lowByte += 256;

                  combinedValue = (highByte << 8) + lowByte;
                  intlist.add(combinedValue);
                  voltage = combinedValue / 10.0;

                  result += "$voltage";
                  result += ",";

                  int byteint_1 = decodeBytedata.getInt8(80 + i);
                  intlist.add(byteint_1);
                  result += "$byteint_1";
                  int byteint_2 = decodeBytedata.getInt8(81 + i);
                  //intlist.add(byteint_2);
                  result += "$byteint_2";
                  int byteint_3 = decodeBytedata.getInt8(82 + i);
                  //intlist.add(byteint_3);
                  result += "$byteint_3";
                  int byteint_4 = decodeBytedata.getInt8(83 + i);
                  //intlist.add(byteint_4);
                  result += "$byteint_4";
                }
                print("Complete......................[16/17]");
                int byteint5 = decodeBytedata.getInt8(156);
                intlist.add(byteint5);

                int byteint6 = decodeBytedata.getInt8(157);
                intlist.add(byteint6);

                for (int i = 158; i <= 196; i++) {
                  int byteint = decodeBytedata.getInt8(i);
                  result += "$byteint";
                  result += ",";
                }
                int chkSum = 0;
                print("Complete......................[17/17]");

                for (int i = 8; i < 197; i++) {
                  chkSum = chkSum + decodeBytedata.getInt8(i);
                }
                result += "$chkSum";
                //data = intlist;
                print(data);
              }

              print(
                  "<-------------------------------------- Result !!! -------------------------------------->");
              //결과 출력및 버퍼 초기화
              print("result = $result");
              print("intlist = $intlist");

              mppt.saveMppt(intlist);

              intlist = [];
              buffer = [];
              checkSumData = [];
              decoDedata = [];
              decodeBytes = Uint8List.fromList(decoDedata);
              decodeBytedata = ByteData.sublistView(decodeBytes);

              //158번 부터 빈 데이터
            }
          }
        } else {
          print(
              "<-------------------------------------- buffsum is 0! -------------------------------------->");
        }
        buff = [];
        buffsum = 0;
        print(
            "<-------------------------------------- RECEIVE END !!! -------------------------------------->");

        buffersum = [];
      }
    }).onDone(() {
      inProgress = false;
    });
  }

  static Future<BackgroundCollectingTask> connect(
      BluetoothDevice server, BuildContext context) async {
    final BluetoothConnection connection =
        await BluetoothConnection.toAddress(server.address);
    return BackgroundCollectingTask._fromConnection(connection, context);
  }

  void dispose() {
    _connection.dispose();
  }

  Future<void> start(BuildContext context) async {
    final nodeState = Provider.of<MpptData>(context, listen: false);

    List<int> nodesend = [];
    Uint8List nodesend_8;

    inProgress = true;
    _buffer.clear();
    notifyListeners();
    //_connection.output.add(ascii.encode('start'));
    //await _connection.output.allSent;

    const oneSecond0 = Duration(milliseconds: 500);
    Timer.periodic(oneSecond0, (timer) async {
      switch (nodeState.loading) {
        case 0:
          if (nodeState.nodeState[0]) {
            //node ON
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x01, 0x00, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          } else {
            //node OFF
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x01, 0x01, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          }

        case 1:
          if (nodeState.nodeState[1]) {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x02, 0x00, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          } else {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x02, 0x01, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          }

        case 2:
          if (nodeState.nodeState[3]) {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x03, 0x00, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          } else {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x03, 0x01, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          }

        case 3:
          if (nodeState.nodeState[3]) {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x04, 0x00, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          } else {
            nodesend = [0x23, 0x43, 0x4D, 0x44, 0x04, 0x01, 0x40];
            nodesend_8 = Uint8List.fromList(nodesend);
            nodeState.togglePower(4);
            if (inProgress == true) {
              _connection.output.add(nodesend_8);
              await _connection.output.allSent;
            }
          }

        case 4:
          nodesend = [];
          nodeState.togglePower(4);
      }
    });

    // n초마다 데이터 전송
    const oneSecond = Duration(seconds: 1);
    Timer.periodic(oneSecond, (timer) async {
      if (nodeState.loading == 4) {
        List<int> myList = [0x23, 0x52, 0x45, 0x51, 0x30, 0x31, 0x40];
        Uint8List uint8List = Uint8List.fromList(myList);
        if (inProgress == true) {
          _connection.output.add(uint8List);
          await _connection.output.allSent;
        }
      }
    });
  }

  Future<void> cancel() async {
    inProgress = false;
    notifyListeners();
    await _connection.finish();
  }

  Future<void> pause() async {
    inProgress = false;
    notifyListeners();
    await _connection.output.allSent;
  }

  Future<void> reasume() async {
    inProgress = true;
    notifyListeners();
    await _connection.output.allSent;
  }
}
