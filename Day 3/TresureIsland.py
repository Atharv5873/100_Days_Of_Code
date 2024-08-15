print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction=input("Type 'left' or 'right'\n").lower()
if direction=="right":
    print("You fell into a hole. Game Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    action=input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if action=="swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door=input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door=="red":
            print("It's a room full of fire. Game Over.")
        elif door=="blue":
            print("You enter a room full of beasts. Game Over.")
        else:
            print("You see a treasure chest. You've won!")
