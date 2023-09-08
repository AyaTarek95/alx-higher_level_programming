#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list:
        return my_list[idx]
    elif idx < 0:
        return "None"
    elif idx > (len(my_list) - 1):
        return (None)
