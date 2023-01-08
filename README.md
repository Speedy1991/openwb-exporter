# Docs coming soon
WIP

## Example Exporter Output

```bash
# HELP evu_APhase1 A an Phase 1 am Hausanschluss
# TYPE evu_APhase1 gauge
evu_APhase1{metric="evu",topic="openWB/evu/APhase1"} 0.0
# HELP evu_APhase2 A an Phase 2 am Hausanschluss
# TYPE evu_APhase2 gauge
evu_APhase2{metric="evu",topic="openWB/evu/APhase2"} 0.0
# HELP evu_APhase3 A an Phase 3 am Hausanschluss
# TYPE evu_APhase3 gauge
evu_APhase3{metric="evu",topic="openWB/evu/APhase3"} 0.0
# HELP evu_ASchieflast Schieflast in A am Hausübergabepunkt
# TYPE evu_ASchieflast gauge
evu_ASchieflast{metric="evu",topic="openWB/evu/ASchieflast"} 0.0
# HELP evu_DailyYieldExportKwh DailyYieldExportKwh
# TYPE evu_DailyYieldExportKwh gauge
evu_DailyYieldExportKwh{metric="evu",topic="openWB/evu/DailyYieldExportKwh"} 0.0
# HELP evu_DailyYieldImportKwh DailyYieldImportKwh
# TYPE evu_DailyYieldImportKwh gauge
evu_DailyYieldImportKwh{metric="evu",topic="openWB/evu/DailyYieldImportKwh"} 0.0
# HELP evu_Hz Herz
# TYPE evu_Hz gauge
evu_Hz{metric="evu",topic="openWB/evu/Hz"} 0.0
# HELP evu_PfPhase1 Power Factor an Phase 1
# TYPE evu_PfPhase1 gauge
evu_PfPhase1{metric="evu",topic="openWB/evu/PfPhase1"} 0.0
# HELP evu_PfPhase2 Power Factor an Phase 2
# TYPE evu_PfPhase2 gauge
evu_PfPhase2{metric="evu",topic="openWB/evu/PfPhase2"} 0.0
# HELP evu_PfPhase3 Power Factor an Phase 3
# TYPE evu_PfPhase3 gauge
evu_PfPhase3{metric="evu",topic="openWB/evu/PfPhase3"} 0.0
# HELP evu_VPhase1 Spannung in Volt an Phase 1
# TYPE evu_VPhase1 gauge
evu_VPhase1{metric="evu",topic="openWB/evu/VPhase1"} 0.0
# HELP evu_VPhase2 Spannung in Volt an Phase 2
# TYPE evu_VPhase2 gauge
evu_VPhase2{metric="evu",topic="openWB/evu/VPhase2"} 0.0
# HELP evu_VPhase3 Spannung in Volt an Phase 3
# TYPE evu_VPhase3 gauge
evu_VPhase3{metric="evu",topic="openWB/evu/VPhase3"} 0.0
# HELP evu_W Leistung am Hausübergabepunkt, Bezug ist positiv, Einspeisung negativ
# TYPE evu_W gauge
evu_W{metric="evu",topic="openWB/evu/W"} 0.0
# HELP evu_WAverage 
# TYPE evu_WAverage gauge
evu_WAverage{metric="evu",topic="openWB/evu/WAverage"} 0.0
# HELP evu_WPhase1 Leistung in Watt am Hausübergabepunkt an Phase 1
# TYPE evu_WPhase1 gauge
evu_WPhase1{metric="evu",topic="openWB/evu/WPhase1"} 0.0
# HELP evu_WPhase2 Leistung in Watt am Hausübergabepunkt an Phase 2
# TYPE evu_WPhase2 gauge
evu_WPhase2{metric="evu",topic="openWB/evu/WPhase2"} 0.0
# HELP evu_WPhase3 Leistung in Watt am Hausübergabepunkt an Phase 3
# TYPE evu_WPhase3 gauge
evu_WPhase3{metric="evu",topic="openWB/evu/WPhase3"} 0.0
# HELP evu_WhExported Eingespeiste Energie in Wh (Zählerstand)
# TYPE evu_WhExported gauge
evu_WhExported{metric="evu",topic="openWB/evu/WhExported"} 0.0
# HELP evu_WhImported Bezogene Energie in Wh (Zählerstand)
# TYPE evu_WhImported gauge
evu_WhImported{metric="evu",topic="openWB/evu/WhImported"} 0.0
# HELP global_DailyYieldAllChargePointsKwh 
# TYPE global_DailyYieldAllChargePointsKwh gauge
global_DailyYieldAllChargePointsKwh{metric="global",topic="openWB/global/DailyYieldAllChargePointsKwh"} 0.0
# HELP global_DailyYieldHausverbrauchKwh 
# TYPE global_DailyYieldHausverbrauchKwh gauge
global_DailyYieldHausverbrauchKwh{metric="global",topic="openWB/global/DailyYieldHausverbrauchKwh"} 0.0
# HELP global_WHouseConsumption Hausverbrauch (errechnet aus PV, EVU, EV, Speicher) in Watt
# TYPE global_WHouseConsumption gauge
global_WHouseConsumption{metric="global",topic="openWB/global/WHouseConsumption"} 0.0
# HELP global_kWhCounterAllChargePoints 
# TYPE global_kWhCounterAllChargePoints gauge
global_kWhCounterAllChargePoints{metric="global",topic="openWB/global/kWhCounterAllChargePoints"} 0.0
# HELP lp_1_APhase1 Stromstärke in Ampere an Phase 1 an LP1
# TYPE lp_1_APhase1 gauge
lp_1_APhase1{device_id="1",metric="lp",topic="openWB/lp/1/APhase1"} 0.0
# HELP lp_1_APhase2 Stromstärke in Ampere an Phase 2 an LP1
# TYPE lp_1_APhase2 gauge
lp_1_APhase2{device_id="1",metric="lp",topic="openWB/lp/1/APhase2"} 0.0
# HELP lp_1_APhase3 Stromstärke in Ampere an Phase 3 an LP1
# TYPE lp_1_APhase3 gauge
lp_1_APhase3{device_id="1",metric="lp",topic="openWB/lp/1/APhase3"} 0.0
# HELP lp_1_PfPhase1 PowerFactor an Phase 1 an LP1
# TYPE lp_1_PfPhase1 gauge
lp_1_PfPhase1{device_id="1",metric="lp",topic="openWB/lp/1/PfPhase1"} 0.0
# HELP lp_1_PfPhase2 PowerFactor an Phase 2 an LP1
# TYPE lp_1_PfPhase2 gauge
lp_1_PfPhase2{device_id="1",metric="lp",topic="openWB/lp/1/PfPhase2"} 0.0
# HELP lp_1_PfPhase3 PowerFactor an Phase 3 an LP1
# TYPE lp_1_PfPhase3 gauge
lp_1_PfPhase3{device_id="1",metric="lp",topic="openWB/lp/1/PfPhase3"} 0.0
# HELP lp_1_VPhase1 Spannung in Volt an Phase 1 an LP1
# TYPE lp_1_VPhase1 gauge
lp_1_VPhase1{device_id="1",metric="lp",topic="openWB/lp/1/VPhase1"} 0.0
# HELP lp_1_VPhase2 Spannung in Volt an Phase 2 an LP1
# TYPE lp_1_VPhase2 gauge
lp_1_VPhase2{device_id="1",metric="lp",topic="openWB/lp/1/VPhase2"} 0.0
# HELP lp_1_VPhase3 Spannung in Volt an Phase 3 an LP1
# TYPE lp_1_VPhase3 gauge
lp_1_VPhase3{device_id="1",metric="lp",topic="openWB/lp/1/VPhase3"} 0.0
# HELP lp_1_W Ladeleistung in Watt an LP1
# TYPE lp_1_W gauge
lp_1_W{device_id="1",metric="lp",topic="openWB/lp/1/W"} 0.0
# HELP lp_1_kWhActualCharged Geladene kWh des aktuellen Ladevorgangs an LP1
# TYPE lp_1_kWhActualCharged gauge
lp_1_kWhActualCharged{device_id="1",metric="lp",topic="openWB/lp/1/kWhActualCharged"} 0.0
# HELP lp_1_kWhChargedSincePlugged Geladene kWh seit letztem anstecken an LP1
# TYPE lp_1_kWhChargedSincePlugged gauge
lp_1_kWhChargedSincePlugged{device_id="1",metric="lp",topic="openWB/lp/1/kWhChargedSincePlugged"} 0.0
# HELP lp_1_kWhCounter Zählerstand in Wh an LP1
# TYPE lp_1_kWhCounter gauge
lp_1_kWhCounter{device_id="1",metric="lp",topic="openWB/lp/1/kWhCounter"} 0.0
# HELP lp_1_kWhDailyCharged Heute geladene kWh an LP1
# TYPE lp_1_kWhDailyCharged gauge
lp_1_kWhDailyCharged{device_id="1",metric="lp",topic="openWB/lp/1/kWhDailyCharged"} 0.0
# HELP lp_1_kmCharged 
# TYPE lp_1_kmCharged gauge
lp_1_kmCharged{device_id="1",metric="lp",topic="openWB/lp/1/kmCharged"} 0.0
# HELP lp_1_plugStartkWh 
# TYPE lp_1_plugStartkWh gauge
lp_1_plugStartkWh{device_id="1",metric="lp",topic="openWB/lp/1/plugStartkWh"} 0.0
# HELP lp_2_APhase1 Stromstärke in Ampere an Phase 1 an LP2
# TYPE lp_2_APhase1 gauge
lp_2_APhase1{device_id="2",metric="lp",topic="openWB/lp/2/APhase1"} 0.0
# HELP lp_2_APhase2 Stromstärke in Ampere an Phase 2 an LP2
# TYPE lp_2_APhase2 gauge
lp_2_APhase2{device_id="2",metric="lp",topic="openWB/lp/2/APhase2"} 0.0
# HELP lp_2_APhase3 Stromstärke in Ampere an Phase 3 an LP2
# TYPE lp_2_APhase3 gauge
lp_2_APhase3{device_id="2",metric="lp",topic="openWB/lp/2/APhase3"} 0.0
# HELP lp_2_PfPhase1 PowerFactor an Phase 1 an LP2
# TYPE lp_2_PfPhase1 gauge
lp_2_PfPhase1{device_id="2",metric="lp",topic="openWB/lp/2/PfPhase1"} 0.0
# HELP lp_2_PfPhase2 PowerFactor an Phase 2 an LP2
# TYPE lp_2_PfPhase2 gauge
lp_2_PfPhase2{device_id="2",metric="lp",topic="openWB/lp/2/PfPhase2"} 0.0
# HELP lp_2_PfPhase3 PowerFactor an Phase 3 an LP2
# TYPE lp_2_PfPhase3 gauge
lp_2_PfPhase3{device_id="2",metric="lp",topic="openWB/lp/2/PfPhase3"} 0.0
# HELP lp_2_VPhase1 Spannung in Volt an Phase 1 an LP2
# TYPE lp_2_VPhase1 gauge
lp_2_VPhase1{device_id="2",metric="lp",topic="openWB/lp/2/VPhase1"} 0.0
# HELP lp_2_VPhase2 Spannung in Volt an Phase 2 an LP2
# TYPE lp_2_VPhase2 gauge
lp_2_VPhase2{device_id="2",metric="lp",topic="openWB/lp/2/VPhase2"} 0.0
# HELP lp_2_VPhase3 Spannung in Volt an Phase 3 an LP2
# TYPE lp_2_VPhase3 gauge
lp_2_VPhase3{device_id="2",metric="lp",topic="openWB/lp/2/VPhase3"} 0.0
# HELP lp_2_W Ladeleistung in Watt an LP2 an LP2
# TYPE lp_2_W gauge
lp_2_W{device_id="2",metric="lp",topic="openWB/lp/2/W"} 0.0
# HELP lp_2_kWhActualCharged Geladene kWh des aktuellen Ladevorgangs an LP2
# TYPE lp_2_kWhActualCharged gauge
lp_2_kWhActualCharged{device_id="2",metric="lp",topic="openWB/lp/2/kWhActualCharged"} 0.0
# HELP lp_2_kWhChargedSincePlugged Geladene kWh seit letztem anstecken an LP2
# TYPE lp_2_kWhChargedSincePlugged gauge
lp_2_kWhChargedSincePlugged{device_id="2",metric="lp",topic="openWB/lp/2/kWhChargedSincePlugged"} 0.0
# HELP lp_2_kWhCounter Zählerstand in Wh an LP2
# TYPE lp_2_kWhCounter gauge
lp_2_kWhCounter{device_id="2",metric="lp",topic="openWB/lp/2/kWhCounter"} 0.0
# HELP lp_2_kWhDailyCharged Heute geladene kWh an LP2
# TYPE lp_2_kWhDailyCharged gauge
lp_2_kWhDailyCharged{device_id="2",metric="lp",topic="openWB/lp/2/kWhDailyCharged"} 0.0
# HELP lp_2_kmCharged 
# TYPE lp_2_kmCharged gauge
lp_2_kmCharged{device_id="2",metric="lp",topic="openWB/lp/2/kmCharged"} 0.0
# HELP lp_2_plugStartkWh 
# TYPE lp_2_plugStartkWh gauge
lp_2_plugStartkWh{device_id="2",metric="lp",topic="openWB/lp/2/plugStartkWh"} 0.0
# HELP pv_DailyYieldKwh 
# TYPE pv_DailyYieldKwh gauge
pv_DailyYieldKwh{metric="pv",topic="openWB/pv/DailyYieldKwh"} 0.0
# HELP pv_MonthlyYieldKwh 
# TYPE pv_MonthlyYieldKwh gauge
pv_MonthlyYieldKwh{metric="pv",topic="openWB/pv/MonthlyYieldKwh"} 0.0
# HELP pv_W PV Leistung in Watt, Erzeugung ist negativ
# TYPE pv_W gauge
pv_W{metric="pv",topic="openWB/pv/W"} 0.0
# HELP pv_WhCounter Zählsterstand in Wh PV erzeugte Energie
# TYPE pv_WhCounter gauge
pv_WhCounter{metric="pv",topic="openWB/pv/WhCounter"} 0.0
# HELP pv_YearlyYieldKwh 
# TYPE pv_YearlyYieldKwh gauge
pv_YearlyYieldKwh{metric="pv",topic="openWB/pv/YearlyYieldKwh"} 0.0
```