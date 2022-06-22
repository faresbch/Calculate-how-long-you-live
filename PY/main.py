

# The Age of The Person

age = int(input("Enter Your Age Here :"))

# Chose The Unite

unite = input("Chose Which Unite You Want Below This : Month, Weeks, Days ").strip().lower()

# Unite Sections
month = age * 12
weeks = month * 4
days = age * 365

if unite == 'month' :
    
    print('You Have Chosed Month Unite')
    print(f'You Have leaved For {month:,}')

elif unite == 'weeks' :
    
    print('You Have Chosed weeks Unite')
    print(f'You Have leaved For {weeks:,}')
    
elif unite == 'days' :
    
    print('You Have Chosed days Unite')
    print(f'You Have leaved For {days:,}')
    
else :
    print('Wrong Unite put The Right One!')





        


