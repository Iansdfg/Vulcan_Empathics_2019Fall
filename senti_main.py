from CRUD_m import create_data
from CRUD_m import read_data
from CRUD_m import close_connection
from CRUD_m import get_connection
import csv

if __name__ == '__main__':

    file_name = 'CSV/intergrated_accurate.wav.csv'

    csvFile = open(file_name, "r")
    reader = csv.reader(csvFile)

    connection = get_connection()
    table_name = 'speech_sentiment'

    for row in reader:
        # print(row)
        sentence = ' ' 
        if len(row) == 8:
            sentence = row[7]

        datum = {
            'time': int(row[0]), 
            'video_id': row[1], 
            'score_val': float(row[2]), 
            'score_max': float(row[3]),
            'score_min': float(row[4]),
            'score_avg': float(row[5]),
            'score_std': float(row[6]),
            'sentence': sentence,
        }
        print(datum)

        create_data(table_name, datum, connection)



    