import 'package:deulog/provider/mppt_data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class ChartScreen extends StatelessWidget {
  const ChartScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final mpptData = Provider.of<MpptData>(context);

    final labels = [
      "grid_vol",
      "grid_freq",
      "ac_out_vol",
      "ac_out_freq",
      "ac_out_app_pow",
      "ac_out_act_pow",
      "out_load_percent",
      "bat_vol",
      "bat_charg_cur",
      "bat_discharg_cur",
      "bat_capacity",
      "pv_in_curr",
      "pv_in_vol",
      "pv_charge_power",
      "Raw voltage  [N1]",
      "Raw current",
      "Raw Frequency",
      "Raw power",
      "Raw Energy",
      "Raw pf",
      "Raw alarm value",
      "Node State",
      "Raw voltage  [N2]",
      "Raw current",
      "Raw Frequency",
      "Raw power",
      "Raw Energy",
      "Raw pf",
      "Raw alarm value",
      "Node State",
      "Raw voltage  [N3]",
      "Raw current",
      "Raw Frequency",
      "Raw power",
      "Raw Energy",
      "Raw pf",
      "Raw alarm value",
      "Node State",
      "Raw voltage  [N4]",
      "Raw current",
      "Raw Frequency",
      "Raw power",
      "Raw Energy",
      "Raw pf",
      "Raw alarm value",
      "Node State",
      "Output priority",
      "Charger priority",
    ];

    List<int> test = List<int>.filled(48, 1);

    List<DataRow> dataRows = [];

    for (int i = 0; i < 48; i++) {
      dataRows.add(buildDataRow(i, labels[i], mpptData.mppdata[i]));
    }

    return Scaffold(
      appBar: AppBar(
          automaticallyImplyLeading: false,
          title: const Center(child: Text("Mppt Data All"))),
      body: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Container(
              decoration: BoxDecoration(
                border: Border.all(),
              ),
              child: Column(
                children: [
                  TextButton(
                      //데이터 Test를 위한 버튼
                      onPressed: () {
                        test[46] = 51;
                        test[10] = 100;
                        test[15] = 5000;
                        test[17] = 110000;
                        test[19] = 1;
                        mpptData.saveMppt(test);
                      },
                      child: const Text("Set All 1")),
                  DataTable(
                    dividerThickness: 1.0,
                    columns: const [
                      DataColumn(label: Text('Index')),
                      DataColumn(label: Text('Parameter')),
                      DataColumn(label: Text('Value')),
                    ],
                    rows: dataRows,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

DataRow buildDataRow(int index, String parameter, int value) {
  return DataRow(
    cells: [
      DataCell(Text(index.toString())),
      DataCell(Text(parameter)),
      DataCell(Text(value.toString())),
    ],
  );
}
