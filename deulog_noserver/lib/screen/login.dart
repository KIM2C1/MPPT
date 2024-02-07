import 'package:flutter/material.dart';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';
import 'bluetooth/SelectBondedDevicePage.dart';
import 'bluetooth/BackgroundCollectingTask.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController idController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  bool isPasswordVisible = true;

  BackgroundCollectingTask? _collectingTask;

  void clearTextFields() {
    idController.clear();
    passwordController.clear();
  }

  void togglePasswordVisibility() {
    setState(() {
      isPasswordVisible = !isPasswordVisible;
    });
  }

  @override
  Widget build(BuildContext context) {
    final screenHeight = MediaQuery.of(context).size.height;
    final screenWidth = MediaQuery.of(context).size.width;

    return GestureDetector(
      onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
      child: Scaffold(
        body: Center(
          child: ListView(
            children: [
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: Container(
                  height: screenHeight * 0.9,
                  width: screenWidth * 0.9,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                  child: Column(
                    children: [
                      Expanded(
                        flex: 5,
                        child: Padding(
                          padding: const EdgeInsets.all(20.0),
                          child: Image.asset(
                            "images/AutoREX.png",
                            height: 40,
                            width: screenHeight * 0.3,
                          ),
                        ),
                      ),
                      Expanded(
                        flex: 2,
                        child: Padding(
                          padding: const EdgeInsets.all(30.0),
                          child: Column(
                            children: [
                              Flexible(
                                child: TextField(
                                  controller: idController,
                                  enableSuggestions: false,
                                  autocorrect: false,
                                  decoration: const InputDecoration(
                                    labelText: 'ID',
                                    border: OutlineInputBorder(),
                                    focusedBorder: OutlineInputBorder(
                                        borderSide:
                                            BorderSide(color: Colors.blue)),
                                    enabledBorder: OutlineInputBorder(
                                        borderSide:
                                            BorderSide(color: Colors.black)),
                                  ),
                                  textInputAction: TextInputAction.next,
                                ),
                              ),
                              const SizedBox(height: 15),
                              Flexible(
                                child: TextField(
                                  controller: passwordController,
                                  enableSuggestions: false,
                                  autocorrect: false,
                                  obscureText: isPasswordVisible,
                                  decoration: InputDecoration(
                                    labelText: 'Password',
                                    border: const OutlineInputBorder(),
                                    suffixIcon: GestureDetector(
                                      behavior: HitTestBehavior.translucent,
                                      child: IconButton(
                                        onPressed: togglePasswordVisibility,
                                        splashColor: Colors.transparent,
                                        highlightColor: Colors.transparent,
                                        icon: Icon(
                                          isPasswordVisible
                                              ? Icons.visibility_off
                                              : Icons.visibility,
                                          color: Colors.grey,
                                        ),
                                      ),
                                    ),
                                    focusedBorder: const OutlineInputBorder(
                                      borderSide:
                                          BorderSide(color: Colors.blue),
                                    ),
                                    enabledBorder: const OutlineInputBorder(
                                      borderSide:
                                          BorderSide(color: Colors.black),
                                    ),
                                  ),
                                  textInputAction: TextInputAction.done,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      Expanded(
                        flex: 1,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            ElevatedButton(
                              onPressed: () async {
                                final id = idController.text;
                                final password = passwordController.text;

                                if (id.isEmpty || password.isEmpty) {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    const SnackBar(
                                      content: Text('아이디 또는 비밀번호를 입력해주세요'),
                                    ),
                                  );
                                } else {
                                  ScaffoldMessenger.of(context)
                                      .hideCurrentSnackBar();

                                  //clearTextFields();

                                  if (_collectingTask?.inProgress ?? false) {
                                    await _collectingTask!.cancel();
                                    setState(() {
                                      /* Update for `_collectingTask.inProgress` */
                                      ScaffoldMessenger.of(context)
                                          .showSnackBar(
                                        const SnackBar(
                                          content: Text('블루투스 연결이 끊어짐'),
                                        ),
                                      );
                                    });
                                  } else {
                                    if (!mounted) return;
                                    final BluetoothDevice? selectedDevice =
                                        await Navigator.of(context).push(
                                      MaterialPageRoute(
                                        builder: (context) {
                                          return const SelectBondedDevicePage(
                                              checkAvailability: false);
                                        },
                                      ),
                                    );

                                    if (selectedDevice != null) {
                                      print(
                                          'Connect -> selected ${selectedDevice.address}');

                                      if (!mounted) return;

                                      await _startBackgroundTask(
                                          context, selectedDevice);
                                      setState(() {});
                                    }
                                  }
                                }
                              },
                              style: ElevatedButton.styleFrom(
                                minimumSize: const Size(40, 40),
                                backgroundColor: Colors.white,
                                shadowColor: Colors.black,
                                elevation: 3,
                              ),
                              child: const Row(
                                children: [
                                  Text(
                                    '시작하기',
                                    style: TextStyle(fontSize: 17),
                                  ),
                                  SizedBox(width: 8),
                                  Icon(Icons.login)
                                ],
                              ),
                            ),
                            ElevatedButton(
                              onPressed: () {
                                Navigator.of(context).pushNamed('/account');
                              },
                              style: ElevatedButton.styleFrom(
                                minimumSize: const Size(40, 40),
                                backgroundColor: Colors.white,
                                shadowColor: Colors.black,
                                elevation: 3,
                              ),
                              child: const Row(
                                children: [
                                  Text(
                                    '회원가입',
                                    style: TextStyle(fontSize: 17),
                                  ),
                                  SizedBox(width: 8),
                                  Icon(Icons.logout)
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _startBackgroundTask(
    BuildContext context,
    BluetoothDevice server,
  ) async {
    try {
      _collectingTask = await BackgroundCollectingTask.connect(server, context);
      if (!mounted) return;
      await _collectingTask!.start(context);
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('블루투스가 연결되었습니다.'),
        ),
      );
      Navigator.of(context).pushNamed('/drawer');
    } catch (ex) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('블루투스 연결에 실패했습니다.'),
        ),
      );
      _collectingTask?.cancel();
      if (!mounted) return;
      /* showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Error occured while connecting'),
            content: Text(ex.toString()),
            actions: <Widget>[
              TextButton(
                child: const Text("Close"),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        },
      ); */
    }
  }
}
