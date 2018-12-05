import string

def solve_1():
    with open('data.txt', 'r') as data:
        message = data.read()
        return reactions(message)

def reactions(message: str):
    while True: #Until all reactions have happened
            prev_len = len(message)
            for n in range(len(message) - 1):
                if message[n].lower() == message[n + 1].lower():
                    if message[n]!= message[n + 1]:
                        message = message[:n] + message[n + 2:]
                        break
            if prev_len == len(message): #If no new elements have been removed to problem is solved and the current length is returned.
                return len(message)

def solve_2():
    lengths = []
    lowercase_alphabet = string.ascii_lowercase
    for letter in lowercase_alphabet:
        with open('data.txt', 'r') as data:
            message = data.read()
            new_message = remove_letter(message, letter)
            cur_len = reactions(new_message)
            print(cur_len)
            lengths.append(cur_len)
    return max(lengths)

def remove_letter(message: str, letter: str):
    while True:
        cur_len = len(message)
        for n in range(len(message)):
            if message[n].lower() == letter:
                message = message[:n] + message[n + 1:]
                break
        if cur_len == len(message):
            return message

        