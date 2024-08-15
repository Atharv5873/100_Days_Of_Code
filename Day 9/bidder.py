from art import logo
from art import sold
import os
print(logo)
print("Welcome to the Secret Auction Program")
bidder={}
name=input("What is your name?: ")
bid=input("What is your bid?: $")
bidder[name]=bid
flag=True
while(flag):
    other=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    os.system('cls')
    if(other.lower()=='yes'):
        name=input("What is your name?: ")
        bid=input("What is your bid?: $")
        bidder[name]=bid
    else:
        flag=False
winner=""
for key in bidder:
    if(winner==""):
        winner=key
    else:
        if(bidder[winner]<bidder[key]):
            winner=key
os.system('cls')
print(sold)
print(f"The winner is {winner} with a bid of ${bidder[winner]}")