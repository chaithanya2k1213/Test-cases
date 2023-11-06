import random
comp_num=random.randint(1,101)
a=[]
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
        num=int(input('Guess a number between 1 and 1002: '))
        a.append(num)
        if num==comp_num:
            print('Congratulations!!! You have guessed the number in {}'.format(len(a)))
            break
        #1
        if num>100 or  num<1:
            print('OUT OF BOUNDS')
            
        
        #2
        if (comp_num+10>num) and (num>comp_num-10):
            
            print('WARM')
            #3
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
                
                    
                    