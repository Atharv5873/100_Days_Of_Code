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
def jump(): 
    turn_left()
    if not wall_in_front():
            move()
    while wall_on_right():
        if wall_in_front():
            turn_left()
        move()
    move_right() 
    if wall_in_front():
        move_right()
    else:
        move_right()
        if wall_in_front():
            turn_left()
        move()
        
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
