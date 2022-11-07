def check_integer_type(n):
    if n >= 1:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"

n = int(input())
print(check_integer_type(n)) 