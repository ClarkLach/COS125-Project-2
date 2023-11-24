# File: LaChance_p2.py
# Author: Clark LaChance
# Date: 8 Dec 2022
# Section: 1 # E-mail: clark.lachance@maine.edu
# Description:
# Generates pseudo-random Mondrian style artworks.
# Collaboration:
# I did not collaborate with any of my peers on this assignment.

from graphics import *
from random import randint, random

WINDOW_X = 800 # Window dimensions
WINDOW_Y = 800
window = GraphWin("Mondrian Style Art", WINDOW_X, WINDOW_Y)

def EasyDimensions(rect): # Dedicated function for getting both points and the x and y coordinates of a rectangle.
    rectP1 = rect.getP1() # Lots of variables, but much easier to work with compared to storing tuples of coordinates and having to index every time.
    rectP2 = rect.getP2()
    rectP1X = rectP1.getX()
    rectP2X = rectP2.getX()
    rectP1Y = rectP1.getY()
    rectP2Y = rectP2.getY()

    if rectP1X > rectP2X: # Sometimes a rectangle will actually be drawn backwards, this is a fix so that generating random values within range still works.
        rectP1X, rectP2X = rectP2X, rectP1X # Swaps Point 1 and Point 2 coordinates if they are backwards.
    if rectP1Y > rectP2Y:
        rectP1Y, rectP2Y = rectP2Y, rectP1Y

    width = rectP2X - rectP1X
    height = rectP2Y - rectP1Y
    
    return rectP1X, rectP1Y, rectP2X, rectP2Y, rectP1, rectP2, width, height


def FillRect(rect): # Chooses a random color for final rectangles.
    r = random()
    if r < 0.09:
        rect.setFill("yellow")
    elif 0.09 <= r < 0.15:
        rect.setFill("blue")
    elif 0.15 <= r < 0.25:
        rect.setFill("red")
    elif 0.25 <= r:
        rect.setFill("white")


def CheckSize(rect): # Checks if rectangle should be split, and calls appropriate split function if needed.
    rectP1X, rectP1Y, rectP2X, rectP2Y, rectP1, rectP2, width, height = EasyDimensions(rect)

    rand_x, rand_y = width, height # Arbitrary assignment, they just need to be at least as big as width/height
    if width*1.5 > 90: # in the event that these assignments are not made.
        rand_x = randint(90, round(width*1.5))
    if height*1.5 > 90:
        rand_y = randint(90, round(height*1.5))
    
    if ((WINDOW_X/2) < (width)) and ((WINDOW_Y/2) < (height)): # Bigger than half the window
        SplitBoth(rect)
    elif (rand_x < width) and (rand_y < height): # Random choice if splits are called or not.
        SplitBoth(rect)
    elif (rand_x < width):
        Split_X(rect)
    elif (rand_y < height):
        Split_Y(rect)
    else:
        FillRect(rect) # Color function is used only here to ensure that only final rectangles are filled.


def Split_X(old_rect): # Splits region into right and left rectangles.
    rectP1X, rectP1Y, rectP2X, rectP2Y, rectP1, rectP2, width, height = EasyDimensions(old_rect)

    lower_bound = round(width * 0.31) + rectP1X # values provided in assignment
    upper_bound = round(width * 0.68) + rectP1X
    rand_x = randint(lower_bound, upper_bound)
    
    right = Rectangle(Point(rand_x, rectP1Y), rectP2)
    left = Rectangle(rectP1, Point(rand_x, rectP2Y))

    for region in [left, right]:
        region.draw(window)
        CheckSize(region)


def Split_Y(old_rect): # Splits region into top and bottle rectangles
    rectP1X, rectP1Y, rectP2X, rectP2Y, rectP1, rectP2, width, height = EasyDimensions(old_rect)

    lower_bound = round(height * 0.31) + rectP1Y # values provided in assignment
    upper_bound = round(height * 0.68) + rectP1Y
    rand_y = randint(lower_bound, upper_bound)
    
    top = Rectangle(rectP1, Point(rectP2X, rand_y))
    bottom = Rectangle(Point(rectP1X, rand_y), rectP2)

    for region in [top, bottom]:
        region.draw(window)
        CheckSize(region)


def SplitBoth(old_rect): # Splits rectangles into four regions.
    rectP1X, rectP1Y, rectP2X, rectP2Y, rectP1, rectP2, width, height = EasyDimensions(old_rect)

    lower_bound_x = round(width * 0.31) + rectP1X # values provided in assignment
    upper_bound_x = round(width * 0.68) + rectP1X
    rand_x = randint(lower_bound_x, upper_bound_x)

    lower_bound_y = round(height * 0.31) + rectP1Y # values provided in assignment
    upper_bound_y = round(height * 0.68) + rectP1Y
    rand_y = randint(lower_bound_y, upper_bound_y)
    
    top_left = Rectangle(rectP1, Point(rand_x, rand_y))
    top_right = Rectangle(Point(rand_x, rectP1Y), Point(rectP2X, rand_y))
    bottom_left = Rectangle(Point(rectP1X, rand_y), Point(rand_x, rectP2Y))
    bottom_right = Rectangle(Point(rand_x, rand_y), rectP2)

    for region in [top_left, top_right, bottom_left, bottom_right]:
        region.draw(window)
        CheckSize(region)


def main():
    base_rect = Rectangle(Point(0,0), Point(WINDOW_X, WINDOW_Y)) # Base rectangle is just the size of the full window.

    SplitBoth(base_rect) # Could actually call CheckSize() or this, but initial check isn't required because it will always be split.

    window.getMouse()
    window.close()

main()