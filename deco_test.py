#decorator

# def charprint(func):
#     def inter_charprint(*args , **kwargs):
#         return func(*args , **kwargs)
#     return inter_charprint

def decofunc(func):
    def wrapper(*args, **kwargs):
        print("input")
        print(func(*args, **kwargs))
        print('output')

    return wrapper


@decofunc
def new_decofunc():
    return 'new_decofunc'


new_decofunc()