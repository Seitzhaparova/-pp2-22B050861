import random
def check(x, name, cnt):
    num=int(input('Take a guess.'))
    cnt += 1
    if num==int(x):
        print('Good job,' + name + '! You guessed my number in '+ str(cnt) + ' guesses!')
    elif num<int(x):
        print('Your guess is too low.')
        check(x, name, cnt)
    elif  num>int(x):
        print('Your guess is too high.')
        check(x, name, cnt)
        
x=random.uniform(1,20)
print(x)
cnt=0
name= input('Hello! What is your name?')
print('Well, '+ name +', I am thinking of a number between 1 and 20.')
check(x, name, cnt)

