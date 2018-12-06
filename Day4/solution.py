# falls or Guard
import csv
from datetime import datetime
import time


def solve_1():
    data_list = ordered_data_list('data.csv')
    sleep_times = dict()
    cur_guard = ''
    sleep_start_date = None
    for entry in data_list:
        if entry[1] == 'Guard':
            if entry[2]not in sleep_times:
                sleep_times[entry[2]] = 0
            cur_guard = entry[2]
        if entry[1] == 'falls':
            sleep_start_date = entry[0]
        if entry[1] == 'wakes':
            d1 = time.mktime(sleep_start_date.timetuple())
            d2 = time.mktime(entry[0].timetuple())
            sleep_times[cur_guard] += (d2 - d1)
    sleepy_guard = max(sleep_times)
    sleep_minutes = [0]*60
    for n in range(1000):
        if data_list[n][2] == sleepy_guard:
            sleep_minutes[data_list[n+1][0].minute:data_list[n+2][0].minute]




def ordered_data_list(filename):
    data_list = []
    with open(filename) as data:
        reader = csv.reader(data)
        for row in reader:
            d = datetime(1518, int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            entry = [d, str(row[4]), str(row[5])]
            data_list.append(entry)
    data_list.sort(key=lambda x: x[0])
    return data_list


def solve_2():
    return 1