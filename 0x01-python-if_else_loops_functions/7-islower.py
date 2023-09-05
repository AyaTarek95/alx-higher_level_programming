#!/usr/bin/python3
def islower(c):
    #function to check wether the character passed is lowercase or othrwise
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
