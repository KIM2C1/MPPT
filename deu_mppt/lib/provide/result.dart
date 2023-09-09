import 'package:flutter/material.dart';

class ResultProvider with ChangeNotifier {
  String _result = '';

  String get result => _result;

  void updateResult(String newValue) {
    _result = newValue;
    //notifyListeners();
  }
}
