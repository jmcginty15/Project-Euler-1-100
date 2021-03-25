def even_fibonacci_numbers():
    even_sum = 2
    n0 = 1
    n1 = 2

    while n1 < 4000000:
        new_sum = n0 + n1
        n0 = n1
        n1 = new_sum

        if n1 % 2 == 0:
            even_sum += n1
    
    return even_sum

print(even_fibonacci_numbers())