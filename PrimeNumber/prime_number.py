def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False


    # loop through all numbers between 2 and the number
    # check to see if number(num) can be divided by the potential prime number
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

