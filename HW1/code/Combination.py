# define after call
def myALU():
    add()  # Noncompliant
    add = sum

    sub()  # Noncompliant
    def sub():
        pass

    MyClass()  # Noncompliant
    class MyClass:
        pass

# function arguments
param_args = [1, 2, 3]
param_kwargs = {'x': 1, 'y': 2}

def print_2_args(a, b=1):
    print(a, b)

print_2_args(1)
print_2_args(1, 2, 3)
print_2_args()

def print_limited_args(a, *, b=2):
    print(a, b)

print_limited_args(1, 2)
print_limited_args(z=42)

# identical value compare/calculate
if a == a: # Noncompliant
    print("equal!")

if  a != a: # Noncompliant
    print("not equal!")

if  a == b and a == b: # Noncompliant
    print("a equal to b!")

j = 5 / 5
k = 5 - 5

# ignore function's params' values
def myFunc(strings, integers):
    integers = 1  # NonCompliant