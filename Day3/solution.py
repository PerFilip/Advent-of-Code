import csv

def solve_1():
    """
    Data was first cleaned with replace for csv
    """

    with open('test.csv') as csv_data:
        overlapping = 0
        reader = csv.reader(csv_data)
        fabric = [[0]*10]*10 # 10000 * 10000 matrix
        for row in reader:
            i = int(row[1])
            j = int(row[2])
            n = int(row[3])
            m = int(row[4])
            for x in range(m):
                for y in range(n):
                    a = x + j
                    b = y + n
                    fabric[a][b] += 1
                    print(fabric[a][b])

        for n in range(10):
            print(fabric[n])
        for i in range(10):
            for j in range(10):
                if fabric[i][j] >= 2:
                    overlapping += 1
        return overlapping
