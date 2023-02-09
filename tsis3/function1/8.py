def spy_game(nums):
    for i in range(0, len(nums)-1):
        if int(nums[i])==0 and int(nums[i+1])==0:
            if int(nums[i+2])==7:
                return True
    return False

a=input('input list of integers: ')
userlist=a.split()
print(spy_game(userlist))
