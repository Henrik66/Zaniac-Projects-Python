#this function finds all of the multiples of 3 and 5 and evaluates their sum

def multiples_of_3_5(limit):
    mult_3 = []
    mult_5 = []
    mult_15 = []
    for i in range(1, limit):
        if i % 3 == 0:
            mult_3.append(i)
        if i % 5 == 0:
            mult_5.append(i)
        if i % 3 == 0 and i % 5 == 0:
            mult_15.append(i)
    sum_mult_3 = sum(mult_3)
    sum_mult_5 = sum(mult_5)
    sum_mult_15 = sum(mult_15)
    
    total_sum = sum_mult_3 + sum_mult_5 - sum_mult_15

    return total_sum

print(multiples_of_3_5(1000))
