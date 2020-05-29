
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n1336516
#    Student name: Max O'Dell
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('blue')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    #goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    #write('    Put your legend here', align = 'left',
          #font=('Arial', 24, 'normal'))    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

# Follow the path as per the provided dataset
def follow_path(path):

    starttokendraw(startpos(path), path[0][2])  #passes the pixel coordinate returned by 'startpos' and the starting token number of the instructions generated by 'random_path' to the 'starttokendraw' function

    directions = [90, 0, 270, 180]  #stores the angles at which the turtle must move for North, East, South or West instructions, respectively

    tokencount = [0] * 5    #creates a list of five zeros to store the number of times each token appeared in the program (index positions match token numbers)
    tokencount[path[0][2]] += 1     #increases the count of the starting token by one (has to be incremented differently than the instructions post-start)
 
    step = 1    #stores the value of the instruction number the 'for' loop is processing
    hideturtle()    #hides the cursor from view

    for instructions in range(1, len(path)):    #main function for drawing tokens, navigating grid spaces and processing instructions. executes a number of times equal to the amount of instructions generated
        move = (path[step][1] * 100)    #actively calculates the number of pixels to be moved, multiplying the number of spaces to be moved by 100 (grid spaces are 100 x 100 pixels)
        token = path[step][2]
        penup()
        if path[step][0] == 'North':    #checks which direction the instruction requires the turtle to move and points it towards the corresponding angle in 'directions'
            setheading(directions[0])   
        elif path[step][0] == 'East':
            setheading(directions[1])    
        elif path[step][0] == 'South':
            setheading(directions[2])   
        elif path[step][0] == 'West':
            setheading(directions[3])
        forward(move)    #moves the turtle forward by the number of pixels calculated and stored in 'move'
        pendown()
        tokendraw(token)    #passes the token number being drawn in the instruction to the 'tokendraw' function to be drawn
        step += 1    #increments the value of the instruction being processed by 1 to step through the list one by one
        tokencount[token] += 1    #increments the count of the token found in the current instruction by 1

    totalcount = sum(tokencount)    #stores the total number of found tokens
    legend(tokencount, totalcount)    #calls the 'legend' function and passes both variables related to the count of tokens found
         
def startpos(path):     #determines the starting position of the turtle, returning pixel coordinates
    if path[0][1] == 'Top left':    #checks the starting position in the start instruction and returns the corresponding coordinate of the location
        return (50,650)
    if path[0][1] == 'Top right':
        return (650,650)
    if path[0][1] == 'Centre':
        return (350,350)
    if path[0][1] == 'Bottom left':
        return (50,50)
    if path[0][1] == 'Bottom right':
        return (650,50)

def starttokendraw(location, token):    #draws the correct starting token
    penup()
    goto(location)    #moves the turtle to the pixel coordinate calculated by 'startpos'
    pendown()
    tokendraw(token)    #draws the correct toke, determined by the index location of the start instruction generated

def legend(tokencount, totalcount):     #draws the legend elements and writes text
    penup()
    goto(750, 700)  #sets up the turtle attributes to prepare for the drawing of the legend
    pendown()
    width(5)
    setheading(0)
    color('blue')
    fillcolor('lightblue')
    begin_fill()
    for legend in range (0,2):  #draws the border in a more efficient manner
        forward(300)
        right(90)
        forward(700)
        right(90)
    end_fill()
    penup()
    color('black')  #resets the turtle attributes for the drawing of tokens
    width(1)

    goto(800,665)   #moves the turtle to the location of the legend title, and joins the number of all tokens found with standard text
    write(str(totalcount) + ' Car Badges Were Found!', align = 'left', font=('Arial', 12, 'bold'))  

    yval = 600  #stores the y-coordinate value of the first token to be drawn in the legend
    token = 0   #sets token 0 as the toke being drawn
    for legendtokens in range (0,5):    #draws all 5 tokens underneath the preceding one
        penup()
        goto(825,yval)    #moves the turtle to 825,yval, the value of which changes with every iteration of the loop
        pendown()
        tokendraw(token)    #draws the current token
        yval -= 125     #increments the y-coordinate of the next token by 125 pixels
        token += 1    #sets the token being drawn to the next in order 

    goto(890,592)
    pendown()
    write('Mercedes Benz (' + str(tokencount[0]) + ')', align = 'left', font=('Arial', 12, 'normal'))   #moves the turtle next to every token and writes its name, as well as how many times it appeared in brackets
    penup()
    goto(890,465)
    pendown()
    write('BMW (' + str(tokencount[1]) + ')', align = 'left', font=('Arial', 12, 'normal'))
    penup()
    goto(890,342)
    pendown()
    write('Nissan (' + str(tokencount[2]) + ')', align = 'left', font=('Arial', 12, 'normal'))
    penup()
    goto(890,220)
    pendown()
    write('Mini Cooper (' + str(tokencount[3]) + ')', align = 'left', font=('Arial', 12, 'normal'))
    penup()
    goto(890,80)
    pendown()
    write('Citroën (' + str(tokencount[4]) + ')', align = 'left', font=('Arial', 12, 'normal'))

