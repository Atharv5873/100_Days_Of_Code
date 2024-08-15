import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("Let's Start")

chosen=random.choice(hangman_words.word_list)
answer=""
answer="_"*len(chosen)
answer_list=list(answer)
print(answer)
lives=6
win = False
letters_used=""


while lives>0 and not win:
    print(f"\n****************************************{lives} LIVES LEFT****************************************")
    guess=input("\nGuess a Letter: ").lower()
    if len(guess)>1:
        print("Enter only one letter")
    else:
        if guess not in letters_used:
            letters_used+=guess
            counter=0
            counter2=0
            for i in chosen:
                if i==guess:
                    answer_list[counter]=i 
                    counter2+=1
                counter+=1
            counter=0
            if counter2==0:
                lives-=1
                print(f"You guessed {guess}, thats not in the word.")
                print("You Loose One Life")
                print("Lives Left: ",lives)
            counter2=0
            if lives==6:
                print(hangman_art.stages[6])
            elif lives==5:
                print(hangman_art.stages[5])
            elif lives==4:
                print(hangman_art.stages[4])
            elif lives==3:
                print(hangman_art.stages[3])
            elif lives==2:
                print(hangman_art.stages[2])
            elif lives==1:
                print(hangman_art.stages[1])
            else:
                print(hangman_art.stages[0])
                print(f"\n****************************************IT WAS {chosen}! YOU LOOSE****************************************")
                break
            for i in answer_list:
                print(i,end="")
            if answer_list == list(chosen):
                win=True
        else:
            print("You already guessed that letter")
if lives>0:
    print("\n****************************************YOU WIN****************************************")