import random

def judge(computer, user_choice):
    if computer == user_choice:
        return f"""===congratulations! you won===
    The computer's coin toss is :{computer} """
    else:
        return f"""===Sorry you lost===
  The computer's coin toss result is {computer}"""

def main():
    print("Welcome to the Coin Guessing Game")
    print("==========************=================")
    print("Choose a method to toss the coin:")
    print("1.Using random.randint()")
    print("2.Using random.random()")

    """
    The rule in rand.randint(0,1) method is that:
    if the random number = 0, computer toss is tais and if the number is 1,computer toss is heads
    The rule in rand.random is that if the random number > .5,computer = tail
    and if number < .5, computer = heads
    """

    rand_method = input("Enter your choice (1 or 2):\n").strip()
    while rand_method not in ["1", "2"]:
        print("Invalid choice")
        rand_method = input("Enter your choice (1 or 2):\n").strip()

    user = input("Enter your Guess (h) for heads or(t) fortails)\n").lower().strip()
    while user not in ['h', 't']:
        print("Invalid choice")
        user = input("Enter your Guess (h) for heads or(t) fortails)\n").lower().strip()

    computer_toss = ""

    if rand_method == "1":
        computer = random.randint(0, 1)
        computer_toss = "h" if computer == 1 else "t"

    else:
        computer = random.random()
        computer_toss = "t" if computer > .5 else "h"

    print(judge(computer_toss, user))

if __name__ == "__main__":
    main()