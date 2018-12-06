import csv

def solve_1():

    """
    Data was first cleaned with replace for csv
    """

    inches = 0
    data = to_list('data.csv')
    fabric = [[0]*10000 for i in range(10000)]
    for entry in data:
        i = entry[0] + 1
        j = entry[1] + 1
        n = entry[2]
        m = entry[3]
        for x in range(n):
            for y in range(m):
                fabric[y + j][x + i] += 1
    for i in range(10000):
        for j in range(10000):
            if fabric[i][j] > 1:
                inches += 1
    return inches


def to_list(filename, mode=1):
    if mode==1:
        data_list = []
        with open(filename) as data:
            reader = csv.reader(data)
            for row in reader:
                data_list.append([int(row[1]), int(row[2]), int(row[3]), int(row[4])])
            return data_list
    elif mode==2:
        data_list = []
        with open(filename) as data:
            reader = csv.reader(data)
            for row in reader:
                data_list.append([row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])])
            return data_list

def solve_2():
    data = to_list('data.csv', 2)
    fabric = [[0]*10000 for i in range(10000)]
    for entry in data:
        i = entry[1] + 1
        j = entry[2] + 1
        n = entry[3]
        m = entry[4]
        for x in range(n):
            for y in range(m):
                fabric[y + j][x + i] += 1
    for row in data:
        overlap = False
        i = row[1] + 1
        j = row[2] + 1
        n = row[3]
        m = row[4]
        for x in range(n):
            for y in range(m):
                if fabric[y + j][x + i] != 1:
                    overlap = True
        if not overlap:
            return row[0]
