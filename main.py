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
from colors import WHITE, BLACK, GREEN, YELLOW, RED, GRAY, BLUE, LIGHT, LIGHT_ERROR, LTYELLOW

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 75
HEIGHT = 75
BOARD_SIZE = 7

# This sets the margin between each cell
MARGIN = 5

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
#(MARGIN + 50) + MARGIN
WINDOW_SIZE_X = 1000
WINDOW_SIZE_Y = 800
WINDOW_SIZE = [WINDOW_SIZE_X, WINDOW_SIZE_Y]
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

def draw_board():
  for row in range(BOARD_SIZE):
    for column in range(BOARD_SIZE):
      color = g.board[row][column].color
      
      pygame.draw.rect(screen, color,
                        [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
  
      if g.get_color(row, column) in [LIGHT,LIGHT_ERROR]:
        screen.blit(lightImg, [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
      
      if g.get_color(row, column) == GREEN:
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

def draw_button():
  # Rect(left, top, width, height)
  pygame.draw.rect(screen, GREEN, [(WIDTH + MARGIN) * BOARD_SIZE + WIDTH, 5, 150, 75])
  text = font.render("VERIFY", True, BLACK, GREEN)
  textRect = text.get_rect()
  textRect.center = ([(WIDTH + MARGIN) * BOARD_SIZE + WIDTH * 2, HEIGHT/2 + MARGIN])
  screen.blit(text, textRect)

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
      
      # Button click
      if (((WIDTH + MARGIN) * BOARD_SIZE + WIDTH) < pos[0] < ((WIDTH + MARGIN) * BOARD_SIZE + WIDTH) + WIDTH*2):
        g.verify()
        
      # Click in the grid
      if column < BOARD_SIZE:
        if row < BOARD_SIZE:
          # Set that location to one
          if(g.get_color(row,column) == WHITE):
            g.switch_on(row,column)
          elif(g.get_color(row,column) == YELLOW):
            g.switch_on(row,column)
          elif(g.get_color(row,column) == LIGHT):
            g.switch_off(row,column)
      
      print("Click ", pos, "Grid coordinates: ", row, column)

  # Set the screen background
  screen.fill(BLACK)

 
  # Render the board
  g.render_board()
  

  # Draw the grid
  draw_board()

  # Draw Button
  draw_button()

  # Limit to 60 frames per second
  clock.tick(60)

  # Go ahead and update the screen with what we've drawn.
  pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
