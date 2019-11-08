# Vulcan_Empathics_2019Fall


<!-- tmp_speech2text.py: 
conver all audio into CSV files eg: 001_S_T.wav.csv 

integrate_CVS.py: 
integrate all csv from tmp_speech2text.py to "CSV/intergrated.wav.csv"
-change format base on database (increment by every second)
-padding 0.5 into sentiment
-copy the last data if there is no data at this point

static_functions.py: 
read "CSV/intergrated.wav.csv" and write "CSV/intergrated_accurate.wav.csv". 
"CSV/intergrated_accurate.wav.csv" has right mean, std, max, min

senti_main.py:
upload file "CSV/intergrated_accurate.wav.csv" to database -->


step 1: <br/>
put all .wav file into "audio" folder <br/>
<br/>

step 2:<br/>
run 'tmp_speech2text.py', get .csv files in CSV folder<br/>
input: audio/<>.wav output CSV/<>.csv <br/>
<br/>

step 3:<br/>
run 'integrate_CVS.py', get one 'intergrated.wav.csv' file<br/>
input: CSV/<>.csv  output:  CSV/intergrated.wav.csv <br/>
<br/>

step 4:<br/>
run 'static_functions.py', get one 'intergrated_accurate.wav.csv' file<br/>
input: CSV/intergrated.wav.csv  output:  CSV/intergrated_accurate.wav.csv <br/>
<br/>

step 5:<br/>
run 'senti_main.py', upload to database<br/>
input: CSV/intergrated_accurate.wav.csv  output: to database <br/>