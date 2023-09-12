import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:deu_mppt/shared/menu_top.dart';
import 'package:deu_mppt/provide/provider_ex.dart';

class SettingScreen extends StatelessWidget {
  const SettingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const MenuTop(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Consumer<DeviceProvider>(
              builder: (context, deviceProvider, child) {
                return Center(
                  child: Column(
                    children: [
                      const Text(
                        "Setting Page",
                        style: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(deviceProvider.deviceStatus.name),
                      Text(deviceProvider.deviceStatus.connectionStatus),
                      Text(deviceProvider.deviceStatus.value.toString()),
                      ElevatedButton(
                        onPressed: () {
                          deviceProvider.toggleAutoUpdate(
                              !deviceProvider.autoUpdateEnabled);
                        },
                        child: Text(deviceProvider.autoUpdateEnabled
                            ? 'Stop Update'
                            : 'Start Update'),
                      ),
                    ],
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
