#!/usr/bin/python3
'''Defines a base class.'''
#import turtle
#import json
#import csv


class Base:
    '''represent Base class.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initiate new base.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

