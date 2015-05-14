# squares.py

# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

def sum_of_square(n):
    result = 0

    counter = 1

    while counter <= n:
        result += counter ** 2

        counter += 1

    return result


def square_of_sum(n):
    result = 0

    counter = 1

    while counter <= n:
        result += counter

        counter += 1

    return result ** 2


def difference(n):
    return square_of_sum(n) - sum_of_square(n)


def main():
    n = input("Enter number: ")
    n = int(n)

    print(difference(n))

if __name__ == '__main__':
    main()