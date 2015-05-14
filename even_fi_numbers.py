#even_fi_numbers.py

# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

def even_number(number):
    return number % 2 == 0

def fibonacci_number(n):
    fib_number = []

    if n == 1:
        fib_number = [1]
    elif n == 2:
        fib_number = [1, 2]
    elif n < 1:
        fib_number = []
    else:
        fib_number = [1, 2]

        for index in range(0, n - 2):
            next_number = fib_number[index] + fib_number[index + 1]

            if next_number > 4000000:
                break

            fib_number.append(next_number)

    return fib_number

# print(fibonacci_number(4000000))

def sum_even_fib_numbers(n):
    result = 0

    for number in fibonacci_number(n):
        if even_number(number):
            result += number

    return result

def main():
    n = input("Enter number: ")
    n = int(n)

    print(sum_even_fib_numbers(n))

if __name__ == '__main__':
    main()