#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = list(dict.fromkeys(my_list))
    sum = 0
    for x in sorted_list:
        sum += x
    return sum