def tokendraw(token):   #draws the token, receiving the argument from other functions corresponding to the token number to be drawn
    if token == 0:    #checks if the desired token is token 0 (Mercedes Benz)
        penup()     #if it is, draws token 0 (so on and so forth for the entire function)
        setheading(90)
        forward(50)
        pendown()
        fillcolor('black')
        begin_fill()
        setheading(180)
        circle(50)
        end_fill()
        setheading(270)
        penup()
        forward(5)
        pendown()
        fillcolor('lightgrey')
        begin_fill()
        setheading(180)
        circle(45)
        end_fill()
        setheading(270)
        forward(45)
        setheading(315)
        forward(45)
        setheading(135)
        penup()
        forward(45)
        pendown()
        setheading(225)
        forward(45)
        fillcolor('black')
        begin_fill()
        setheading(25)
        forward(35)
        setheading(335)
        forward(35)
        setheading(125)
        forward(43)
        setheading(100)
        forward(43)
        setheading(260)
        forward(43)
        setheading(235)
        forward(46)
        hideturtle()
        end_fill()
        color('black')
        penup()
        setheading(45)
        forward(49)            

    if token == 1:  #BMW
        penup()
        setheading(90)
        forward(50)
        pendown()
        color('black')
        fillcolor('skyblue')
        begin_fill()
        setheading(270)
        forward(50)
        setheading(180)
        forward(50)
        end_fill()
        setheading(0)
        forward(100)
        begin_fill()
        left(180)
        forward(50)
        left(90)
        forward(50)
        end_fill()
        color('black')
        setheading(90)
        penup()
        forward(7)
        pendown()
        width(15)
        right(90)
        circle(43)
        setheading(90)
        penup()
        forward(43)
        width(1)

    if token == 2:  #Nissan
        penup()
        setheading(90)
        forward(45)
        left(90)
        pendown()
        fillcolor('gainsboro')
        begin_fill()
        circle(45)
        end_fill()
        penup()
        left(90)
        forward(10)
        pendown()
        fillcolor('white')
        begin_fill()
        right(90)
        circle(35)
        end_fill()
        penup()
        left(90)
        forward(25)
        right(90)
        pendown()
        fillcolor('gainsboro')
        begin_fill()
        forward(49)
        left(90)
        forward(20)
        left(90)
        forward(98)
        left(90)
        forward(20)
        left(90)
        forward(49)
        end_fill()
        penup()
        left(90)
        forward(10)

    if token == 3:   #Mini Cooper
        fillcolor('silver')
        begin_fill()
        setheading(90)
        penup()
        forward(10)
        right(90)
        pendown()
        forward(50)
        right(135)
        forward(28)
        right(45)
        forward(60)
        right(45)
        forward(28)
        setheading(0)
        forward(49.6)
        end_fill()
        penup()
        right(90)
        forward(10)
        dot(50, 'silver')
        dot(45, 'black')
        dot(43, 'silver')
        dot(40, 'black')
        color('black')

    if token == 4:   #Citroën
        penup()
        setheading(90)
        forward(40)
        pendown()
        fillcolor('silver')
        begin_fill()
        setheading(330)
        forward(58)
        right(60)
        forward(20)
        setheading(150)
        forward(58)
        left(60)
        forward(58)
        setheading(90)
        forward(20)
        right(60)
        forward(58)
        end_fill()
        penup()
        setheading(270)
        forward(30)
        pendown()
        begin_fill()
        setheading(330)
        forward(58)
        right(60)
        forward(20)
        setheading(150)
        forward(58)
        left(60)
        forward(58)
        setheading(90)
        forward(20)
        right(60)
        forward(58)
        end_fill()
        penup()
        setheading(270)
        forward(10)
        
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("The Car Badge Treasure Hunt! (Mercedes Benz, BMW, Mini Cooper, Nissan and Citroën)")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
#follow_path(fixed_path_99) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment


# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
