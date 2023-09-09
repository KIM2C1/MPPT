import 'package:flutter/material.dart';

import 'package:provider/provider.dart';

import 'package:deu_mppt/shared/menu_top.dart';

import 'package:deu_mppt/provide/provider_ex.dart';
import 'package:deu_mppt/provide/result.dart';

class ChartScreen extends StatelessWidget {
  const ChartScreen({super.key});

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
                        "Chart Page",
                        style: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(deviceProvider.deviceStatus.name),
                      Text(deviceProvider.deviceStatus.connectionStatus),
                      Text(deviceProvider.deviceStatus.value.toString()),
                      ElevatedButton(
                        onPressed: () async {
                          deviceProvider.toggleAutoUpdate(
                              !deviceProvider.autoUpdateEnabled);
                        },
                        child: Text(deviceProvider.autoUpdateEnabled
                            ? 'Stop Update'
                            : 'Start Update'),
                      ),
                      const SizedBox(height: 10),
                      Consumer<ResultProvider>(
                        builder: (context, resultProvider, child) {
                          final resultProvider =
                              Provider.of<ResultProvider>(context);
                          return Center(
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                const Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      "Results",
                                      style: TextStyle(
                                        fontWeight: FontWeight.bold,
                                        fontSize: 18,
                                      ),
                                    )
                                  ],
                                ),
                                const SizedBox(height: 10),
                                SingleChildScrollView(
                                  scrollDirection: Axis.vertical,
                                  child: Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Container(
                                        height: 300,
                                        width: 300,
                                        decoration: const BoxDecoration(
                                            color: Colors.white),
                                        child: Text(
                                          resultProvider.result,
                                          style: const TextStyle(
                                            fontSize: 15,
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          );
                        },
                      )
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
