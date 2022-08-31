#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    for i in range(len(list_1)):
        for x in range(len(list_2)):
            if list_1[i] == list_2[x]:
                return set(list_1[i])
