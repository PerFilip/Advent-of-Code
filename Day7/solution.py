import csv

def solve_1():
    data = to_list('data.csv')
    
    while True:


def to_list(filename):
    data_list = []
    with open(filename) as data:
        reader = csv.reader(data)
        for row in reader:
            data_list.append([row[1], row[3]])
    return data_list

def solve_2():
    return 0