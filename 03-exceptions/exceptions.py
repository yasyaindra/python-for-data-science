# try:
#     print(0/0)
# except ZeroDivisionError:
#     print("cannot divide in zero")

while True:
    try:
        x = int(input("Please input a number:"))
        print(x)
        break
    except ValueError:
        print("Number is invalid")