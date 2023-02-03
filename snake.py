# made by Jayavant

import turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 30
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment_position in POSITIONS:
            self.add_segment(segment_position)


    def add_segment(self, segment_position):
        t1 = turtle.Turtle("square")
        t1.color("red")
        t1.penup()
        t1.goto(segment_position)
        self.segments.append(t1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

        # new segment

    def move(self):
        for seg in range((len(self.segments) - 1), 0, -1):
            x_position = self.segments[seg - 1].xcor()
            y_position = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_position, y_position)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


