'''
# defining turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# slide please
def slide(count):
    while count > 0:
        move()
        count -= 1

# defining jump
def jump():
     count = 0
     while wall_in_front():
            turn_left()
            move()
            turn_right()
            count += 1
     move()
     turn_right()
     slide(count)
     turn_left()

# front_is_clear() or wall_in_front(), at_goal()
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
'''