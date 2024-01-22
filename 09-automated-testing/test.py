def smallest_item(xs):
    return min(xs)


# try:
#     assert 4 + 5 == 10
#     print("SUKSES")
# except AssertionError:
#     print("ERROR")


try:
    assert smallest_item([1,3,6,10,-3]) == 3
    print("SUKSES")
except AssertionError:
    print("ERROR")