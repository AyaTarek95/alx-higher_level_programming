#!usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
 
    bil = 0
    for z in range(0, x):
        try:
            print("{:d}".format(my_list[z]), end="")
            bil += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (bil)
