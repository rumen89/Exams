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

# def to_digits(n):
#     result = []

#     while n != 0:
#         digit = n % 10

#         result += [digit]

#         n = n // 10

#     return result

def contains_digit(number, digit):
    if digit in to_digits(number):
        return True

    return False



# 5.Number containing all digits?

# Implement a function, called contains_digits(number, digits) 
# where digits is a list of integers and number is an integer.

# The function should return True if all digits are contained in number.

# Signature

# def contains_digits(number, digits):
#     pass
# Test examples

# >>> contains_digits(402123, [0, 3, 4])
# True
# >>> contains_digits(666, [6,4])
# False
# >>> contains_digits(123456789, [1,2,3,0])
# False
# >>> contains_digits(456, [])
# True

# def to_digits(n):
#     result = []

#     while n != 0:
#         digit = n % 10

#         result = [digit] + result

#         n = n // 10

#     return result

def contains_digits(number, digits):
    for digit in digits:
        if digit not in to_digits(number):
            return False

    return True


def make_list(n):
    result = []

    while n != 0:
        number = input("Enter number: ")
        number = int(number)

        result += [number]

        n = n - 1

    return result




# 6. Is number balanced?

# A number is called balanced, 
# if we take the middle of it and the sums of the left and right parts are equal.

# For example, the number 1238033 is balanced, 
# because it's left part is 123 and right part is 033.

# We have : 1 + 2 + 3 = 0 + 3 + 3 = 6.

# A number with only one digit is always balanced!

# Implement the function is_number_balanced(n) that checks if n is balanced.

# Signature

# def is_number_balanced(n):
#     pass
# Test examples

# >>> is_number_balanced(9)
# True
# >>> is_number_balanced(11)
# True
# >>> is_number_balanced(13)
# False
# >>> is_number_balanced(121)
# True
# >>> is_number_balanced(4518)
# True
# >>> is_number_balanced(28471)
# False
# >>> is_number_balanced(1238033)
# True

def digits_count(n):
    result = 0

    for digit in to_digits(n):
        result += 1

    return result


def head(n):
    return to_digits(n)[0]


def tail(n):
    return to_digits(n)[len(to_digits(n)) - 1]


def body(n):
    result = 0

    for index in range(1, len(to_digits(n)) - 1):
        result = result * 10 + to_digits(n)[index]

    return result


def is_number_balanced(n):
    head_sum = 0

    tail_sum = 0

    while True:
        head_sum += head(n)

        tail_sum += tail(n)

        n = body(n)

        if digits_count(n) <= 1:
            break

    if head_sum == tail_sum:
        return True

    return False






# 7.Counting substrings

# Implement the function count_substrings(haystack, needle). 
# It returns the count of occurrences of the string needle in the string haystack.

# Don't count overlapped substings and take case into consideration! 
# For overlapping substrings, check the "baba" example below.

# Signature

# def count_substrings(haystack, needle):
#     pass
# Test examples

# >>> count_substrings("This is a test string", "is")
# 2
# >>> count_substrings("babababa", "baba")
# 2
# >>> count_substrings("Python is an awesome language to program in!", "o")
# 4
# >>> count_substrings("We have nothing in common!", "really?")
# 0
# >>> count_substrings("This is this and that is this", "this")  # "This" != "this"
# 2

def charachter_counter(string):
    counter = 0

    while counter < len(string):
        counter += 1

    return counter


def part_of_string(n, search_word, string):
    result = ""

    for index in range(n, n + charachter_counter(search_word)):
        result += string[index]

    return result


def count_substrings(haystack, needle):
    counter = 0

    index = 0

    while index + charachter_counter(needle) <= len(haystack):
        if part_of_string(index, needle, haystack) == needle:
            counter += 1

            index += charachter_counter(needle)

        else:
            index += 1

    return counter



# 8.Zero Insertion

# Given an integer, implement the function zero_insert(n), 
# which returns a new integer, constructed by the following algorithm:

# If two neighboring digits are the same (like 55), insert a 0 between them (505)
# Also, if we add two neighboring digits 
# and take their module by 10 (% 10) and the result is 0 - add 0 between them.
# For example, if we have the number 116457, result will be: 10160457:

# 1 and 1 are the same, so we insert 0 between them
# 6 + 4 % 10 = 0, so we insert 0 between them.
# Examples

# >>> zero_insert(116457)
# 10160457
# >>> zero_insert(55555555)
# 505050505050505
# >>> zero_insert(1)
# 1
# >>> zero_insert(6446)
# 6040406

def to_digits(n):
    result = []

    while n != 0:
        digit = n % 10

        result = [digit] + result

        n = n // 10

    return result

def to_number(digits):
    result = 0

    for digit in digits:
        result = result * 10 + digit

    return result

