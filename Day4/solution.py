# falls or Guard
import csv
from datetime import datetime
import time


def solve_1():
    sleep_time = dict()
    with open('data.csv') as data:
        reader = csv.reader(data)
        cur_guard = " "
        fall_asleep_row = []
        sleeping = False
        for row in reader:
            if str(row[4]) == 'Guard':
                if sleeping:
                    print(fall_asleep_row[0:4])
                    sleep_time[cur_guard]+= minute_difference(fall_asleep_row[0:4], row[0:4])
                    sleeping = False
                cur_guard = str(row[5])
                if not (cur_guard in sleep_time):
                    sleep_time[cur_guard] = 0
                
            elif str(row[4]) == 'falls':
                if not sleeping:
                    fall_asleep_row = row
                    sleeping = True
            elif str(row[4]) == 'wakes':
                if sleeping:
                    sleep_time[cur_guard]+= minute_difference(fall_asleep_row[0:4], row[0:4])
                    sleeping = False
    return max(sleep_time)

def minute_difference(date1, date2):
    d1 = datetime(1518 , int(date1[0]), int(date1[1]), int(date1[2]), int(date1[3]))
    d2 = datetime(1518 , int(date2[0]), int(date2[1]), int(date2[2]), int(date2[3]))
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())
    return int(d2_ts-d1_ts) / 60

def solve_2():
    return 1