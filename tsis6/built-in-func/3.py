def isPalindrome(s):
    rev = "".join(reversed(s))
    print(rev)
    if (s == rev):
        return True
    return False
  
s = input()
a = isPalindrome(s)
  
if (a):
    print("Yes")
else:
    print("No")