#!/usr/bin/python3

# a method that prints in stdout the character '#' n times for the height and width

def display(n, m):
    for i in range(m):
        for j in range(n):
            print('#', end='')
        print()



display(4, 6)