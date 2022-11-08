#Given a number N, print sum of all even numbers from 1 to N.

def sum_of_even(n):
	sum = 0
	i = 1
	while(i<=n):
		if(i % 2 == 0):
			sum = sum + i
		i = i + 1

	return sum

n = int(input())
print(sum_of_even(n))