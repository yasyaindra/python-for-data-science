x = 1

if x > 2:
    print(True)
else:
    print(False)
    
is_success = "Success!" if x == 200 else "Failed!"
# print(is_success)

x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1
    
for x in range(10):
    if x == 2:
        print("Dua")
        continue
    if x == 7:
        print("Tujuh")
        break
    print(x)