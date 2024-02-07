//PACKAGES
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'package:permission_handler/permission_handler.dart';

//SCREEN
import 'package:deulog_noserver/screen/login.dart';
import 'package:deulog_noserver/screen/drawer.dart';
import 'package:deulog_noserver/screen/account.dart';

//PROVIDER
import 'package:deulog_noserver/provider/mppt_data.dart';

void main() {
  if (Platform.isAndroid) {
    SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent, // Make the status bar transparent
      statusBarIconBrightness: Brightness.dark, // Set the text color to black
    ));

    WidgetsFlutterBinding.ensureInitialized();
    [
      Permission.location,
      Permission.storage,
      Permission.bluetooth,
      Permission.bluetoothConnect,
      Permission.bluetoothScan
    ].request().then((status) {
      runApp(MultiProvider(
        providers: [
          ChangeNotifierProvider(
            create: (context) => MpptData(),
          ),
        ],
        child: const MyApp(),
      ));
    });
  } else {
    runApp(const MyApp());
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          fontFamily: 'Pretendard',
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple)
              .copyWith(background: const Color(0xFFF1F3F5)),
        ),
        initialRoute: '/',
        routes: {
          '/': (context) => const LoginScreen(),
          '/drawer': (context) => const DrawerScreen(),
          '/account': (context) => const CreateAccountScreen(),
        });
  }
}
