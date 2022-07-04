#Itrerative approach..
#def get_factorial_for_loop(n):
#    result = 1
#     if n > 1:
#       for i in range(1, n+1):
#           result = result * i
#       return result
#   else:
#       return 'n has to be positive'
#inp = input("Enter a number: ")
#inp = int(inp)
#print(f"The result is: {get_factorial_for_loop(inp)}") 

#Recurcive approach..
def rec(n):
    if n==0:
        return 1
    else:
        return n*rec(n-1)
num = int(input("Enter a number"))
if num<0:
    print("the fact is not exist")
else:
    print("the factorial is",rec(num))