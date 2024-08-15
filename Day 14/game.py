import random
from art import logo, vs
from game_data import data
import os
key2 = random.randint(0, len(data))
score=0
first_time=True
while True:
    os.system('cls')
    print(logo)
    if not first_time:
        print(f"You're right! Current score: {score}.")
    else:
        first_time=False
    key1 = key2
    key2 = random.randint(0, len(data))
    while key2 == key1:
        key2 = random.randint(0, len(data))

    a=f"{data[key1]['name']}, a {data[key1]['description']}, from {data[key1]['country']}"
    b=f"{data[key2]['name']}, a {data[key2]['description']}, from {data[key2]['country']}"
    a1=data[key1]['follower_count']
    b1=data[key2]['follower_count']
    print(f"Compare A: {a}")
    print(vs)
    print(f"Compare B: {b}\n")
    bigger = 'a' if a1 > b1 else 'b'
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == bigger:
        score +=1
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break;



