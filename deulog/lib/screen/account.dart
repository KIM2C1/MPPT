import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';

class CreateAccountScreen extends StatefulWidget {
  const CreateAccountScreen({super.key});

  @override
  State<CreateAccountScreen> createState() => _CreateAccountScreenState();
}

class _CreateAccountScreenState extends State<CreateAccountScreen> {
  final TextEditingController idController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController repasswordController = TextEditingController();

  final _password = FocusNode();
  final _repassword = FocusNode();

  bool isPasswordVisible = true;

  void togglePasswordVisibility() {
    setState(() {
      isPasswordVisible = !isPasswordVisible;
    });
  }

  void _showSnackbar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        duration: const Duration(seconds: 2), // Adjust the duration as needed
      ),
    );
  }

  @override
  void dispose() {
    _password.dispose();
    _repassword.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          children: [
            const Expanded(
              flex: 1,
              child: Row(
                children: [
                  Text(
                    "회원가입",
                    style: TextStyle(fontSize: 38),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 1,
              child: Column(
                children: [
                  Flexible(
                    child: TextFormField(
                      controller: idController,
                      enableSuggestions: false,
                      autocorrect: false,
                      autofocus: true,
                      decoration: const InputDecoration(
                        labelText: '아이디를 입력해주세요. (홍길동@홍길동.com)',
                      ),
                      textInputAction: TextInputAction.next,
                      onFieldSubmitted: (_) {
                        FocusScope.of(context).requestFocus(_password);
                      },
                    ),
                  ),
                  const SizedBox(height: 15),
                  Flexible(
                    child: TextFormField(
                      controller: passwordController,
                      enableSuggestions: false,
                      autocorrect: false,
                      obscureText: isPasswordVisible,
                      focusNode: _password,
                      decoration: const InputDecoration(
                        labelText: '비밀번호를 입력해주세요.',
                      ),
                      textInputAction: TextInputAction.next,
                      onFieldSubmitted: (_) {
                        FocusScope.of(context).requestFocus(_repassword);
                      },
                    ),
                  ),
                  const SizedBox(height: 15),
                  Flexible(
                    child: TextFormField(
                      controller: repasswordController,
                      enableSuggestions: false,
                      autocorrect: false,
                      obscureText: isPasswordVisible,
                      focusNode: _repassword,
                      decoration: InputDecoration(
                        labelText: '비밀번호를 확인해주세요.',
                        suffixIcon: GestureDetector(
                          behavior: HitTestBehavior.translucent,
                          onTap: togglePasswordVisibility,
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
                      ),
                      textInputAction: TextInputAction.done,
                      onFieldSubmitted: (_) {
                        setState(() {});
                      },
                    ),
                  ),
                ],
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                    onPressed: () async {
                      final password = passwordController.text;
                      final repassword = repasswordController.text;
                      final id = idController.text;

                      if (password.isNotEmpty &&
                          repassword.isNotEmpty &&
                          id.isNotEmpty) {
                        if (passwordController.text ==
                            repasswordController.text) {
                          try {
                            await FirebaseAuth.instance
                                .createUserWithEmailAndPassword(
                              email: idController.text.toLowerCase().trim(),
                              password: passwordController.text.trim(),
                            );
                            if (!mounted) return;
                            _showSnackbar("가입 성공! 로그인해주세요");
                            Navigator.of(context).pop();
                          } on FirebaseAuthException catch (e) {
                            if (e.code == 'weak-password') {
                              _showSnackbar("비밀번호가 너무 짧습니다! 6자 이상");
                              passwordController.clear();
                              repasswordController.clear();
                            } else if (e.code == 'email-already-in-use') {
                              _showSnackbar("이미 존재하는 이메일입니다");
                              idController.clear();
                            }
                          }
                        } else {
                          _showSnackbar("비밀번호를 다시 확인 해주세요");
                        }
                      } else {
                        _showSnackbar("아이디 또는 비밀번호를 입력해주세요");
                      }
                    },
                    child: const Text("회원가입")),
                /* ElevatedButton(
                    onPressed: () {
                      Navigator.of(context).pushNamed('/drawer');
                    },
                    child: const Text("TEST")), */
              ],
            ),
          ],
        ),
      ),
    );
  }
}
