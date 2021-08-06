'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# defining turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# defining jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# iterate the 6 times

# iterate the 6 times
for i in range(6):
    jump()
'''