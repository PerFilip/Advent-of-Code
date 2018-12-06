import csv

def calculate(mode=1):

    """
    Function solving the Day 1 problems.
    mode = 1 solves the first of the problems, 
    while mode = 2 solves the second problem.
    """
    
    if(mode==1):
        with open('data.csv') as csv_data:
            total = 0
            reader = csv.reader(csv_data)
            for row in reader:
                total += int(row[0])
            return total

    def file_to_list(file_name):
        with open(file_name) as csv_data:
            values = []
            reader = csv.reader(csv_data)
            for row in reader:
                values.append(int(row[0]))
            return values

    if(mode==2):
        values = file_to_list('data.csv')
        possible_sums = set()
        cur_sum = 0
        while True:
            for i in values:
                cur_sum += i
                if cur_sum not in possible_sums:
                    possible_sums.add(cur_sum)
                else:
                    return cur_sum