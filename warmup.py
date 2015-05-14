# warmup.py

# Palindrome Score

# We denote the "Palindrome score" of an integer by the following function:

# P(n) = 1, if n is palindrome
# P(n) = 1 + P(s) where s is the sum of n and the reverse of n
# Implement a function, called p_score(n), which finds the palindrome score for n.

# Lets see two examples:

# p_score(121) = 1, because 121 is a palindrome.
# p_score(48) = 3, because:

# P(48) = 1 + P(48 + 84) = 132
# P(132) = 1 + 1 + P(132 + 321 = 363)
# P(363) = 1.
# When we return from the recursion, we get 3.
# Signature

# def p_score(n):
#     pass
# Test examples

# >>> p_score(121)
# 1
# >>> p_score(48)
# 3
# >>> p_score(198)
# 6

def reverse_number(n):
    result = 0

    while n != 0:
        digit = n % 10

        result = result * 10 + digit

        n = n // 10

    return result

def is_palindrome(n):
    if reverse_number(n) == n:
        return True

    return False



def p_score(n):
    result = 0
    if_not_palindrome = 0

    while 1:
        if is_palindrome(n):
            result += if_not_palindrome + 1
            break
        else:
            n = n + reverse_number(n)
            if_not_palindrome += 1

    return result


# def main():
#     n = input("Enter number: ")
#     n = int(n)

#     print(p_score(n))

# if __name__ == '__main__':
#     main()



# Hack Numbers

# A hack number is an integer, that matches the following criteria:

# The number, represented in binary, is a palindrome
# The number, represented in binary, has an odd number of 1's in it
# Example of hack numbers:

# 1 is 1 in binary
# 7 is 111 in binary
# 7919 is 1111011101111 in binary
# Implement a function, called next_hack(n) 
# that takes an integer and returns the next hack number, that is bigger than n

# Signature

# def next_hack(n):
#     pass
# Test examples

# >>> next_hack(0)
# 1
# >>> next_hack(10)
# 21
# >>> next_hack(8031)
# 8191

def number_to_list(n):
    result = []

    while n != 0:
        digit = n % 10

        result += [digit]

        n = n // 10

    return result




def is_palindrome(n):
    result = 0

    for number in number_to_list(n):
        result = result * 10 + number

    return result




def to_binary(n):
    result = ""

    while 1:
        result = str(n % 2) + result

        n = n // 2

        if n <= 1:
            result = str(n) + result
            break

    return int(result)


def count_on_one(n):
    counter = 0

    n = to_binary(n)

    for number in number_to_list(n):
        if number == 1:
            counter += 1

    return counter

def is_odd(n):
    if n % 2 != 0:
        return True

    return False



def next_hack(n):
    m = n + 1

    while 1:
        if is_palindrome(to_binary(m)) and is_odd(count_on_one(m)):
            return m
        else:
            m += 1

def main():
    n = input("Enter some number: ")
    n = int(n)

    next_number = n + 1

    while 1:
        if is_palindrome(to_binary(n)) and is_odd(count_on_one(n)):
            print("First hack number is: {}".format(n))
            print("Next hack number is: {}".format(next_hack(n)))
            break
        else:
            n += 1


if __name__ == '__main__':
    main()
