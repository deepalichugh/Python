
def checkMember(n):
#Implement Your Code Here
    num1 = 0
    num2 = 1
    sum = 0
    arr = []
    while sum <= n:
        sum = num1+num2
        if n == num1 or n == num2 or n == sum:
            ans = True
        else:
            ans = False
        num1 = num2
        num2 = sum
    return ans
   
    

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")