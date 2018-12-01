import csv

def calculate(mode=1):

    """
    Function solving the Day 1 problems.
    mode = 1 solves the first of the problems, 
    while mode = 2 solves the second problem.
    """
    
    if(mode==1):
        with open('data.csv') as csv_data:
            sum = 0 # start value for sum
            reader = csv.reader(csv_data)
            for row in reader:
                sum += int(row[0])

            print(sum)

    if(mode==2):
        with open('data.csv') as csv_data:
            sum = 0
            dict_of_sums = {}
            reader = csv.reader(csv_data)
            not_complete = True
            while not_complete:
                for row in reader:
                    sum += int(row[0])
                    if sum in dict_of_sums:
                        print(sum)
                        not_complete = False
                    else:
                        dict_of_sums[sum]= True
