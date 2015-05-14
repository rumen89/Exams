# n_prime_digit.py

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.

# What is the 10 001st prime number?

import time

def prime_number(n):
    counter = 3

    while counter <= n ** (0.5 + 1):
        if n % 2 == 0:
            return False
        if n % counter == 0:
            return False
        counter += 2

    return True


def n_prime_number(n):
    result = 0

    counter = 3

    while n >= 0:
        if prime_number(counter):
            result = counter
            n -= 1
            print(result)
        counter += 2

    return result

def main():
    n = input("Enter number: ")
    n = int(n)
    begin = time.time()
    n_prime_number(n)
    end = time.time()
    total = end - begin
    # print(n_prime_number(n))
    print("Total time is: {}".format(total))

if __name__ == '__main__':
    main()
