import random
comp_num=random.randint(1,101)
a=[]
print('GUESSING GAME CHALLENGE')
print('# You have to guess a random number which is choosen by the computer.')
print("# If you have choosen the number with less than difference of 10 of Computer's number then you will get output as WARM")
print("# If you have choosen the number with more than difference of 10 of Computer's number then you will get output as COLD")
print("# After getting WARM if your number is closer to the number than the previous guess, return WARMER!")
print("# After getting WARM if your number is farther from the number than the previous guess, return COLDER!")
print("# If your guess equals to the computer number, then it will print in how many chances u have completed the game")
num=int(input('Guess a number between 1 and 100: '))
if num==comp_num:
    print('Congratulations!!! You have guessed the number in {}'.format(len(a)))
elif num!=comp_num:
    if (comp_num+10>num) and (num>comp_num-10):
        a.append(num)
        print('WARM')
    else:
        a.append(num)
        print('COLD')
    while 1:
        num=int(input('Guess a number between 1 and 100: '))
        a.append(num)
        if num==comp_num:
            print('Congratulations!!! You have guessed the number in {}'.format(len(a)))
            break
        
        if num>100 or  num<1:
            print('OUT OF BOUNDS')
            
        
        
        if (comp_num+10>num) and (num>comp_num-10):
            
            print('WARM')
            
            while 1:
                num=int(input('Guess a number between 1 and 100: '))
                a.append(num)
                e=a[-2]-comp_num
                if e<0:
                    e=-(e)
                f=num-comp_num
                if f<0:
                    f=-(f)
                if num==comp_num:
                    print('Congratulations!!! You have guessed the number in {}'.format(len(a)))
                    break
                
                elif (comp_num+10<num) and (num<comp_num-10):
                    a.append(num)
                    print('COLD')
                elif e>f:
                    print('WARMER!!')
                elif e<f:
                    print('COLDER!!!')              
            break
        elif (comp_num+10<=num) or (num<=comp_num-10):
            a.append(num)
            print('COLD')
                
                    
                    