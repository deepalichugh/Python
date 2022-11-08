def sum_of_n(n):
    i = 1
    sum = 0
    while(i<=n):
        sum = sum + i
        i=i+1

    return sum

n = int(input())
print(sum_of_n(n))