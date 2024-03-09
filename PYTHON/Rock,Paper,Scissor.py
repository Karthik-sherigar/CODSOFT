import random
Rock="""

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

Paper="""

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock,Paper,Scissors]     
score = 0
no = 1
inc = 1
while(no<=inc):
    print("--------------------")
    user_choice = int(input("Enter your choice:\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
   

    if user_choice >= 3 or user_choice < 0:
        print("...You Entered Invalid Choice. You Will Lose...")
    else:
        print("--------------------")
        print("User Choice:")
        print(game_images[user_choice])
        computer_choice = random.randint(0,2)
        print("Computer Choice:\n")
        print(game_images[computer_choice])
        print("--------------------")
        if(computer_choice==user_choice):
            print(".....Tie.....")
            print("Score:",score)
            print("--------------------")
        elif (computer_choice == 0 and user_choice== 2):
            print(".....You Lose.....")
            score = score-10
            
            print("Score:",score)
            print("--------------------")
        elif (user_choice == 0 and computer_choice == 2):
            print(".....You Win.....")
            score = score+10
            print("Score:",score)
            print("--------------------")
        elif (computer_choice>user_choice):
            print(".....You Lose.....")
            score = score-10
            print("Score:",score)
            print("--------------------")
        elif (user_choice>computer_choice):
            print(".....You Win.....")
            score = score+10
            print("Score:",score)
    
    print("One more Match ?\n1 for Yes\n0 for No")
    ch = int (input())
    if ch == 1:
        inc = inc+1
        
    elif ch == 0:
        break
    else:
        print("...You Entered Invalid Choice...")
        break

print("Your Total Score:")
print(score)
print("--------------------")