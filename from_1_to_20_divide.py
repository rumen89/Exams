# from_1_to_20_divide.py

# 2520 is the smallest number 
# that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers 
# from 1 to 20?


def prime_factor(n):
    result = []

    counter = 2

    while 1:

        if n % counter == 0:
            result += [counter]
            n = n // counter
            counter = 2
        elif n % counter != 0:
            counter += 1

        if n == 1:
            break
        # print(n)
        # print(result)
    return result

def prime_numbers(n, numbers):
    result = []

    counter = 2

    for number in numbers:
        if number in result and number ** counter + 1 <= n:
            result += [number]
            counter += 1
        elif number not in result:
            result += [number]
            counter = 2

    return result



def n_to_m_divider(n, m):
    numbers = []

    result = 1

    for number in range(n, m + 1):
        numbers += prime_factor(number)

    prime_numbers_list = prime_numbers(m, sorted(numbers))

    for number in prime_numbers_list:
        result *= number

    return result


def main():
    n = input("Enter first number: ")
    n = int(n)

    m = input("Enter second number(must be bigger than first number): ")
    m = int(m)

    print(n_to_m_divider(n, m))


if __name__ == '__main__':
    main()