#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    total = 0
    for element in my_list:
        if element not in uniq_list:
            total += element
            uniq_list.append(element)
    return total
