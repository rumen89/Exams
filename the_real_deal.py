# the_real_deal.py

# 1.Sum all divisors of an integer

# Given an integer, implement a function, called sum_of_divisors(n) 
# that calculates the sum of all divisors of n.

# For example, the divisors of 8 are 1, 2, 4 and 8 and 1 + 2 + 4 + 8 = 15. 
# The divisors of 7 are 1 and 7, which makes the sum = 8.

# Signature

# def sum_of_divisors(n):
#     pass
# Test examples

# >>> sum_of_divisors(8)
# 15
# >>> sum_of_divisors(7)
# 8
# >>> sum_of_divisors(1)
# 1
# >>> sum_of_divisors(1000)
# 2340

def sum_of_divisors(n):
    counter = 1

    sum_of_all_divisors = 0

    while counter <= n:
        if n % counter == 0:
            sum_of_all_divisors += counter

        counter += 1

    return sum_of_all_divisors




# 2.Check if integer is prime

# Given an integer, implement a function, 
# called is_prime(n) which returns True if n is a prime number. 
# You should handle the case with negative numbers too.

# A prime number is a number, that is divisible only by 1 and itself.

# 1 is not considered to be a prime number. If you are curious why, find out here.

# Signature

# def is_prime(n):
#     pass
# Test examples

# >>> is_prime(1)
# False
# >>> is_prime(2)
# True
# >>> is_prime(8)
# False
# >>> is_prime(11)
# True
# >>> is_prime(-10)
# False

def is_prime(n):
    counter = 2

    if n < 0:
        n = n * (-1)

    if n == 1:
        return False

    while counter < n:
        if n % counter == 0:
            return False

        counter += 1

    return True




# 3.Check if a number has a prime number of divisors

# Given an integer, implement a function, called prime_number_of_divisors(n), 
# which returns True if the number of n's divisors is a prime number, 
# False otherwise.

# For example, the divisors of 8 are 1, 2, 4 and 8, 
# a total of 4. 4 is not a prime number. The divisors of 9 are 1, 
# 3 and 9, a total of 3. 3 is a prime number.

# Signature

# def prime_number_of_divisors(n):
#     pass
# Test examples

# >>> prime_number_of_divisors(7)
# True
# >>> prime_number_of_divisors(8)
# False
# >>> prime_number_of_divisors(9)
# True

def prime_number_of_divisors(n):
    counter = 1

    divisors_count = 0

    while counter <= n:
        if n % counter == 0:
            divisors_count += 1

        counter += 1

    if is_prime(divisors_count):
        return True

    return False


# 4.Number containing a single digit?

# Implement a function, called contains_digit(number, digit) which checks 
# if digit is contained in the given number.

# digit and number are integers.

# Signature

# def contains_digit(number, digit):
#     pass
# Test examples

# >>> contains_digit(123, 4)
# False
# >>> contains_digit(42, 2)
# True
# >>> contains_digit(1000, 0)
# True
# >>> contains_digit(12346789, 5)
# False

def to_digits(n):
    result = []

    while n != 0:
        digit = n % 10

        result += [digit]

        n = n // 10

    return result

def contains_digit(number, digit):
    if digit in to_digits(number):
        return True

    return False


def main():
    n = input("Enter some number: ")
    n = int(n)

    digit = input("Enter single digit: ")
    digit = int(digit)

    # print("Sum of all divisors of {} is: {}".format(n, sum_of_divisors(n)))
    # print("Is {} a prime number? \n{}".format(str(int(n)), is_prime(n)))
    # print("Is {} has a prime number of divisors? \n{}".format(n, prime_number_of_divisors(n)))
    print("Is {} in {}? \n{}".format(digit, n, contains_digit(n, digit)))


if __name__ == '__main__':
    main()