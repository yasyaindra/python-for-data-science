# if ["hello",12]:
#     print(True)
# else:
#     print(False)


one_less_than_three = 1 < 3 
true_equals_false = True == False


# None = null
x = None
# assert x == None
# try:
#     assert x is None
#     print("Sukses")
# except AssertionError:
#     print("x bukan None")

# Daftar tipe data dan struktur data yang merupakan false

a = False
b = None
c = []
d = {}
e = ""
f = set()
g = 0
h = 0.0

def get_string():
    return "Hello World"

s = get_string()

# if s:
#     print(s[0])
# else:
#     print("")
    
# first_string = s and s[0]

safe_x = x or 0

# x = 2

safe_x = x if x is not None else 0


# print(first_string)

# print(safe_x)

print(all([True, 1, {3}]))
print(any([False, 0, {}]))
# print(all([]))