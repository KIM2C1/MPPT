import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

import 'package:provider/provider.dart';
import 'package:fl_chart/fl_chart.dart';

import 'package:deu_mppt/shared/menu_top.dart';
import 'package:deu_mppt/provide/xvalue.dart';

class ChartScreen extends StatelessWidget {
  const ChartScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF1F3F5),
      appBar: const MenuTop(),
      body: PageView(
        children: const <Widget>[
          Page1(),
          Page2(),
          Page3(),
          Page4(),
        ],
      ),
    );
  }
}

class Page1 extends StatelessWidget {
  const Page1({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        color: const Color(0xFFF1F3F5),
        child: const Padding(
          padding: EdgeInsets.all(8.0),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.looks_one_outlined,
                    size: 30,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_two_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_3_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_4_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                ],
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Grid_Vol>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Ac_Out_Vol>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Ac_Out_App_Pow>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Ac_Out_Act_Pow>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Out_Load_Percent>",
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class Page2 extends StatelessWidget {
  const Page2({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        color: const Color(0xFFF1F3F5),
        child: const Padding(
          padding: EdgeInsets.all(8.0),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.looks_one_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_two_outlined,
                    size: 30,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_3_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_4_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                ],
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Bat_Vol>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Bat_Carge_Cur>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Bat_Discharg_Cur>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Bat_Capacity>",
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class Page3 extends StatelessWidget {
  const Page3({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        color: const Color(0xFFF1F3F5),
        child: const Padding(
          padding: EdgeInsets.all(8.0),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.looks_one_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_two_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_3_outlined,
                    size: 30,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_4_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                ],
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Pv_In_Cur>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Pv_In_Vol>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Pv_Charge_Power>",
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class Page4 extends StatelessWidget {
  const Page4({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        color: const Color(0xFFF1F3F5),
        child: const Padding(
          padding: EdgeInsets.all(8.0),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.looks_one_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_two_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_3_outlined,
                    size: 20,
                    color: Colors.grey,
                  ),
                  SizedBox(width: 15),
                  Icon(
                    Icons.looks_4_outlined,
                    size: 30,
                  ),
                ],
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Raw_Vol>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Raw_Cur>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Raw_Power>",
              ),
              SizedBox(height: 10),
              GraphTile(
                tiltle: "<Raw_Engrgy>",
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class GraphTile extends StatelessWidget {
  const GraphTile({
    required this.tiltle,
    super.key,
  });

  final String tiltle;

  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;

    return Container(
      padding: const EdgeInsets.all(10),
      height: 265,
      //width: 340,
      width: screenSize.width * 0.9,
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
      child: Column(
        children: [
          Row(
            children: [
              Text(
                tiltle,
                style: const TextStyle(
                  //fontSize: 15,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          SizedBox(
            height: 200,
            width: screenSize.width * 0.8,
            child: const LineChartSample10(),
          ),
        ],
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
                      borderData: FlBorderData(show: false),
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
