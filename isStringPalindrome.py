def palindrome(s):
    if s == " ":
        return True
    s3 = ""
    s2 = ""
    ans = True
    for i in range(len(s)):
        if s[i].isdigit() == True:
            s2 = s2 + s[i]
        elif s[i].isalpha() == True:
            s2 = s2 + s[i].lower()
        else:
            s2 = s2 + ""

    for i in range(len(s2)):
        if s2[i] >= "a" and s2[i] <= "z" or s2[i] >= '0' and s2[i] <= '9':
            s3 = s3 + s2[i]

    for i in range(len(s3)):
        j = len(s3) - i - 1
        if j>i and s3[j] != s3[i]:
            ans = False
            break
    print(ans)

palindrome("race a car")