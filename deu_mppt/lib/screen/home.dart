import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';

import 'package:provider/provider.dart';
import 'package:fl_chart/fl_chart.dart';

import 'package:deu_mppt/shared/menu_top.dart';
import 'package:deu_mppt/provide/xvalue.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      backgroundColor: Color(0xFFF1F3F5),
      appBar: MenuTop(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(height: 8),
            BatteryTable(),
            SizedBox(height: 15),
            TotalOutputBar(),
            SizedBox(height: 15),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                DataTile(
                  height: 160,
                  width: 160,
                  node: 1,
                ),
                SizedBox(width: 10),
                DataTile(
                  height: 160,
                  width: 160,
                  node: 2,
                ),
              ],
            ),
            SizedBox(height: 10),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                DataTile(
                  height: 160,
                  width: 160,
                  node: 3,
                ),
                SizedBox(width: 10),
                DataTile(
                  height: 160,
                  width: 160,
                  node: 4,
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class DataTile extends StatelessWidget {
  const DataTile({
    required this.height,
    required this.width,
    required this.node,
    super.key,
  });

  final double height;
  final double width;
  final int node;

  IconData nodeIcon(node) {
    switch (node) {
      case 1:
        return Icons.filter_1_outlined;
      case 2:
        return Icons.filter_2_outlined;
      case 3:
        return Icons.filter_3_outlined;
      case 4:
        return Icons.filter_4_outlined;
      default:
        return Icons.filter_none_outlined;
    }
  }

  @override
  Widget build(BuildContext context) {
    final screenHight = MediaQuery.of(context).size;

    return Container(
      padding: const EdgeInsets.all(10),
      height: height,
      //width: width,
      width: screenHight.width * 0.92 / 2,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.4),
            blurRadius: 5.0,
            spreadRadius: 0.0,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Icon(nodeIcon(node)),
              /* Text(
                node,
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                ),
              ), */
              const Icon(Icons.bolt_sharp),
            ],
          ),
          const Divider(height: 10),
          const SizedBox(height: 10),
          const Text(
            "100 kW",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
          const SizedBox(height: 5),
          const Text(
            "120 V",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
          const SizedBox(height: 5),
          const Text(
            "16 A",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
        ],
      ),
    );
  }
}

