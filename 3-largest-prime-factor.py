import math

def is_prime(n):
    for i in range(2, math.ceil(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    
    return True

def largest_prime_factor(n):
    divisor = 2

    while divisor < n / 2:
        factor = n / divisor

        if factor % 1 == 0 and is_prime(factor):
            return int(factor)
        else:
            divisor += 1

print(largest_prime_factor(600851475143))