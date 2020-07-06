from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#decorator

# def charprint(func):
#     def inter_charprint(*args , **kwargs):
#         return func(*args , **kwargs)
#     return inter_charprint

# def decofunc(func):
#     def wrapper(*args, **kwargs):
#         print("input")
#         print(func(*args, **kwargs))
#         print('output')
#     return wrapper


class Decofunc:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('input')
        print(self.function(*args, **kwargs))
        print('output')


@Decofunc
def rescon():
    return 'aaa'

rescon()


# def new_decofunc():
#     return 'new_decofunc'
#     def inner_new_decofunc():
#         return 'new_decofunc_1'

# new_decofunc()