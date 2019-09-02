def checkPalindrom(s):
    if s==s[::-1]: # a good way to reverse a string
        return True
    else:
        return False

def Longest_palindrom_substring():
    s = input("enter you string")
    max_len = -1
    pal_string = ""
    for i in range(0, len(s)+1, 1):
        for j in range(i+1, len(s)+1, 1):
            #print(s[i:j],max_len,i,j)
            if checkPalindrom(s[i:j]) == True and max_len < j - i:
                max_len = j - i
                pal_string = s[i:j]

    return max_len,pal_string

while True:
    ans=Longest_palindrom_substring()
    print(ans[0])
    print(ans[1])

