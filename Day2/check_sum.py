import csv

def solve_problem1():
    with open('data.csv') as csv_data:
            doubles = 0
            triples = 0
            reader = csv.reader(csv_data)
            for row in reader:
                cur_string = row[0]
                letter_dict = dict()
                for char in cur_string:
                    if char in letter_dict:
                        letter_dict[char] += 1
                    else:
                        letter_dict[char] = 1
                has_double = False
                has_triple = False
                for char in letter_dict:
                    if (letter_dict[char] == 2 and not has_double):
                        doubles += 1
                        has_double = True
                    elif (letter_dict[char] == 3 and not has_triple):
                        triples += 1
                        has_triple = True
            return (doubles * triples)

def solve_problem2():
    with open('data.csv') as csv_data:
        reader = csv.reader(csv_data)
        string_list = list(reader)

        j = 0
        for i in range(len(string_list)):
            cur_string = string_list[i]
            for n in range(len(string_list[i])):

        
            