from random import *
import string
def random_user_id(length):
    bank = string.ascii_letters + string.digits
    id = ""
    for i in range(length):
        index = randint(0, len(bank) - 1)
        id = id + bank[index]
    return id


def user_id_gen_by_user():
    length = int(input("number of chars: "))
    count = int(input("number of IDs: "))
    for i in range(count):
        print(random_user_id(length))

def seven_random_numbers():
    first = randint(0,9)
    second = randint(0,9)
    while (first == second):
        second = randint(0,9)

    output = []
    for i in range(10):
        if i != first and i != second:
            output.append(i)
    return output

print(seven_random_numbers())

def shuffle_list(param):
    n = len(param)
    # do a list of 0 to n-1, then randint an index, pop it out, and assign it
    # to another list. Then use this as the list of "new" indices, construct 
    # the new one, and return it
