def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(3,5))

def area_of_circle(r):
    return r * r * 3.14

print(area_of_circle(5))

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if (not isinstance(num, (int, float))):
            print("Bad input")
            return
        else:
            sum = num + sum
    return sum

print(add_all_nums(3, 4.5, 7))
print(add_all_nums(3, 7, 'hi'))

def capitalize_list_items(list):
    for i in range(len(list)):
        list[i] = list[i].capitalize()
    return list

print(capitalize_list_items(['hi', 'BYE', 'Aa']))

def greet(Name= 'Guest'):
    print(f'Hello, {Name}')

greet()
greet("alice")

def is_prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print("7:", is_prime(7))
print("48:", is_prime(48))
print("11:", is_prime(11))
print("37:", is_prime(37))
print("100:", is_prime(100))
print("999:", is_prime(999))

key_words = []
def valid_variable(var):
    if var in key_words:
        return False
    
    for char in var:
        # check alphanumeric or underscore
        pass
    
    return True