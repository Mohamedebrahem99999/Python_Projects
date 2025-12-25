import random
from rockpapersissors_ascii import ascii_list

def ascii_print(c_choice,u_choice,c_score,u_score):
    """prints the proper ascii art, the players choices and the scores of the players"""

    print()
    print(f"You chose {u_choice}")
    print(f"computer chose {c_choice}")
    print("="*40)
    print(ascii_list[u_choice])
    print(ascii_list[c_choice])
    print("=" * 40)
    print(f"===== YOUR SCORE = {u_score} =======")
    print(f"===== COMPUTER SCORE = {c_score} =======")

    if  u_score >= 15 and u_score > c_score:
         print("--- YOU WIN! 🎉 ---")
    elif c_score >= 15 and u_score < c_score:
        print("--- COMPUTER WINS! 🤖 ---")
    else:
        print("The game continues")

def main():
    beat_rules = {"rock" :"scissors" ,"paper" : "rock", "scissors":"paper"}

    user_score = 0
    computer_score = 0

    print("Welcome to the rock, Paper, Scissors game")
    start = input("Press enter to start or type (help) for the rules: ").lower().strip()
    while start and start != "help":
        print("Invalid choice")
        start = input("please make sure to press enter of type (help) to know the rules")
    if start and start == "help":

        print("""        ********* RULES *********
      1) You choose and the computer chooses
      2) Rock smashes scissors -> Rock wins
      3) Scissors cut paper -> Scissors win
      4) Paper covers Rock -> Paper wins 
      5) The game is n number of rounds 
      The player whose score reaches or exceeds 15 wins
      If both players reached the 15 points, there will be penalities""")

    n = 1
    while (15 > computer_score and 15 > user_score and not (user_score == computer_score == 15)
        or computer_score == user_score and computer_score >= 15):

        print(f"This is round {n}")

        computer_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("type (rock, paper or scissors) : ").lower().strip()
        while user_choice !="rock" and user_choice!="paper" and user_choice != "scissors":
            print("Invalid choice")
            user_choice = input("please make sure to type (rock, paper or scissors) : ").lower().strip()

        print()
        if user_choice == computer_choice:
            print("Draw")
            computer_score += 5
            user_score += 5
            ascii_print(computer_choice,user_choice,computer_score,user_score)

        elif beat_rules[user_choice] != computer_choice:
            print("Computer wins")
            computer_score += 5
            ascii_print(computer_choice,user_choice,computer_score,user_score)

        else:
            print("User wins")
            user_score += 5
            ascii_print(computer_choice, user_choice,computer_score,user_score)
        n+=1

    return None

while True:
    main()
    again = input("Would you like to play again? (y/n): ").lower().strip()
    while again != "y" and again != "n":
        print("Invalid choice")
        again = input("Please be sure to input (y) letter or (n) letter without any additions: ").lower().strip()
    if again != 'y':
        print("Thanks for playing!")
        break
