import re
import random
import time
import os
h_s = ""

def exceed(score):
    """checks if score exceeds 21"""
    if score > 21:
        return True
    else:
        return None

def compare (turn = "",user_cards = 0,computer_cards = 0):
    """checks for exceed and for BlackJack """
    if user_cards == 21 and computer_cards == 21:
        return f"\nDraw\nTotal score you have is {sum(user)} of {user}\ncomputer's second card is {computer[1]}\n total score computer has = {sum(computer)} of {computer}"
    elif computer_cards == 21 and user_cards != 21 and (h_s == "stand" or computer[0] == 11):
        return f"Computer's total score is {sum(computer)} of {computer}\ncomputer got BlackJack\nComputer wins"
    elif computer_cards != 21 and user_cards == 21:
        return f"Your total score is {sum(user)} of {user}\nYou got BlackJack\nYou win\nComputer Total score = {sum(computer)} of {computer}"

    if exceed(user_cards):
        return f"You lose\nYou have total score of {sum(user)} of {user}\nWhich exceeds 21\nWhile computer total score is {sum(computer)} of {computer}"

    elif exceed(computer_cards):
        return f"Computer loses\nYou wins\nComputer have total score of {sum(computer)} of {computer}\nWhile user total score is {sum(user)} of {user}"
    else:
        return None
    #there must be a condition
def final_comparison (user_cards,computer_cards):
    """compares score of computer and user and return the greater if found else draw"""
    if computer_cards < user_cards < 21:
        return f"You win\nTotal score you have = {sum(user)} of {user}\nTotal score computer has = {sum(computer)} of {computer}"
    elif user_cards < computer_cards < 21:
        return f"You lose\nTotal score you have = {sum(user)} of {user}\nTotal score computer has = {sum(computer)} of {computer}"
    else:
        return f"Draw\nTotal score you have = {sum(user)} of {user}\nTotal score computer has = {sum(computer)} of {computer}"

deck = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":10,"boy":10,"queen":10}

user = []
computer = []

def card_distribution(t,lst):
    """function responsible for distribution of cards"""
    choice = random.choice(list(deck.keys()))
    if choice == 1: #Aices case
        if sum(lst) + 11 <= 21:
            deck[1] = 11
        else:
            deck[1] = 1
    lst.append(deck[choice])
    return f"{t}'ve got {choice} with {deck[choice]} points"

def game():
    """the main function"""
    os.system("cls" if os.name == "nt" else "clear")
    print("""""")
    for _ in range(2):
        print(card_distribution("You",user))
    print(f"Total points you have = {sum(user)} of {user}\n")

    for _ in range(2):
        if len(computer) < 1:
            print(card_distribution("computer",computer))
            print()
        else:
            card_distribution("computer",computer)
    if computer[0] == 11: #checking for computer blackjack -->the function also checks for user blackjack automatically
        print("checking a computer blackjack...")
        time.sleep(1)
        print("Checking second card.....")
        time.sleep(1)
        if compare(user_cards = sum(user),computer_cards = sum(computer)) and sum(computer) == 21:
            return compare(user_cards = sum(user),computer_cards = sum(computer))
        else:
            print("Computer got no BlackJack")

    if compare(user_cards=sum(user), computer_cards=sum(computer)): #checks for user blackjack --> the function also checks for computer blackjack automatically
        return compare(user_cards=sum(user), computer_cards=sum(computer))

    def hit_stand (choice): return "".join(re.findall(r"[a-z]+",choice.lower()+"\n"))
    global h_s
    h_s = hit_stand(input("Choose on of the following:\n1)hit\n2)stand\n"))
    while h_s != "hit" and h_s != "stand":
        print("Please make sure you have input either hit or stand ")
        h_s = hit_stand(input("Choose on of the following:\n1)hit\n2)stand\n"))
    while h_s == "hit":
        print()
        print(card_distribution("You",user))
        print()
        if compare("You",sum(user),sum(computer)):
            return compare("You", sum(user), sum(computer))
        print(f"Total points you have = {sum(user)}\n of {user}")
        h_s = hit_stand(input("Choose on of the following:\n1)hit\n2)stand "))

    print(f"second card the computer has is {computer[1]}")
    if compare("computer", sum(user), sum(computer)):
        print(f"Total score computer has = {sum(computer)} of {computer}")
        return compare("computer", sum(user), sum(computer))

    while (h_s == "stand") and (sum(computer) < 17):
        print(f"Total points the computer has = {sum(computer)} of {computer}\n")
        print(card_distribution("computer", computer))
        if compare("computer",sum(user),sum(computer)):
            return compare("computer", sum(user), sum(computer))

    else:
        if compare(user_cards=sum(user), computer_cards=sum(computer)):
            return compare(user_cards=sum(user), computer_cards=sum(computer))
        return final_comparison(sum(user),sum(computer))
print(game())