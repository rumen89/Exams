# largest_prime_factor.py

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def prime_number(number):
    counter = 2

    while counter < number:
        if number % counter == 0:
            return False

        counter += 1

    return True

def largest_prime_factor(n):
    result = 0

    m = n // 2

    while m > 2:
        if n % m == 0 and prime_number(m):
            result = m
            break
        print (m)
        m -= 1

    return result

print(largest_prime_factor(600851475143))