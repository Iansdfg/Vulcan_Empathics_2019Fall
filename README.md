# Vulcan_Empathics_2019Fall


<!-- tmp_speech2text.py: 
conver all audio into CSV files eg: 001_S_T.wav.csv  -->

<!-- integrate_CVS.py: 
integrate all csv from tmp_speech2text.py to "CSV/intergrated.wav.csv"
-change format base on database (increment by every second)
-padding 0.5 into sentiment
-copy the last data if there is no data at this point -->

<!-- static_functions.py: 
read "CSV/intergrated.wav.csv" and write "CSV/intergrated_accurate.wav.csv". 
"CSV/intergrated_accurate.wav.csv" has right mean, std, max, min -->

<!-- senti_main.py:
upload file "CSV/intergrated_accurate.wav.csv" to database -->