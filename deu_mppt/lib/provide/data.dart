import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';

class DeviceId with ChangeNotifier {
  BluetoothDevice? _device;

  BluetoothDevice? get device => _device;

  void setDevice(BluetoothDevice? id) {
    _device = id;
    //notifyListeners();
  }
}

class BluetoothData with ChangeNotifier {
  String _data = "";

  String? get data => _data;

  List<int> buff = [];
  List<int> buffer = [];
  List<int> checkSumData = [];
  List<int> decoDedata = [];
  List<int> animalchar = [];
  List<int> ranchar = [];

  // 추가 데이터를 받아서 _data에 추가하는 함수
  void addData(List<int> additionalData) {
    //_data ??= [];
    Uint8List bytes;
    Uint8List decodeBytes;

    String result = '';
    int buffsum = 0;

    checkSumData = [];
    decoDedata = [];

    //_data = additionalData;

    print(
        "<-------------------------------------- Process 1 !!! -------------------------------------->");
    buff.addAll(additionalData);
    for (int i = 0; i < buff.length; i++) {
      buffsum += buff[i];
    }
    print("buffsum is : $buffsum");

    if (buffsum != 0) {
      print("Recive value is = $additionalData");

      //Check value length
      int valueLength = additionalData.length;
      print("valuelenghth = $valueLength");

      //받은 데이터의 길이를 알기 위해서
      bytes = Uint8List.fromList(additionalData);
      ByteData byteData = ByteData.sublistView(bytes);
      const int byteLength = 200;

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
      if ((buffer.length < byteLength) && (additionalData != null)) {
        buffer.addAll(additionalData);
        if (buffer.length <= 96) {
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
            for (var i = 0; i <= decodeBytedata.lengthInBytes - 24; i += 24) {
              int short2byteInt = decodeBytedata.getInt16(i, Endian.little);
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

              int byte2Int1 = decodeBytedata.getInt16(i + 13, Endian.little);
              result += '$byte2Int1, ';

              int byte2Int2 = decodeBytedata.getInt16(i + 15, Endian.little);
              result += '$byte2Int2, ';

              int byte2Int3 = decodeBytedata.getInt16(i + 17, Endian.little);
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
          _data = result;
          //context.read<ResultProvider>().updateResult(result);

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

    notifyListeners();
  }
}