def zero_insert(n):
    result = []

    digits = to_digits(n)

    for index in range(0, len(digits)):
        result += [digits[index]]

        if index + 1 < len(digits):
            neighbor = index + 1

            if digits[index] == digits[neighbor] or digits[index] + digits[neighbor] == 10:
                result += [0]

    number = to_number(result)

    return number



# 9.Sum Numbers in Matrix

# You are given a NxM matrix of integer numbers.

# Implement a function, called sum_matrix(m) 
# that returns the sum of all numbers in the matrix.

# The matrix will be represented as nested lists in Python.

# Examples:

# >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# >>> sum_matrix(m)
# 45
# >>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# >>> sum_matrix(m)
# 0
# >>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# >>> sum_matrix(m)
# 55

def sum_matrix(m):
    result = 0

    for row in m:
        for element in row:
            result += element

    return result




# 10.Matrix Bombing

# You are givn a NxM matrix of integer numbers.

# We can drop a bomb at any place in the matrix, which has the following effect:

# All of the 3 to 8 neighbours (depending on where you hit!) 
# of the target are reduced by the value of the target.
# Numbers can be reduced only to 0 - they cannot go to negative.
# For example, if we have the following matrix:

# 10 10 10
# 10  9  10
# 10 10 10
# and we drop bomb at 9, this will result in the following matrix:

# 1 1 1
# 1 9 1
# 1 1 1
# Implement a function called matrix_bombing_plan(m).

# The function should return a dictionary where keys are positions in the matrix, 
# represented as tuples, and values are the total sum of the elements of the matrix, 
# after the bombing at that position.

# The positions are the standard indexes, starting from (0, 0)

# For example if we have the following matrix:

# 1 2 3
# 4 5 6
# 7 8 9
# and run the function, we will have:

# {(0, 0): 42,
#  (0, 1): 36,
#  (0, 2): 37,
#  (1, 0): 30,
#  (1, 1): 15,
#  (1, 2): 23,
#  (2, 0): 29,
#  (2, 1): 15,
#  (2, 2): 26}
# We can see that if we drop the bomb at (1, 1) or (2, 1), we will do the most damage!

def find_neghbours(n, m, matrix):
    result = []

    if n - 1 >= 0:
        begins_n = n - 1
    else:
        begins_n = n

    if n + 1 < len(matrix):
        end_n = n + 1
    else:
        end_n = n

    if m - 1 >= 0:
        begins_m = m - 1
    else:
        begins_m = m

    if m + 1 < len(matrix[0]):
        end_m = m + 1
    else:
        end_m = m

    for i in range(begins_n, end_n + 1):
        for j in range(begins_m, end_m + 1):
            if (n, m) != (i, j):
                result += [(i, j)]

    return result

def bomb_efect(n, m, matrix):
    result = []
    bomb = matrix[n][m]

    neighbors = find_neghbours(n, m, matrix)

    for a in range(0, len(matrix)):
        for b in range(0, len(matrix[a])):
            for tuple in neighbors:
                i = tuple[0]
                j = tuple[1]

                result += [matrix[a][b]

                if a == i and b == j:
                    current = matrix[i][j]

                    if current - bomb < 0:
                        current = 0
                    else:
                        current = current - bomb

                    result[a][b] = curent

    return result


def matrix_bombing_plan(m):
    result = {}

    for i in range (0, len(m)):
        for j in range(0, len(m[i])):
            bomb_matix = bomb_efect(i, j, m)
            print(m)
            result[(i, j)] = sum_matrix(bomb_matix)

    return result




def main():
    # n = input("Enter some number: ")
    # n = int(n)

    # m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

    # haystack = input("Enter haystack: ")
    # needle = input("Enter needle: ")

    # digit = input("Enter single digit: ")
    # digit = int(digit)

    # number = input("Enter digit counter: ")
    # number = int(number)

    # digits = make_list(number)

    # print("Sum of all divisors of {} is: {}".format(n, sum_of_divisors(n)))
    # print("Is {} a prime number? \n{}".format(str(int(n)), is_prime(n)))
    # print("Is {} has a prime number of divisors? \n{}".format(n, prime_number_of_divisors(n)))
    # print("Is {} in {}? \n{}".format(digit, n, contains_digit(n, digit)))
    # print("Is digits of {} in {}? \n{}".format(n, digits, contains_digits(n, digits)))
    # print(body(n))
    # print("Is {} a balanced number? \n{}".format(n, is_number_balanced(n)))
    # print(count_substrings(haystack, needle))
    # print(zero_insert(n))
    # print(sum_matrix(m))
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(matrix_bombing_plan(m))
    print(bomb_efect(0, 1, m))
    # print(find_neghbours(0, 2, m))

if __name__ == '__main__':
    main()