def fact(n):
    zeroes = 0
    for i in range(5, n*5):
        zeroes = zeroes + n/i
    return zeroes
num = int(input("Enter a number"))
if num<0:
    print("the fact is not exist")
else:
    print("the trail_factorial is",fact(num))