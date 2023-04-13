import random
def gameWin(comp, you):
    # If comp and you are same declare a tie
    if comp == you:
        return None
        # When comp choses rock
    elif comp =='r':
            if you=='s':
                return False
            elif you=="p":
                return True
        # When comp choses Scissor
    elif comp =='s':
            if you=='p':
                return False
            elif you=="r":
                return True
        # When Comp Choses Paper
    elif comp =='p':
            if you=='r':
                return False
            elif you=="s":
                return True
print("Comp Turn : Rock(r) , Paper(p), Scissor(s)")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 'r'
elif randNo ==2:
    comp = 'p'
elif randNo==3:
    comp='s'
you = input("Your Turn : Rock(r) , Paper(p), Scissor(s)")

a = gameWin(comp, you)
print(f"Comp has choosen {comp}")
print(f"you have choosen {you}")
if a ==None:
    print("The game was tie")
elif a:
    print("You win!")
else: 
    print("You loose")
