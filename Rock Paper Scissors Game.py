import random

rock ='''

       __________

 _____'      ______)

          (__________)

          (__________)

           (________)
  _____
        ,___ (_____)

'''

paper ='''

      __________

 _____'     ______)______

                 __________)

                   __________)

                    ________)
  _____
        ,_________________)

'''
scissors = '''

       __________

 _____'     ______)______

                 __________)

                   __________)

           (________)
  _____
        ,___ (_____)

'''
game_images=[rock,paper,scissors]

user_choice=int(input("enter the choice:Type 0 for rock,1 for paper,2 for scissors"))

if user_choice>=3 or user_choice<0:
    print("You entered invalid number, You lose")

else:
    print(game_images[user_choice])

    computer_choice=random.randint(0,2)

    print("computer chose:")

    print(computer_choice)

    print(game_images[computer_choice])

    if computer_choice==user_choice:

        print("It's a draw")

    elif computer_choice==0 and user_choice==2:

        print("You Lose")

    elif user_choice==2 and computer_choice==0:

        print("You Win")

    elif computer_choice>user_choice:

        print("You Lose")

    elif user_choice>computer_choice:

        print("You Win")
