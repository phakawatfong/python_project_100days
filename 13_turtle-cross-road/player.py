from turtle import Turtle


MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.go_to_start()
        self.setheading(90)


    
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
