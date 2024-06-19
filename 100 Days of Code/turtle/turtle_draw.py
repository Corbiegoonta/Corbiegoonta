from turtle import Turtle, Screen
import random
import colorgram

class TDraw():

    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()
        pass

    def square(self, size):
        for i in range(4):
            self.turtle.forward(size)
            self.turtle.right(90)
        pass
        

    def draw_polygon(self,length):
        for i in range(3, 11):
            angle = 360/i
            self.random_colour()
            for j in range(i):
                self.turtle.forward(length)
                self.turtle.right(angle)
        self.screen.exitonclick()
        pass
    
    def random_colour(self):
        self.screen.colormode(255)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colour = self.turtle.pencolor(r,g,b)
        return colour
    
    def random_walk(self, step, distance, line_width, speed):
        self.screen.screensize((distance*step+10),(distance*step+10))
        self.turtle.pensize(line_width)
        self.turtle.speed(speed)
        for i in range(distance):
            self.random_colour()
            direction = (0, 90, 180, 270)
            self.turtle.setheading(random.choice(direction))
            self.turtle.forward(step)
        self.screen.exitonclick()
        pass
    
    def draw_spirograph(self, radius, circle_number):
        self.turtle.speed("fastest")
        for i in range(circle_number):
            self.random_colour()
            self.turtle.setheading(i*360/circle_number)
            self.turtle.circle(radius)
        self.screen.exitonclick()
        pass

    def dashed_line(self, line, space, length):
        self.screen.screensize((length*2*(line+space)+10),(length*2*(line+space)+20))
        for i in range(length):
            self.turtle.forward(line)
            self.turtle.pu()
            self.turtle.forward(space)
            self.turtle.pd()
        self.screen.exitonclick()

    def create_dot_art(self):
        colours = colorgram.extract(rf'C:\Users\nickc\OneDrive\Desktop\Code\Personal Projects\100 Days of Code\turtle\image.jpg', 34)

        colour_numbers = []

        for colour in colours:
            l = []
            l.append(colour.rgb.r)
            l.append(colour.rgb.g)
            l.append(colour.rgb.b)
            colour_numbers.append(tuple(l))

        print(colour_numbers)

        colour_list = [(235, 234, 233), (236, 233, 235), (233, 235, 237), (225, 233, 229), (225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128), (205, 91, 106), (151, 212, 174), (146, 207, 222), (137, 180, 45), (28, 157, 171), (83, 73, 40), (9, 79, 115), (227, 181, 160), (95, 102, 165), (220, 174, 186), (181, 189, 208), (91, 49, 46), (32, 56, 56), (45, 70, 70)]

        colour_list_ww = [(225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128), (205, 91, 106), (151, 212, 174), (146, 207, 222), (137, 180, 45), (28, 157, 171), (83, 73, 40), (9, 79, 115), (227, 181, 160), (95, 102, 165), (220, 174, 186), (181, 189, 208), (91, 49, 46), (32, 56, 56), (45, 70, 70)]

        self.screen.colormode(255)
        self.turtle.speed(0)
        self.turtle.ht()
        self.turtle.pu()
        startx = -250
        starty = -250
        rows = 10
        dot_radius = 40
        dot_distance = 100
        canvas_size = rows*dot_distance*2*dot_radius
        self.screen.screensize(canvas_size, canvas_size)
        self.turtle.setpos(startx, starty)
        for i in range(rows):
            for j in range(9):
                self.turtle.goto(startx+i*dot_distance, j*dot_distance)
                self.turtle.dot(dot_radius, random.choice(colour_list))
        self.screen.exitonclick()

    def eas_forward(self):
        self.turtle.forward(10)
        pass

    def eas_backwards(self):
        # self.turtle.right(180)
        self.turtle.forward(-10)
        pass

    def eas_cc(self):
        self.turtle.left(10)
        pass
    
    def eas_c(self):
        self.turtle.right(10)
        pass
    
    def eas_clear(self):
        self.turtle.home()
        self.turtle.clear()
        pass

    def eas_undo(self):
        self.turtle.undo()
        pass

    def etch_a_sketch(self):
        # forward = None
        # backwards = None
        # counter_clockwise = None
        # clockwise = None
        # clear = None
        # undo = None
        fun = None 
        key = None

        self.screen.listen()
        self.screen.onkeypress(self.eas_forward, "w")
        self.screen.onkeypress(self.eas_backwards, "s")
        self.screen.onkeypress(self.eas_cc, "a")
        self.screen.onkeypress(self.eas_c, "d")
        self.screen.onkeypress(self.eas_clear, "space")
        self.screen.mainloop()
        pass

    def turtle_race(self, width, height, number_of_turtles):
        self.screen.setup(width=width, height=height)
        input_check = True
        while input_check is True:
            try:
                bet = int(self.screen.textinput(title="Turtle Bet", prompt= f"Which turtle do you want to bet on out of the {number_of_turtles} turtles in the race?\n"))
                if bet >= 1 or bet <= number_of_turtles:
                    input_check = False
            except Exception as e:
                print(e)
                print(f"Sorry this input is invalid. Please choose a number between 1 and {number_of_turtles}.")
        starting_x = (width / 20) - (width / 2)
        starting_y = (height / 2) - (height / 20)
        y_increment = height * (18 / 20) / (number_of_turtles - 1)
        self.turtle.speed(0)
        self.turtle.penup()
        count = 0
        for number in range(number_of_turtles):
            self.turtle.shape("turtle")
            self.screen.colormode(255)
            self.turtle.goto(starting_x, starting_y)
            self.turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
            if count < (number_of_turtles - 1):
                self.turtle.clone()
                starting_y -= y_increment
                count += 1
        turtle_list = self.screen.turtles()
        x_coordinate = starting_x
        while x_coordinate < ((width / 2) - (width /20)):
            for racing_turtle in turtle_list:
                racing_turtle.fd(random.randint(1, 10))
                if racing_turtle.xcor() > x_coordinate:
                    x_coordinate = racing_turtle.xcor()
        final_positions = []
        position_count = []
        position_counter = 0
        for turtle in turtle_list:
            final_positions.append(turtle.xcor())
        winning_x_cor = max(final_positions)
        winners = []
        for cor in final_positions:
            if cor == winning_x_cor:
                if position_counter == 0:
                    winners.append(number_of_turtles)
                else:
                    winners.append(position_counter)
            position_counter += 1
        print("The winner is turtle number: ")
        print(*winners)
        if bet in winners:
            print("Your bet was correct. You win!")
        else:
            print("Sorry, you bet incorrectly. You lose.")

        self.screen.exitonclick()

        pass

    

    def exit(self):
        self.screen.exitonclick()
        pass

TDraw().turtle_race(1000, 800, 5)
