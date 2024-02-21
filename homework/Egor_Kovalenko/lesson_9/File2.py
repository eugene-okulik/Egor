import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def max_temp(x):
    return x > 28


hot_temp_value = filter(max_temp, temperatures)
new_temp_list = list(hot_temp_value)
print(max(new_temp_list))
print(min(new_temp_list))
average_temp = statistics.mean(new_temp_list)
print(round(average_temp))
