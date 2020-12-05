"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc

 sources:
  https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
"""
import pygame
from readfile import readFile
from game import Game
from colors import WHITE, BLACK, GREEN, YELLOW, RED, GRAY, BLUE, LIGHT, LIGHT_ERROR

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 75
HEIGHT = 75
BOARD_SIZE = 7



# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(BOARD_SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(BOARD_SIZE):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[5][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
#(MARGIN + 50) + MARGIN
WINDOW_SIZE = [1000, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)

lightImg = pygame.image.load('lightbulb.png')
font = pygame.font.Font('freesansbold.ttf', 32)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rfile = readFile('boards.txt')
lines = rfile.read()
g = Game(lines)


# -------- Main Program Loop -----------
while not done:
  for event in pygame.event.get():  # User did something
    if event.type == pygame.QUIT:  # If user clicked close
      done = True  # Flag that we are done so we exit this loop
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # User clicks the mouse. Get the position
      pos = pygame.mouse.get_pos()
      # Change the x/y screen coordinates to grid coordinates
      column = pos[0] // (WIDTH + MARGIN)
      row = pos[1] // (HEIGHT + MARGIN)
      # Set that location to one
      if(g.board[row][column].color == WHITE):
        g.board[row][column].switchOn()
      
      print("Click ", pos, "Grid coordinates: ", row, column)

  # Set the screen background
  screen.fill(BLACK)

  # Draw the grid
  for row in range(BOARD_SIZE):
    for column in range(BOARD_SIZE):
      color = g.board[row][column].color
      
      pygame.draw.rect(screen, color,
                        [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

      if g.board[row][column].color == LIGHT:
        screen.blit(lightImg, [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                        
      if g.board[row][column].color == GREEN:
        text = font.render(str(g.board[row][column].value), True, BLACK, GREEN)
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = ([((MARGIN + WIDTH) * column + MARGIN) + WIDTH/2,
                        ((MARGIN + HEIGHT) * row + MARGIN) + HEIGHT/2])

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        screen.blit(text, textRect)


  # Limit to 60 frames per second
  clock.tick(60)

  # Go ahead and update the screen with what we've drawn.
  pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
