import 'package:flutter/material.dart';
/* 
  0  : grid_vol          V
  1  : grid_freq         Hz
  2  : ac_out_vol        V
  3  : ac_out_freq       Hz  
  4  : ac_out_app_pow        유효전력
  5  : ac_out_act_pow        피상전력
  6  : out_load_percent 
  7  : bat_vol 
  8  : bat_charg_cur 
  9  : bat_discharg_cur 
  10 : bat_capacity 
  11 : pv_in_curr
  12 : pv_in_vol
  13 : pv_charge_power
  --------------Node1 Data--------------
  14 : Raw voltage       V
  15 : Raw current       A
  16 : Raw Frequency     Hz
  17 : Raw power         W
  18 : Raw Energy        Wh
  19 : Raw pf            역률
  20 : Raw alarm value
  21 : Node State
  --------------Node2 Data--------------
  22 : Raw voltage       V
  23 : Raw current       A
  24 : Raw Frequency     Hz
  25 : Raw power         W
  26 : Raw Energy        Wh
  27 : Raw pf            
  28 : Raw alarm value
  29 : Node State  
  --------------Node3 Data--------------
  30 : Raw voltage       V
  31 : Raw current       A
  32 : Raw Frequency     Hz
  33 : Raw power         W
  34 : Raw Energy        Wh
  35 : Raw pf            
  36 : Raw alarm value    
  37 : Node State          
  --------------Node4 Data--------------
  38 : Raw voltage       V
  39 : Raw current       A
  40 : Raw Frequency     Hz
  41 : Raw power         W
  42 : Raw Energy        Wh
  43 : Raw pf            
  44 : Raw alarm value  
  45 : Node State

  46 : Output source priority
   0 : Utility first
   1 : Solar first
   2 : SBU first
  
  47 : Charger source priority
   0 : Utility first
   1 : Solar first
   2 : Solar + Utility
   3 : Only solar
*/

class MpptData with ChangeNotifier {
  List<int> checkNode = [21, 29, 37, 45];

  int _loading = 4;
  List<int> _mppdata = List<int>.filled(48, 0);
  final List<bool> _nodeState = List<bool>.filled(4, false);

  int get loading => _loading;
  List<int> get mppdata => _mppdata;
  List<bool> get nodeState => _nodeState;

  void saveMppt(List<int> data) {
    _mppdata = data;

    for (int i = 0; i < 4; i++) {
      _nodeState[i] = data[checkNode[i]] == 1;
    }
    notifyListeners();
    //print('Received data: $data');
    //print('Saved data: $_mppdata');
  }

  void togglePower(int node) {
    switch (node) {
      case 0:
        _loading = 0;
      case 1:
        _loading = 1;
      case 2:
        _loading = 2;
      case 3:
        _loading = 3;
      default:
        _loading = 4;
    }
    notifyListeners();
  }
}
