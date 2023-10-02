import 'package:flutter/material.dart';

import 'package:deu_mppt/shared/menu_top.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;

    return Scaffold(
      appBar: const MenuTop(),
      backgroundColor: const Color(0xFFF1F3F5),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(10.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Padding(
                padding: EdgeInsets.only(left: 10),
                child: Text(
                  "회원정보",
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 10),
              Container(
                padding: const EdgeInsets.all(10),
                height: 230,
                width: screenSize.width,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(18),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.4),
                      blurRadius: 5.0,
                      spreadRadius: 0.0,
                      offset: const Offset(0, 3),
                    )
                  ],
                ),
                child: const Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.circle_rounded,
                        size: 130,
                      ),
                      SizedBox(height: 15),
                      Text(
                        "User Name",
                        style: TextStyle(fontSize: 18),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: const Padding(
                      padding: EdgeInsets.all(10.0),
                      child: Row(
                        children: [
                          Icon(Icons.add_alert_outlined),
                          SizedBox(width: 10),
                          Text("누적경고 (1)"),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 20),
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: const Padding(
                      padding: EdgeInsets.all(10.0),
                      child: Row(
                        children: [
                          Icon(Icons.error_outline_outlined, color: Colors.red),
                          SizedBox(width: 10),
                          Text("경고 사항 (1)"),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(10),
                    color: Colors.white,
                  ),
                  child: Column(
                    children: [
                      const Padding(
                        padding: EdgeInsets.all(8.0),
                        child: Row(
                          children: [
                            Icon(Icons.arrow_circle_right_outlined, size: 25),
                            SizedBox(width: 20),
                            Text(
                              "아이디: User ID",
                              style: TextStyle(fontSize: 17),
                            ),
                          ],
                        ),
                      ),
                      Divider(
                        height: 20,
                        color: Colors.blue[400],
                      ),
                      const Padding(
                        padding: EdgeInsets.all(8.0),
                        child: Row(
                          children: [
                            Icon(Icons.arrow_circle_right_outlined, size: 25),
                            SizedBox(width: 20),
                            Text(
                              "비밀번호 변경하기",
                              style: TextStyle(fontSize: 17),
                            ),
                          ],
                        ),
                      ),
                      Divider(
                        height: 20,
                        color: Colors.blue[400],
                      ),
                      const Padding(
                        padding: EdgeInsets.all(8.0),
                        child: Row(
                          children: [
                            Icon(Icons.arrow_circle_right_outlined, size: 25),
                            SizedBox(width: 20),
                            Text(
                              "버전 정보 : 0.0.1",
                              style: TextStyle(fontSize: 17),
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
}
