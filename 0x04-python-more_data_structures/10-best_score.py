#!/usr/bin/python3
def best_score(a_dictionary):
    new_list = a_dictionary.copy()
    for key in new_list:
        if new_list[key] == max(new_list.values()):
            return key
