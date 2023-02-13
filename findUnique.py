import sys

def findUnique(arr, n) :
    #Your code goes here
    d1 = dict()
    count = 0
    for i in arr:
        d1[i] = d1.get(i, 0) + 1
    for i in d1:
        if d1[i] == 1:
            return (i)

print(findUnique([2, 3, 1, 6, 3, 6, 2], 7))
    























#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1