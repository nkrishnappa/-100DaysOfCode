from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) -1, 0, -1):
            pos = self.segments[segment_number - 1].position()
            self.segments[segment_number].setposition(pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

'''
class Snake:
    def __init__(self):
        self.position = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        for position in self.position:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) -1, 0, -1):
            pos = self.segments[segment_number - 1].position()
            self.segments[segment_number].setposition(pos)
        self.segments[0].forward(20)
        self.segments[0].left(90)
'''