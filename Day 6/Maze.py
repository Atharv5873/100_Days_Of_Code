def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_left():
    turn_left()
    move()
def move_right():
    turn_right()
    move()
while not at_goal():
    if right_is_clear():
        move_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
