#!/usr/bin/python3


def safe_print_list_integers(my_list=[], a=0):
    bet = 0
    for i in range(0, a):
        try:
            print("{:d}".format(my_list[i]), end="")
            bet += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (bet)
