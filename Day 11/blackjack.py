import random
import os
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score == 0:
        print(art.draw)
        return "It's a draw"
    elif user_score == 0:
        print(art.win)
        return "You win with a Blackjack"
    elif computer_score == 0:
        print(art.loose)
        return "Computer wins with a Blackjack"
    elif user_score>21:
        print(art.loose)
        return "You went over. Computer wins"
    elif computer_score>21:
        print(art.win)
        return "Computer went over. You win"
    elif user_score>computer_score:
        print(art.win)
        return "You win"
    else:
        print(art.loose)
        return "Computer wins"
def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards : {user_cards}, current score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score==0 or computer_score ==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=='y' and not is_game_over:
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        
    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ").lower() == 'y':
    os.system('cls')
    play_game()