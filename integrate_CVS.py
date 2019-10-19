import csv
import os 

def read_sigle_file(file_name, id_num, intergrated_list):
    folder_name = './CSV/'
    path_name = folder_name + file_name
    csvFile = open(path_name, "r")
    reader = csv.reader(csvFile)

    reader_list = list(reader)[1:]
    max_time = int(reader_list[-1][0])

    curr_reader_pos = 0
    curr_data = ['0.0']*7
    for count in range(1,max_time):
        if int(reader_list[curr_reader_pos][0]) == count:
            intergrated_list.append([count] + [id_num] + reader_list[curr_reader_pos][2:])
            curr_reader_pos += 1
            curr_data = reader_list[curr_reader_pos]
        else:
            intergrated_list.append([count] + [id_num] + curr_data[2:])

    intergrated_list.append(reader_list[-1])
    csvFile.close()

def write_file(large_list):
    csvFile = open("CSV/intergrated.wav.csv", "w")
    writer = csv.writer(csvFile)
    for listt in large_list:
        writer.writerow(listt)

            

if __name__ == "__main__":
    intergrated_list = []
    # file_name = "001_S_T.wav.csv"
    # id_num = file_name[:3]
    # read_sigle_file(file_name, id_num, intergrated_list)

    lists = os.listdir('CSV/')
    for item in lists:
        if '0' <= item[0] <= '9':
            id_num = item[:3]
            read_sigle_file(item, id_num, intergrated_list)

    write_file(intergrated_list)
    for item in intergrated_list:
        print(item)





