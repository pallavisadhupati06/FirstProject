import random
comp=random.randint(1,20)
while(True):
  choice=int(input("Enter your choice of number,Please!!!"))
  if(choice==comp):
    print("You have selected the right one!!!,Congratulations")
    break
  elif(choice>comp):
    print("Your choice is Greater than choosen,select lower one")
  elif(choice<comp):
    print("Your choice is Lower than choosen,select greater one")
print("Game Ended\nIf you want to play again,Please restart")