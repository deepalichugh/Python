def fah_to_cel(s, e, w):
    cel = 0
    for fah in range(s, e+1, w):
        cel = ((fah - 32)*5)/9
        print(fah, cel)

s = int(input())
e = int(input())
w = int(input())
fah_to_cel(s, e, w)