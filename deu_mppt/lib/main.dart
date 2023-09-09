/*플러터 기본 라이브러리*/
import 'dart:io';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

/*플러터 외부 라이브러리*/
import 'package:provider/provider.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';
import 'package:permission_handler/permission_handler.dart';

/*내부 파일 Import*/
import 'package:deu_mppt/screen/login.dart';
import 'package:deu_mppt/screen/draw.dart';
import 'package:deu_mppt/screen/home.dart';
import 'package:deu_mppt/screen/chart.dart';
import 'package:deu_mppt/screen/profile.dart';
import 'package:deu_mppt/screen/find_device.dart';
import 'package:deu_mppt/screen/setting.dart';
import 'package:deu_mppt/orgin/ble_main.dart';

import 'package:deu_mppt/provide/provider_ex.dart';
import 'package:deu_mppt/provide/result.dart';
import 'package:deu_mppt/provide/auto_crawling.dart';

void main() {
  if (Platform.isAndroid) {
    SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
    ));
    WidgetsFlutterBinding.ensureInitialized();
    [
      Permission.location,
      Permission.storage,
      Permission.bluetooth,
      Permission.bluetoothConnect,
      Permission.bluetoothScan
    ].request().then(
      (status) {
        runApp(
          MultiProvider(
            providers: [
              ChangeNotifierProvider(create: (_) => DeviceProvider()),
              ChangeNotifierProvider(create: (_) => Testprovide()),
              ChangeNotifierProvider(create: (_) => ResultProvider()),
              ChangeNotifierProvider(create: (_) => AutoProvider()),
            ],
            child: const LoginApp(),
          ),
        );
      },
    );
  } else {
    runApp(
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => DeviceProvider()),
          ChangeNotifierProvider(create: (_) => Testprovide()),
          ChangeNotifierProvider(create: (_) => ResultProvider()),
          ChangeNotifierProvider(create: (_) => AutoProvider()),
        ],
        child: const LoginApp(),
      ),
    );
  }
}

class BluetoothAdapterStateObserver extends NavigatorObserver {
  StreamSubscription<BluetoothAdapterState>? _btStateSubscription;

  @override
  void didPush(Route route, Route? previousRoute) {
    super.didPush(route, previousRoute);
    if (route.settings.name == '/deviceScreen') {
      // Start listening to Bluetooth state changes when a new route is pushed
      _btStateSubscription ??= FlutterBluePlus.adapterState.listen((state) {
        if (state != BluetoothAdapterState.on) {
          // Pop the current route if Bluetooth is off
          navigator?.pop();
        }
      });
    }
  }

  @override
  void didPop(Route route, Route? previousRoute) {
    super.didPop(route, previousRoute);
    // Cancel the subscription when the route is popped
    _btStateSubscription?.cancel();
    _btStateSubscription = null;
  }
}

class LoginApp extends StatelessWidget {
  const LoginApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const LoginScreen(),
        '/draw': (context) => const DrawScreen(),
        '/home': (context) => const HomeScreen(),
        '/chart': (context) => const ChartScreen(),
        '/profile': (context) => const ProfileScreen(),
        '/device': (context) => const FindDevicesScreen(),
        '/my_device': (context) => const DeviceScreenMy(),
        '/setting': (context) => const SettingScreen(),
      },
    );
  }
}
