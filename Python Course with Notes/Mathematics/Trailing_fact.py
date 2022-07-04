def trailfact(n):
    fact=1
    for i in range(1, n+1):
        fact = fact*i
    zeroes = 0
    while(fact%10==0):
        fact = fact/10
        zeroes = zeroes+1
    return zeroes
num = int(input("Enter a number"))
if num<0:
    print("the fact is not exist")
else:
    print("the trail_factorial is",trailfact(num))