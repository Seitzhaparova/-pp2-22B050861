def has_33(nums):
    #txt=0
    for i in range(0, len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

    """if(txt>=2):
        return True
    else: return False
    """
"""1
a=input('input list of integers: ')
userlist=a.split()

print(has_33(userlist))
"""
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]) )
print(has_33([3, 1, 3]))
