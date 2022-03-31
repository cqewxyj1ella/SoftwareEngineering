# define after call
def myALU():
    add = sum
    add()

    def sub():
        pass
    sub()

    class MyClass:
        pass
    MyClass()

# function arguments
param_args = [1, 2, 3]
param_kwargs = {'x': 1, 'y': 2}

def print_2_args(a, b=1):
    print(a, b)

print_2_args(1)

# identical value compare/calculate
if a == b: # Noncompliant
    print("equal!")

if  a != b: # Noncompliant
    print("not equal!")

if  a == b and a == c: # Noncompliant
    print("a equal to b and a equal to c!")

j = 5 / 3
k = 5 - 4

# ignore function's params' values
def myFunc(strings, integers):
    store = integers
    integers = 1  # NonCompliant