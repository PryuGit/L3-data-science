#guess the number
import random

ans=random.randint(1,100)

for x in range(1,6):
    num=int(input('Guess a number(1-100):'))
    if(num<ans):
        print("Go Higher")
    elif(num>ans):
        print("Go Lower")
    elif(num==ans):
        print("Correct")
        break
else:
    print("Game Over")
    print(f"The number was ",ans)
