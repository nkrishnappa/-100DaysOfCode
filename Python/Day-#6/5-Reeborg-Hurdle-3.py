'''
# defining turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# defining jump
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# front_is_clear() or wall_in_front(), at_goal()
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

'''