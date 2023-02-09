def pal(str):
    str1=str[::-1]
    if str == str1:
        return True
    return False

str=input()
print(pal(str))