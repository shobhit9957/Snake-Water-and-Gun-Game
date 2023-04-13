import random
def gameWin(comp, you):
    # If comp and you are same then declare a tie
    if comp == you:
        return None
    # If comp has chosen r
    elif comp == 'rock':
        if you == 'scissor':
            return False
        elif you =='paper':
            return True
    # If Comp has choosen p
    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you =='scissor':
            return True
    # If Comp has choosen s
    elif comp == 'scissor':
        if you == 'paper':
            return False
        elif you =='rock':
            return True
print("Comp Turn : Rock(r), Paper(p), Scissor(s)")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 'rock'
elif randNo ==2:
    comp = 'paper'
elif randNo ==3:
    comp = 'scissor'
you = input("Your Turn : Rock(r), Paper(p), Scissor(s)")
if you=='s':
    you = 'scissor'
elif you=='p':
    you = 'paper'
elif you=='r':
    you = 'rock'
a = gameWin(comp, you)
print(f"Computer has choosen {comp}")
print(f"You Have choosen {you}")
if a == None:
    print("Oops! The game was tie")
elif a:
    print("You win!")
else: 
    print("You lose")