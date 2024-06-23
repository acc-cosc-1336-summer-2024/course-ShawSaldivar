#

def get_factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    sum = 0
    x = 0

    while x <= num:
        if x % 2 != 0:
            sum += x
        x += 1
        
    return sum