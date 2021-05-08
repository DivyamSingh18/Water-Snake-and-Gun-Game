import random

co=0
u=0
games =0
lst = ['snake','water', 'gun']
print("---------------------------The game has begun-------------------------------")
while games < 10 :
    comp = random.choice(lst)
    user = input("\nEnter your choice:")

    print(f" computer: {comp}   -   You: {user}    ")

    if comp == 'snake' and user == 'water':
        co+=1
        print(f'you lose , computer won,  SCORE -> COM:{co} , You:{u} ' )
    elif comp == 'water' and user == 'snake':
        u+=1
        print(f'you won , computer lost,  SCORE -> COM:{co} , You:{u} ')

    elif comp == 'water' and user == 'gun':
        co+=1
        print(f'you lose , computer won,  SCORE -> COM:{co} , You:{u} ' )
    elif comp == 'gun' and user == 'water':
        u+=1
        print(f'you won , computer lost,  SCORE -> COM:{co} , You:{u} ')

    elif comp == 'gun' and user == 'snake':
        co+=1
        print(f'you lose , computer won,  SCORE -> COM:{co} , You:{u} ' )
    elif comp == 'snake' and user == 'gun':
        u+=1
        print(f'you won , computer lost,  SCORE -> COM:{co} , You:{u} ')
    elif comp == user:
        print(f"Its a Draw,  SCORE -> COM:{co} , You:{u} ")
    else:
        print('Inavlid input')

    games+=1

if co > u:
    print(f"Final Score -> COM:{co} , You:{u} \n")
    print("!!!Computer Wins!!!")
elif co<u:
    print(f"Final Score -> COM:{co} , You:{u} \n")
    print('!!!You Won!!!')
else:
    print(f"Final Score -> COM:{co} , You:{u} \n")
    print('It\'s a Draw')