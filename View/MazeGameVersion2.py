# Part 1: Setting Up The Maze
from turtle import *
import tkinter as tk


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


# Create Pen
class Pen(RawTurtle):
    def __init__(self, tk_canvas):
        super().__init__(tk_canvas)
        self.tk_canvas = tk_canvas
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(RawTurtle):
    def __init__(self, tk_canvas):
        super().__init__(tk_canvas)
        self.tk_canvas = tk_canvas
        #self.hideturtle()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def check_if_space_has_a_wall(self, move_to_x, move_to_y):
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_up(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        self.check_if_space_has_a_wall(move_to_x, move_to_y)

    def go_down(self, event):
        # Calculate the spot to move to
        print("this was triggered")
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        self.check_if_space_has_a_wall(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.check_if_space_has_a_wall(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.check_if_space_has_a_wall(move_to_x, move_to_y)





class GameArea(RawTurtle):
    def __init__(self, tk_canvas):
        super().__init__(tk_canvas)
        self.tk_canvas = tk_canvas
        self.hideturtle()
        screen = self.getscreen()
        screen.bgcolor('black')
        screen.tracer(0)

        # Create levels list
        levels = [""]

        # Define first level
        level_1 = [
            "XP XXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X       XX  XXXXXX  XXXXX",
            "X       XX  XXX        XX",
            "XXXXXX  XX  XXX        XX",
            "XXXXXX  XX  XXXXXX  XXXXX",
            "XXXXXX  XX    XXXX  XXXXX",
            "X  XXX        XXXX  XXXXX",
            "X  XXX  XXXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "X                XXXXXXXX",
            "XXXXXXXXXXXX     XXXXX  X",
            "XXXXXXXXXXXXXXX  XXXXX  X",
            "XXX  XXXXXXXXXX         X",
            "XXX                     X",
            "XXX         XXXXXXXXXXXXX",
            "XXXXXXXXXX  XXXXXXXXXXXXX",
            "XXXXXXXXXX              X",
            "XX   XXXXX              X",
            "XX   XXXXXXXXXXXXX  XXXXX",
            "XX    XXXXXXXXXXXX  XXXXX",
            "XX          XXXX        X",
            "XXXX                    X",
            "XXXXXXXXXXXXXXXXXXXXX  XX"
        ]

        # Add maze to mazes list
        levels.append(level_1)

        # Set up the level
        self.setup_maze(levels[1])
        screen.update()

    # Create Level Setup Function
    def setup_maze(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                # Get the character at each x,y coordinate
                # NOTE the order of y and x in the next line
                character = level[y][x]
                # Calculate the screen x, y coordinates
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                # Check if it is an X (representing a wall)
                if character == "X":

                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    # Add coordinates to wall list, tuple containing coordinates
                    walls.append((screen_x, screen_y))

                # Check if it is a P (representing the player)
                if character == "P":
                    player.goto(screen_x, screen_y)


class MazeGameCanvas():
    def __init__(self, win):
        self.canvas = tk.Canvas(win, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.pack()






# Turn off screen updates
# wn.tracer(0)

# Main Game Loop
# while True:
# Update screen
# wn.update()

win = tk.Tk()
win.title("Maze Game")
play_button = tk.Button(win, text="Start Game", width=25)
play_button.pack()
maze_game = MazeGameCanvas(win)
# Create class instances
pen = Pen(maze_game.canvas)
player = Player(maze_game.canvas)



# Create wall coordinate list
walls = []
maze_game_area = GameArea(maze_game.canvas)

# Keyboard Binding

win.bind('<Button-1>', player.go_down)
win.bind('<KeyRelease>', player.go_up())

# listen()
# onkey(player.go_left, "Left")
# onkey(player.go_right, "Right")
# onkey(player.go_up, "Up")
# onkey(player.go_down, "Down")
win.mainloop()
# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.title("A Maze Game")
# wn.
# wn.setup(700, 700)


# m.mainloop()
