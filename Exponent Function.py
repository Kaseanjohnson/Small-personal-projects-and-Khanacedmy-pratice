def up_the_power( base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(up_the_power(2,3))