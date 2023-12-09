def double(x):
    return x * 2

def apply_to_one(f):
    return f(1)

my_double = double

x = apply_to_one(my_double)

print(x)

y = apply_to_one(lambda x: x + 4)

another_func = lambda x: x - 1

# sama dengan ini

def another_func():
    return x - 1

print(y)