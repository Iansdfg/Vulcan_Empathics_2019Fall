import csv
import os 

def get_video_lenth():
    name_to_time = dict()
    csvFile = open('video_len.csv' , "r")
    reader = csv.reader(csvFile)
    for row in reader:
        name_to_time[row[0][:3]] = row[1]

    return name_to_time

def read_sigle_file(file_name, id_num, intergrated_list):
    name_to_time = get_video_lenth()

    folder_name = './CSV/'
    path_name = folder_name + file_name
    csvFile = open(path_name, "r")
    reader = csv.reader(csvFile)

    reader_list = list(reader)[1:]
    max_time = int(name_to_time[id_num])
    # print(reader_list)

    curr_reader_pos = 0
    curr_data = ['0.0']*7
    for count in range(1, max_time+1):

        if curr_reader_pos < len(reader_list): 
            if int(reader_list[curr_reader_pos][0]) == count:
                intergrated_list.append([count] + [id_num] + reader_list[curr_reader_pos][2:])
                curr_reader_pos += 1
                if curr_reader_pos < len(reader_list):
                    curr_data = reader_list[curr_reader_pos]
            else:
                intergrated_list.append([count] + [id_num] + [0.5] + curr_data[3:])
        else: 
            new_last_data = curr_data[2:6] + ['0.0'] + [' '] 
            intergrated_list.append([count] + [id_num] + new_last_data)

    csvFile.close()

def save_data_into_arrary(array_name):
    lists = os.listdir('CSV/')
    for item in lists:
        if '0' <= item[0] <= '9':
            id_num = item[:3]
            read_sigle_file(item, id_num, array_name)


def write_file(large_list):
    csvFile = open("CSV/intergrated.wav.csv", "w")
    writer = csv.writer(csvFile)
    for listt in large_list:
        writer.writerow(listt)

if __name__ == "__main__":
    intergrated_list = []

    # single file
    # lists = os.listdir('CSV/')
    # for item in lists:
    #     if item == '001_S_T.wav.csv':
    #         id_num = item[:3]
    #         read_sigle_file(item, id_num, intergrated_list)


    save_data_into_arrary(intergrated_list)
    write_file(intergrated_list)
    for item in intergrated_list:
        print(item)




