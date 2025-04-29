from turtle import Turtle
STARTING_POSITION =[(0,0) , (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        for positions in STARTING_POSITION :
            self.add_segments(positions)

    def add_segments(self,positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def extend_segments(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]

