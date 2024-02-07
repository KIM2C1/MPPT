import 'dart:async';
import 'package:intl/intl.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'package:percent_indicator/percent_indicator.dart';

import 'package:deulog/provider/mppt_data.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String formattedDate = '';
  Timer? _timer;

  List<String> imagePaths = [];
  List<String> imageText = [];

  @override
  void initState() {
    super.initState();

    // Initialize the Korean locale data
    initializeDateFormatting('ko_KR', null);

    // Start a timer to update the date and day of the week every second
    _timer = Timer.periodic(const Duration(milliseconds: 200), (Timer timer) {
      if (mounted) {
        setState(() {
          formattedDate = _getCurrentDateAndDayOfWeek();
        });
      }
    });
  }

  @override
  void dispose() {
    super.dispose();
    _timer?.cancel();
  }

  String _getCurrentDateAndDayOfWeek() {
    DateTime currentTime = DateTime.now();

    // Format the date with the Korean locale
    var dateFormat = DateFormat('yyyy-MM-dd EEEE', 'ko_KR');

    return dateFormat.format(currentTime);
  }

  List<String> _getImageData(priority) {
    switch (priority) {
      case 48: // Utility first
        imagePaths = [
          "images/generate_on.png",
          "images/solar_off.png",
          "images/battery_off.png",
        ];
        imageText = [
          "1. 한전",
          "2. 태양광",
          "3. 배터리",
        ];
        break;
      case 49: // Solar first
        imagePaths = [
          "images/solar_on.png",
          "images/generate_off.png",
          "images/battery_off.png",
        ];
        imageText = [
          "1. 태양광",
          "2. 한전",
          "3. 배터리",
        ];
        break;
      case 50: // Solar + Utility
        imagePaths = [
          "images/solar_on.png",
          "images/generate_on.png",
          "images/battery_off.png",
        ];
        imageText = [
          "1. 태양광",
          "+  한전",
          "2. 배터리",
        ];
        break;
      case 51: // Only solar
        imagePaths = [
          "images/solar_on.png",
          "images/generate_off.png",
          "images/battery_off.png",
        ];
        imageText = [
          "1. 태양광",
          "2. 한전",
          "3. 배터리",
        ];
        break;
      default: // Utility first
        imagePaths = [
          "images/generate_on.png",
          "images/solar_off.png",
          "images/battery_off.png",
        ];
        imageText = [
          "1. 한전",
          "2. 태양광",
          "3. 배터리",
        ];
    }
    return imagePaths;
  }

  @override
  Widget build(BuildContext context) {
    final screenHeight = MediaQuery.of(context).size.height;
    final screenWidth = MediaQuery.of(context).size.width;

    final mppdata = Provider.of<MpptData>(context);

    List<bool> powerState = mppdata.nodeState;

    double maxRatedPower = 1000.0; // 최대 정격 전력 (가정)

    double node1Load = ((mppdata.mppdata[17] / 1000) *
            (mppdata.mppdata[15] / 1000) *
            mppdata.mppdata[19]) /
        maxRatedPower;

    double node2Load = ((mppdata.mppdata[25] / 1000) *
            (mppdata.mppdata[23] / 1000) *
            mppdata.mppdata[27]) /
        maxRatedPower;

    double node3Load = ((mppdata.mppdata[33] / 1000) *
            (mppdata.mppdata[31] / 1000) *
            mppdata.mppdata[35]) /
        maxRatedPower;

    double node4Load = ((mppdata.mppdata[41] / 1000) *
            (mppdata.mppdata[39] / 1000) *
            mppdata.mppdata[43]) /
        maxRatedPower;

    Color getColorForBat(double load) {
      if (load >= 0.4) {
        return Colors.blue; // Red for load >= 0.7
      } else if (load >= 0.2) {
        return Colors.orange; // Orange for load between 0.4 and 0.7
      } else {
        return Colors.red; // Blue for load < 0.4
      }
    }

    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          children: [
            const SizedBox(height: 45),
            Expanded(
              flex: 1,
              child: Table(
                columnWidths: const {
                  0: FlexColumnWidth(6),
                  1: FlexColumnWidth(4),
                },
                border: const TableBorder(
                  top: BorderSide(
                    color: Color.fromARGB(69, 158, 158, 158),
                    width: 1.0,
                  ),
                  bottom: BorderSide(
                    color: Color.fromARGB(69, 158, 158, 158),
                    width: 1.0,
                  ),
                ),
                children: [
                  TableRow(
                    children: [
                      TableCell(
                        child: Container(
                          decoration: const BoxDecoration(
                            border: Border(
                              right: BorderSide(
                                color: Color.fromARGB(69, 158, 158, 158),
                                width: 1.0,
                              ),
                            ),
                          ),
                          child: Container(
                            alignment: Alignment.centerLeft,
                            height: 45,
                            color: const Color(0xFFF1F3F5),
                            child: Image.asset(
                              "images/AutoREX.png",
                              //height: 30,
                              width: screenHeight * 0.15,
                            ),
                          ),
                        ),
                      ),
                      TableCell(
                        // Add a border only to the left side
                        child: Container(
                          decoration: const BoxDecoration(
                            border: Border(
                              left: BorderSide(
                                color: Color.fromARGB(69, 158, 158, 158),
                                width: 1.0,
                              ),
                            ),
                          ),
                          child: Container(
                            alignment: Alignment.centerRight,
                            height: 45,
                            color: const Color(0xFFF1F3F5),
                            child: Text(
                              formattedDate,
                              style: const TextStyle(
                                color: Colors.black,
                                fontSize: 15,
                              ),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 4,
              child: Column(
                children: [
                  const Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        "충전 우선순위",
                        style: TextStyle(
                            fontSize: 15, fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                  Container(
                    width: screenWidth * 1,
                    height: screenHeight * 0.18,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(15),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.grey.withOpacity(0.4),
                          blurRadius: 5.0,
                          spreadRadius: 0.0,
                          offset: const Offset(0, 3),
                        ),
                      ],
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        ChargeInfo(
                          screenWidth: screenWidth,
                          imagePaths: _getImageData(mppdata.mppdata[46]),
                          imageText: imageText,
                          index: 0,
                        ),
                        ChargeInfo(
                          screenWidth: screenWidth,
                          imagePaths: imagePaths,
                          imageText: imageText,
                          index: 1,
                        ),
                        ChargeInfo(
                          screenWidth: screenWidth,
                          imagePaths: imagePaths,
                          imageText: imageText,
                          index: 2,
                        ),
                      ],
                    ),
                  )
                ],
              ),
            ),
            Expanded(
              flex: 2,
              child: Column(
                children: [
                  const Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      Text(
                        "배터리 잔량",
                        style: TextStyle(
                          fontSize: 15,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 7),
                  Container(
                    width: screenWidth * 1,
                    height: screenHeight * 0.05,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(15),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.grey.withOpacity(0.4),
                          blurRadius: 5.0,
                          spreadRadius: 0.0,
                          offset: const Offset(0, 3),
                        ),
                      ],
                    ),
                    child: LinearPercentIndicator(
                      width: screenWidth * 0.75,
                      animation: true,
                      animationDuration: 50,
                      lineHeight: 15.0,
                      percent: mppdata.mppdata[10] / 100,
                      trailing: Text(
                        "${mppdata.mppdata[10]} %",
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      progressColor: getColorForBat(mppdata.mppdata[10] / 100),
                      barRadius: const Radius.circular(15),
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 6,
              child: Column(
                children: [
                  const Row(
                    children: [
                      Text(
                        "노드 상태",
                        style: TextStyle(
                          fontSize: 15,
                          fontWeight: FontWeight.bold,
                        ),
                      )
                    ],
                  ),
                  const SizedBox(height: 7),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      NodeInfo(
                        screenWidth: screenWidth,
                        nodeNum: 0,
                        //nodePower: 100,
                        nodePower: mppdata.mppdata[17] / 1000,
                        nodeVoltage: mppdata.mppdata[14] / 10,
                        nodeCurrent: mppdata.mppdata[15] / 1000,
                        nodeLoad: node1Load,

                        isPowerOn: powerState[0],
                      ),
                      NodeInfo(
                        screenWidth: screenWidth,
                        nodeNum: 1,
                        nodePower: mppdata.mppdata[25] / 1000,
                        nodeVoltage: mppdata.mppdata[22] / 10,
                        nodeCurrent: mppdata.mppdata[23] / 1000,
                        nodeLoad: node2Load,
                        isPowerOn: powerState[1],
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      NodeInfo(
                        screenWidth: screenWidth,
                        nodeNum: 2,
                        nodePower: mppdata.mppdata[33] / 1000,
                        nodeVoltage: mppdata.mppdata[30] / 10,
                        nodeCurrent: mppdata.mppdata[31] / 1000,
                        nodeLoad: node3Load,
                        isPowerOn: powerState[2],
                      ),
                      NodeInfo(
                        screenWidth: screenWidth,
                        nodeNum: 3,
                        nodePower: mppdata.mppdata[41] / 1000,
                        nodeVoltage: mppdata.mppdata[38] / 10,
                        nodeCurrent: mppdata.mppdata[39] / 1000,
                        nodeLoad: node4Load,
                        isPowerOn: powerState[3],
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class ChargeInfo extends StatelessWidget {
  const ChargeInfo({
    super.key,
    required this.screenWidth,
    required this.imagePaths,
    required this.imageText,
    required this.index,
  });

  final double screenWidth;
  final List<String> imagePaths;
  final List<String> imageText;
  final int index;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 10, bottom: 10),
          child: Container(
            width: screenWidth * 0.24,
            height: screenWidth * 0.24,
            decoration: BoxDecoration(
              color: const Color(0xFFF1F3F5),
              borderRadius: BorderRadius.circular(100),
            ),
            child: Center(
              child: Image(
                image: AssetImage(imagePaths[index]),
                width: screenWidth * 0.18,
                height: screenWidth * 0.18,
              ),
            ),
          ),
        ),
        Text(
          imageText[index],
          style: const TextStyle(
            fontSize: 15,
            fontWeight: FontWeight.bold,
          ),
        ),
      ],
    );
  }
}

class NodeInfo extends StatefulWidget {
  const NodeInfo({
    super.key,
    required this.screenWidth,
    required this.nodeNum,
    required this.nodePower,
    required this.nodeVoltage,
    required this.nodeCurrent,
    required this.nodeLoad,
    required this.isPowerOn,
  });

  final double screenWidth;
  final int nodeNum;
  final double nodePower;
  final double nodeVoltage;
  final double nodeCurrent;
  final double nodeLoad;
  final bool isPowerOn;

  @override
  State<NodeInfo> createState() => _NodeInfoState();
}

class _NodeInfoState extends State<NodeInfo> {
  //bool isPowerOn = false;

  Color buttonColor = Colors.black;

  Icon nodeIcon(int value) {
    switch (value) {
      case 1:
        return const Icon(Icons.filter_2_sharp);
      case 2:
        return const Icon(Icons.filter_3_sharp);
      case 3:
        return const Icon(Icons.filter_4_sharp);
      default:
        return const Icon(Icons.filter_1_sharp);
    }
  }

  @override
  Widget build(BuildContext context) {
    bool isPowerOn = widget.isPowerOn;

    if (isPowerOn) {
      buttonColor = Colors.blue;
    } else {
      buttonColor = Colors.black;
    }

    void togglePower() {
      final powerState = Provider.of<MpptData>(context, listen: false);
      powerState.togglePower(widget.nodeNum);

      setState(() {
        isPowerOn = !isPowerOn;
        buttonColor = isPowerOn ? Colors.blue : Colors.black;
        print('${widget.nodeNum} Node Power is ${isPowerOn ? 'ON' : 'OFF'}');
        /* ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text(
              '${widget.nodeNum} Node Power is ${isPowerOn ? 'ON' : 'OFF'}'),
        )); */
      });
    }

    return Container(
      width: widget.screenWidth * 0.43,
      height: widget.screenWidth * 0.38,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(15),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.4),
            blurRadius: 5.0,
            spreadRadius: 0.0,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.only(top: 4, bottom: 4, left: 4),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Transform.translate(
              offset: const Offset(0, -8),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  nodeIcon(widget.nodeNum),
                  //SizedBox(width: widget.screenWidth * 0.08),
                  Padding(
                    padding: const EdgeInsets.only(right: 28),
                    child: Text(
                      "${(widget.nodeLoad * 100).toStringAsFixed(0)}%",
                      style: const TextStyle(fontWeight: FontWeight.bold),
                    ),
                  ),
                  //const Icon(Icons.electric_bolt_rounded),

                  IconButton(
                    onPressed: togglePower,
                    icon: const Icon(Icons.power_settings_new_rounded),
                    color: buttonColor,
                  ),
                ],
              ),
            ),
            Transform.translate(
                offset: const Offset(0, -15), child: const Divider(height: 1)),
            Transform.translate(
              offset: const Offset(0, -7),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        "${widget.nodePower} kW",
                        style: const TextStyle(
                          fontSize: 17,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        "${widget.nodeVoltage} V",
                        style: const TextStyle(
                          fontSize: 17,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        "${widget.nodeCurrent} A",
                        style: const TextStyle(
                          fontSize: 17,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                  VerticalProgressBar(
                    nodeLoad: widget
                        .nodeLoad, // Set the progress value between 0.0 and 1.0
                  ),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}

class VerticalProgressBar extends StatelessWidget {
  final double nodeLoad;

  const VerticalProgressBar({super.key, required this.nodeLoad});

  Color _getColorForLoad(double load) {
    if (load >= 0.7) {
      return Colors.red; // Red for load >= 0.7
    } else if (load >= 0.4) {
      return Colors.orange; // Orange for load between 0.4 and 0.7
    } else {
      return Colors.blue; // Blue for load < 0.4
    }
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Container(
              height: 78 * (1 - nodeLoad), // Remaining space
            ),
            Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: _getColorForLoad(nodeLoad),
              ),
              height: 78 * nodeLoad, // Adjust the height based on progress
              width: 20,
            ),
          ],
        ),
        Container(width: 14),
      ],
    );
  }
}
