"""
 George Duensing
 cs325: HW8
 December 07, 2020
 
 sources:
  https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
  http://simpson.edu/computer-science/
  
"""
import node

from colors import WHITE, BLACK, GREEN, RED, YELLOW, LTYELLOW, LIGHT, LIGHT_ERROR

BOARD_SIZE = 7

## Traversal functions
##
def goLeft(h): return h.left
def goRight(h): return h.right
def goDown(h): return h.dn
def goUp(h): return h.up

class Game:
  def __init__(self, lines):
    self.board = []
    self.lights = []
    self.white_spaces = []
    self.numbered_spaces = []
    
    # Make the board
    for row in range(0,BOARD_SIZE):
      self.board.append([])
      for column in range(0,BOARD_SIZE):
        self.board[row].append(None)

    # Populate the board
    for row in range(0,BOARD_SIZE):
      l = lines.pop(0)
      for column in range(0,BOARD_SIZE):
        typeSpace = l.pop(0)
        #print(typeSpace)
        if typeSpace == 'w':
          wspace = node.WhiteNode()
          self.board[row][column] = wspace
          self.white_spaces.append(wspace)
        if typeSpace == 'b':
          bspace = node.BlackNode()
          self.board[row][column] = bspace
        if len(typeSpace) == 2:
          nspace = node.NumberedNode(int(typeSpace[1]))
          self.board[row][column] = nspace
          self.numbered_spaces.append(nspace)
    
    self.setUpLinks()

  def setUpLinks(self):
    # Set-up top row
    for x in range(0,BOARD_SIZE):
        self.board[0][x].dn = self.board[1][x]
        if(x < BOARD_SIZE - 1):
          self.board[0][x].right = self.board[0][x+1]
        if(x > 0):
          self.board[0][x].left = self.board[0][x-1]
    # Set-up right row
    for x in range(0,BOARD_SIZE):
      self.board[x][BOARD_SIZE - 1].left = self.board[x][BOARD_SIZE - 2]
      if (x < 6):
        self.board[x][BOARD_SIZE - 1].dn = self.board[x+1][BOARD_SIZE - 1]
      if (x > 0):
        self.board[x][BOARD_SIZE - 1].up = self.board[x-1][BOARD_SIZE - 1]
    # Set-up bottom row
    for x in range(0,BOARD_SIZE):
      self.board[BOARD_SIZE - 1][x].up = self.board[BOARD_SIZE - 2][x]
      if(x < 6):
        self.board[BOARD_SIZE - 1][x].right = self.board[BOARD_SIZE - 1][x+1]
      if(x > 0):
        self.board[BOARD_SIZE - 1][x].left = self.board[BOARD_SIZE - 1][x-1]
    # Set-up left row
    for x in range(0,BOARD_SIZE):
      self.board[x][0].right = self.board[x][1]
      if(x < BOARD_SIZE - 1):
        self.board[x][0].dn = self.board[x+1][0]
      if(x > 0):
        self.board[x][0].up = self.board[x-1][0]
    # Set-up middle rows
    for x in range(1,BOARD_SIZE-1):
      for y in range(1,BOARD_SIZE-1):
        self.board[x][y].up = self.board[x-1][y]
        self.board[x][y].right = self.board[x][y+1]
        self.board[x][y].dn = self.board[x+1][y]
        self.board[x][y].left = self.board[x][y-1]

  # Call after rendering board
  def verify(self):
    white_space_bool = True
    numbered_space_bool = True
    light_bool = True
    # Check that white spaces are all lit
    for n in self.white_spaces:
      if n.color != YELLOW:
        if n.color != LIGHT:
          white_space_bool = False
    # Check that numbered spaces have appropriate number of lights adjacent
    for n in self.numbered_spaces:
      if (self.verify_numbered_space(n) == False):
        numbered_space_bool = False
    # Check for collisions
    for head in self.lights:
      if (not self.verify_light_space(head, goLeft)):
        light_bool = False
        head.color = LIGHT_ERROR
      if (not self.verify_light_space(head, goRight)):
        light_bool = False
        head.color = LIGHT_ERROR
      if (not self.verify_light_space(head, goUp)):
        light_bool = False
        head.color = LIGHT_ERROR
      if (not self.verify_light_space(head, goDown)):
        light_bool = False
        head.color = LIGHT_ERROR
    
    print(light_bool and white_space_bool and numbered_space_bool)
    return light_bool and white_space_bool and numbered_space_bool

  # Return true if no conflicts
  def verify_light_space(self, head, next):
    if head != None:
        head = next(head)
    while head != None:
      if head.color == LIGHT:
        if head.color == LIGHT_ERROR:
          return False
      elif head.color == BLACK:
        head = None
      elif head.color == GREEN:
        head = None
      
      if head != None:
        head = next(head)
    return True

  # Helper function to check numbered spaces
  def verify_numbered_space(self, head):
    count = 0
    required = head.value
    if head.up != None:
      if head.up.color == LIGHT:
        count += 1
    if head.right != None:
      if head.right.color == LIGHT:
        count += 1
    if head.dn != None:
      if head.dn.color == LIGHT:
        count += 1
    if head.left != None:
      if head.left.color == LIGHT:
        count += 1
    return count >= required

  def get_color(self, row, column):
    return self.board[row][column].color
  
  def set_color(self, row, column, color):
    self.board[row][column].color = color
    
  def switch_on(self, row, column):
    self.lights.append(self.board[row][column])
    self.board[row][column].color = LIGHT
  
  def switch_off(self, row, column):
    self.board[row][column].color = WHITE
    self.lights.remove(self.board[row][column])
    
    
  def render_board(self):
    for head in self.white_spaces:
      if head.color not in [LIGHT,LIGHT_ERROR]:
        head.color = WHITE
    
    for head in self.lights:
      self.switchOnTraverse(head, goLeft)
      self.switchOnTraverse(head, goRight)
      self.switchOnTraverse(head, goDown)
      try:
        self.switchOnTraverse(head, goUp)
      except:
        pass    
    
  # next = function that returns next (up,dn,lft,rt) link
  def switchOnTraverse(self, head, next):
    #if head != None:
        #head = next(head)
    
    while head != None:
      if head.color == WHITE:
        head.color = YELLOW
      elif head.color == BLACK:
        head = None
      elif head.color == GREEN:
        head = None
      
      if head != None:
        head = next(head)

  def printBoard(self):
    for x in self.board:
      for y in x:
        print(y, end='   ')
      print("\n")
  

# Read lines from a text file
# Split lines by commas and add them to the array
class readFile:
  def __init__(self, f):
    self.f = f

  # Return list of text lines
  def read(self):
    # First, open file to read.
    readFile = open(self.f, 'r')
    # Store each row of text in the list
    lines = []
    for line in readFile:
        line = line.rstrip()
        lines.append(line.split(','))
    readFile.close()

    return lines