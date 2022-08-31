#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        new_list= map(lambda replace: replace if new_list[i] == search else new_list[i], new_list)
        print(new_list)
 
search_replace([1, 2, 3, 4, 5], 2, 98)      
