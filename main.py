import random
x=int(input('enter how many times you want to roll the dice'))
i=0
while (i < x):
    a=[]
    user=input('enter y if you want to continue or n if you want to stop and exit: ').lower()
    if user=='y':
        a.append(random.randint(1,6))
        a.append(random.randint(1,6))
    elif user=='n':
        print('You have exited the program.')
        print('The final list is:', a)
        print(f'the number of times you have rolled is {i+1}')
        break
    else:
        print("invalid input, please enter y or n")
        continue
    print(a)
    i+=1
print(f'the number of times you have rolled is {i}')
