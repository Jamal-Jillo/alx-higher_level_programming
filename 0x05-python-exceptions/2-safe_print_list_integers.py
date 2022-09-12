#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if my_list[i] is int:
                print("{:d}".format(my_list[i]), end="")
            print()
            return x
    except (ValueError, TypeError):
        print()
        return i
