def sum_of_even(n):
  sum = 0
  for i in range(0,n + 1):
    if(i%2 != 0):
      continue
    else:
      sum=sum+i

  return (sum)

num = int(input())
print(sum_of_even(num))
