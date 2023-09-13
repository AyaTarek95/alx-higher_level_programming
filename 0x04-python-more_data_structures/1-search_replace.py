#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = []
    for x in my_list:
        if x == search:
            rep_list.append(replace)
        else:
            rep_list.append(x)
    return rep_list
