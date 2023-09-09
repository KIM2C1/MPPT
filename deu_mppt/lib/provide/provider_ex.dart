import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

class DeviceData {
  final String name;
  final String connectionStatus;
  final int value;

  DeviceData(this.name, this.connectionStatus, this.value);
}

class DeviceProvider extends ChangeNotifier {
  DeviceData _deviceStatus = DeviceData('Device Name', 'Connected', 0);
  Timer? _timer;
  bool _autoUpdateEnabled = false;

  DeviceProvider() {
    _startAutoUpdate();
  }

  DeviceData get deviceStatus => _deviceStatus;

  bool get autoUpdateEnabled => _autoUpdateEnabled;

  void _startAutoUpdate() {
    if (_autoUpdateEnabled) {
      _timer = Timer.periodic(const Duration(milliseconds: 200), (timer) {
        final newValue = Random().nextInt(255) + 1;
        _updateValue(newValue);
      });
    }
  }

  void _updateValue(int newValue) {
    _deviceStatus = DeviceData(
      _deviceStatus.name,
      _deviceStatus.connectionStatus,
      newValue,
    );
    notifyListeners();
  }

  void toggleAutoUpdate(bool enabled) {
    _autoUpdateEnabled = enabled;
    if (_autoUpdateEnabled) {
      _startAutoUpdate();
    } else {
      _timer?.cancel();
    }
    notifyListeners();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
}
