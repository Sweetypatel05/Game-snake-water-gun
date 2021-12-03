import random
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif  you=='g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you =='w':
            return True
        elif you == ' s':
            return False

print("comp Turn : Snake (s) water(w) gun (g)?")
randNo = random.randint(1,3)
if randNo ==1 :
    comp ='s'
elif randNo ==2:
    comp = 'w'
elif randNo == 3:
        comp = 'g'

you = input("your turn : snake(s) water(w) gun (g)?")
a =gamewin(comp,you)  
print(f"computer: {comp}")
print(f"you :{you}")
  
if a  == None:
    print("the game is tie!")  
elif a :
    print("you win")
else:
    print("you lose!!")        


            
