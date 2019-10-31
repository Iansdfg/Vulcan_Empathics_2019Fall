import csv
import os 
from statistics import stdev, mean

def cvs_to_dict():
    intergrated_file = open("CSV/intergrated.wav.csv", "r")
    reader = csv.reader(intergrated_file)

    id_to_row = dict()
    keys = []
    for row in reader:
        key = row[1]
        # print(key, row)
        if key not in id_to_row:
            id_to_row[key] = [row]
            keys.append(key)
        else:
            id_to_row[key].append(row)
    return id_to_row, keys

def save_one_file_to_cvs(key):
    res = []
    senti = [ ]
    count = 1
    for row in id_to_row[key]:
        senti.append(float(row[2]))
        if len(senti) < 2:
            stand_div = 0.0
        else:
            stand_div = stdev(senti)
        res.append(row[:3] + [max(senti)] + [min(senti)] + [mean(senti)] + [stand_div] + row[-1:])
        count += 1
    return res 


if __name__ == "__main__":
    id_to_row, keys = cvs_to_dict()
    final = []
    for key in keys:
        final += save_one_file_to_cvs(key)

    csvFile = open("CSV/intergrated_accurate.wav.csv", "w")
    writer = csv.writer(csvFile)
    for ele in final:
        writer.writerow(ele)



