def mult_3_and_5():
    sum3 = 0
    sum5 = 0

    for n in range(3, 1000, 3):
        sum3 += n
    for n in range(5, 1000, 5):
        if n % 3 != 0:
            sum5 += n
    
    return sum3 + sum5

print(mult_3_and_5())