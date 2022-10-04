next = 0
first = 0
second = 1

n = int(input())

for i in range(0, n + 1):
  # next = i
  fib = next
  print(first)
  next = first + second
  first = second
  second = next