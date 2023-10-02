import 'dart:async';
import 'package:flutter/material.dart';

class XValueProvider with ChangeNotifier {
  double _xValue = 0;
  double get xValue => _xValue;

  XValueProvider() {
    // Periodically update xValue every 1 second
    Timer.periodic(const Duration(milliseconds: 40), (timer) {
      _xValue += 0.05; // Update xValue as needed
      notifyListeners();
    });
  }
}
