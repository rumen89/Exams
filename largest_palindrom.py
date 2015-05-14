# largest_palindrom.py

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def count_digits(number):
    result = 0

    while number != 0:
        number = number // 10

        result += 1

    return result

# print(count_digits(131))

def reverse_number(number):
    result = 0

    while number != 0:
        digit = number % 10

        result = result * 10 + digit

        number = number // 10

    return result


def is_palindrom(number):
    return number == reverse_number(number)

# print(is_palindrom(131))
# print(reverse_number(131))


def smaller_number(m):
    result = 1

    counter = 1

    while counter < m:
        result = result * 10

        counter += 1

    return result


def bigger_number(m):
    result = 9

    counter = 1

    while counter < m:
        result = result * 10 + 9

        counter += 1

    return result

# print(smaller_number(3))
# print(bigger_number(3))



def largest_palindrom(m):

# 'm' е броят на цифрите в числото

    result = 0

    for number in range(smaller_number(m), bigger_number(m) + 1):
        for number_2 in range(smaller_number(m), bigger_number(m) + 1):
            if is_palindrom(number * number_2):
                palindrom = number * number_2

    result = palindrom

    return result

print(largest_palindrom(3))
