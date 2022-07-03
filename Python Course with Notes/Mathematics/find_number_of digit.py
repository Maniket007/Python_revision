#Iterative approach
#def countdigit(n):
    #count=0
    #while n!=0:
        #n//=10
        #count=count+1
    #return count
#n=345289467
#print("number is %d"%countdigit(n))

#Recurcive approach
def countdigit(n):
    if n//10 == 0:
        return 1
    return 1+countdigit(n//10)
n=2334556
print("Number is %d"%countdigit(n))