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
        for i in range(len(values)):
            index = i
            for n in range(len(values)):
                if (index == len(values) - 1):
                    index = 0
                elif(index == i - 1):
                    break
                total = sum(possible_sums) + values[i]
                print(total)
                if total in possible_sums:
                    return total
                else:
                    possible_sums.add(total)