class TotalOutputBar extends StatelessWidget {
  const TotalOutputBar({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    final screenHight = MediaQuery.of(context).size;

    return Container(
      padding: const EdgeInsets.all(10),
      height: 50,
      //width: 340,
      //height: screenHight.height * screenHight.aspectRatio * 0.14,
      width: screenHight.width * 0.93,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.4),
            blurRadius: 5.0,
            spreadRadius: 0.0,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: const Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Text(
            "Total",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          VerticalDivider(width: 10),
          Text(
            "120 kW",
            style: TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
          VerticalDivider(width: 10),
          Text(
            "220 V",
            style: TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
          VerticalDivider(width: 10),
          Text(
            "16 A",
            style: TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}

class BatteryTable extends StatefulWidget {
  const BatteryTable({
    super.key,
  });

  @override
  State<BatteryTable> createState() => _BatteryTableState();
}

class _BatteryTableState extends State<BatteryTable> {
  double value = 75.0;

  @override
  Widget build(BuildContext context) {
    final screenHight = MediaQuery.of(context).size;

    return Container(
      padding: const EdgeInsets.all(10),
      height: screenHight.width >= 200 ? 275 : screenHight.height * 0.28,
      width: screenHight.width * 0.93,
      /* height: 233,
      width: 340, */
      decoration: BoxDecoration(
        color: Colors.white,
        //color: const Color(0xFF8BD2FC),
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
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
            flex: 8,
            child: Column(
              children: [
                const SizedBox(height: 10),
                /* Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    if (value < 16)
                      const Icon(
                        Icons.battery_alert_rounded,
                        size: 25,
                        color: Colors.red,
                      ),
                    const Icon(
                      Icons.battery_charging_full_rounded,
                      size: 25,
                      color: Colors.green,
                    ),
                  ],
                ), */
                Container(
                  //height: 188,
                  //width: 220,
                  height:
                      screenHight.width >= 200 ? 230 : screenHight.height * 0.2,
                  //height: screenHight.height * 0.2,
                  width: screenHight.width * 0.67,
                  decoration: const BoxDecoration(color: Colors.white),
                  child: const LineChartSample10(),
                  //child: CircularGraph(value: value),
                ),
                /* Slider(
                  value: value,
                  min: 0,
                  max: 100,
                  activeColor: Colors.blue,
                  onChanged: (newValue) {
                    setState(() {
                      value = newValue;
                    });
                  },
                ), */
              ],
            ),
          ),
          const Expanded(
            flex: 1,
            child: VerticalDivider(
              width: 10,
            ),
          ),
          const Expanded(
            flex: 2,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "한전",
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                SizedBox(
                  height: 15,
                ),
                Text(
                  "태양광",
                  style: TextStyle(color: Colors.grey),
                ),
                SizedBox(
                  height: 15,
                ),
                Text(
                  "발전기",
                  style: TextStyle(color: Colors.grey),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class CircularGraph extends StatefulWidget {
  final double value;

  const CircularGraph({
    Key? key,
    required this.value,
  }) : super(key: key);
  @override
  State<CircularGraph> createState() => _CircularGraphState();
}

class _CircularGraphState extends State<CircularGraph> {
  Color getColor(value) {
    if (value < 16) {
      return Colors.red;
    } else if (value <= 31) {
      return Colors.orange.withOpacity(0.8);
    } else {
      return Colors.green.withOpacity(0.8);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            spreadRadius: 2,
            blurRadius: 9,
            offset: const Offset(0, 0),
          ),
        ],
      ),
      child: ClipOval(
        child: Container(
          decoration: const BoxDecoration(
            color: Colors.white,
            shape: BoxShape.circle,
          ),
          child: Column(
            children: <Widget>[
              Stack(
                alignment: Alignment.center,
                children: [
                  SizedBox(
                    width: 140,
                    height: 140,
                    child: PieChart(
                      PieChartData(
                        sectionsSpace: 0,
                        centerSpaceRadius: 55,
                        sections: [
                          PieChartSectionData(
                            showTitle: false,
                            color: getColor(widget.value),
                            //color: Colors.green.withOpacity(0.8),
                            value: widget.value,
                            radius: 15,
                          ),
                          PieChartSectionData(
                            showTitle: false,
                            color: Colors.grey.withOpacity(0.3),
                            value: 100 - widget.value,
                            radius: 15,
                          ),
                        ],
                      ),
                    ),
                  ),
                  Text(
                    '${widget.value.toInt()}%', // Your text here
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.black, // Customize text color
                    ),
                  )
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}

class LineChartSample10 extends StatefulWidget {
  const LineChartSample10({Key? key}) : super(key: key);

  @override
  State<LineChartSample10> createState() => _LineChartSample10State();
}

class _LineChartSample10State extends State<LineChartSample10> {
  final limitCount = 200;
  final sinPoints = <FlSpot>[];
  final cosPoints = <FlSpot>[];

  double xValue = 0;
  double step = 0.05;

  late Timer timer;

  @override
  void initState() {
    super.initState();
    final xValueProvider = Provider.of<XValueProvider>(context, listen: false);

    timer = Timer.periodic(const Duration(milliseconds: 40), (timer) {
      while (sinPoints.length > limitCount) {
        sinPoints.removeAt(0);
        cosPoints.removeAt(0);
      }

      // Get the xValue from the provider
      xValue = xValueProvider.xValue;

      setState(() {
        // Add data points based on xValue received from the provider
        sinPoints.add(FlSpot(xValue, sin(xValue)));
        cosPoints.add(FlSpot(xValue, cos(xValue)));
        //sinPoints.add(FlSpot(xValue, 0.8));
        //cosPoints.add(FlSpot(xValue, 0.4));
      });

      xValue += step;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Consumer<XValueProvider>(
      builder: (context, xValueProvider, child) {
        // Access xValue from the provider
        xValue = xValueProvider.xValue;

        return cosPoints.isNotEmpty
            ? AspectRatio(
                aspectRatio: 1.5,
                child: LineChart(
                  LineChartData(
                      minY: -1,
                      maxY: 1,
                      minX: sinPoints.first.x,
                      maxX: sinPoints.last.x,
                      lineTouchData: const LineTouchData(enabled: true),
                      clipData: const FlClipData.all(),
                      gridData: const FlGridData(
                        show: true,
                        drawVerticalLine: true,
                      ),
                      borderData: FlBorderData(show: true),
                      lineBarsData: [
                        sinLine(sinPoints),
                        cosLine(cosPoints),
                      ],
                      titlesData: const FlTitlesData(
                        show: true,
                        topTitles: AxisTitles(
                          sideTitles: SideTitles(reservedSize: 0),
                        ),
                        rightTitles: AxisTitles(
                          sideTitles: SideTitles(reservedSize: 0),
                        ),
                        leftTitles: AxisTitles(
                          sideTitles: SideTitles(reservedSize: 0),
                        ),
                      )
                      /* titlesData: const FlTitlesData(
                      show: true,
                    ), */
                      ),
                ),
              )
            : Container();
      },
    );
  }

  LineChartBarData sinLine(List<FlSpot> points) {
    return LineChartBarData(
      spots: points,
      dotData: const FlDotData(
        show: false,
      ),
      gradient: const LinearGradient(
        colors: [Colors.black, Colors.red],
        stops: [0.1, 1.0],
      ),
      barWidth: 4,
      isCurved: false,
    );
  }

  LineChartBarData cosLine(List<FlSpot> points) {
    return LineChartBarData(
      spots: points,
      dotData: const FlDotData(
        show: false,
      ),
      gradient: const LinearGradient(
        colors: [Colors.black, Colors.black],
        stops: [0.1, 1.0],
      ),
      barWidth: 4,
      isCurved: false,
    );
  }

  @override
  void dispose() {
    timer.cancel();
    super.dispose();
  }
}
