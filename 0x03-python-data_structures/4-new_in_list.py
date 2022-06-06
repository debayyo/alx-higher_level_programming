#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_listt = my_list.copy()
    if idx < 0:
        return my_listt
    if idx >= len(my_listt):
        return my_listt
    my_list[idx] = element
    return my_listt
