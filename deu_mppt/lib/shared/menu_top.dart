import 'package:deu_mppt/provide/data.dart';
import 'package:flutter/material.dart';

import 'package:provider/provider.dart';

class MenuTop extends StatelessWidget implements PreferredSizeWidget {
  const MenuTop({super.key});

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      iconTheme: const IconThemeData(color: Colors.black),
      backgroundColor: const Color(0xFFF1F3F5),
      title: const Text(
        'DEU MPPT',
        style: TextStyle(
          color: Colors.black,
          fontSize: 20,
        ),
      ),
      elevation: 0.0,
      actions: [
        IconButton(
          icon: const Icon(Icons.bluetooth_connected_rounded, size: 20),
          onPressed: () {
            showDialog(
              context: context,
              builder: (BuildContext context) {
                return AlertDialog(
                  title: const Text('디바이스 정보'),
                  content: SingleChildScrollView(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Consumer<DeviceId>(
                            builder: (context, testProvide, child) {
                          final device = testProvide.device;
                          return Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text("연결된 디바이스: ${device?.localName ?? 'N/A'}"),
                                Text("RemotedId: ${device?.remoteId ?? 'N/A'}"),
                              ]);
                        }),
                      ],
                    ),
                  ),
                  actions: [
                    TextButton(
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                      child: const Text('OK'),
                    ),
                  ],
                );
              },
            );
          },
        ),
        const Popbutton()
      ],
    );
  }
}

class Popbutton extends StatelessWidget {
  const Popbutton({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    void handleMenuItemClick(String value, BuildContext context) {
      switch (value) {
        case '1':
          Navigator.of(context).pushNamed('/device2');
          break;
        case '2':
          Navigator.of(context).pushNamed('/setting');
          break;
      }
    }

    return PopupMenuButton<String>(
      onSelected: (value) => handleMenuItemClick(value, context),
      itemBuilder: (BuildContext context) {
        return [
          const PopupMenuItem<String>(
            value: '1',
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Text('Device'),
                SizedBox(width: 8),
                Icon(Icons.bluetooth_searching),
              ],
            ),
          ),
          const PopupMenuItem<String>(
            value: '2',
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Text('Setting'),
                SizedBox(width: 8),
                Icon(Icons.settings, size: 20),
              ],
            ),
          ),
        ];
      },
    );
  }
}
