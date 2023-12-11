my_list = [1,2]
my_tuples = (3,4)

try:
    my_tuples[0] = 1
except TypeError:
    print("Tuples cannot be modified")

def sum_numbers(x, y):
    return (x+y),(y-x)

a, b = sum_numbers(4,5)

print(a)
print(b)