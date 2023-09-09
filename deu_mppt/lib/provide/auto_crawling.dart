import 'dart:async';
import 'package:flutter/material.dart';

class AutoProvider with ChangeNotifier {
  Timer? _timer;
  bool _isAutoEnabled = false;

  bool get isAutoEnabled => _isAutoEnabled;

  void toggleAuto() {
    _isAutoEnabled = !_isAutoEnabled;
    notifyListeners();
  }

  void startAutoWriting() {
    _timer = Timer.periodic(const Duration(milliseconds: 200), (timer) {
      if (_isAutoEnabled) {
        print("!!!!!!!!!!!!!");
        //onWritePressed?.call();
      }
    });
  }

  void stopAutoWriting() {
    _timer?.cancel();
  }
}
