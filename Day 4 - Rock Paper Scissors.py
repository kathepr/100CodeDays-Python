import random

rock = """

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    """

paper = """

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

    """
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    
    """


game_images = [rock, paper, scissors]
index_total_game_images = len(game_images)-1

your_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)


if your_choice > index_total_game_images or your_choice < 0:
    print("\nYou wrote an invalid number\n")
else:
    print(f"\nYour Choice: {game_images[your_choice]}")
    print(f"Computer Choice: {game_images[computer_choice]}")

    if your_choice == computer_choice:
        print("\n This is a draw\n")
    elif your_choice == 0 and computer_choice == 2:
        print("\n You win!\n")
    elif your_choice == 1 and computer_choice == 0:
        print("\n You win!\n")
    elif your_choice == 2 and computer_choice == 1:
        print("\n You win!\n")
    else:
        print("\n You lose!\n")