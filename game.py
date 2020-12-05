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
          nspace = node.NumberedNode(typeSpace[1])
          self.board[row][column] = nspace
          #self.board[row].append(lines[row].pop(0))
    
    self.setUpLinks()

  def setUpLinks(self):
    # Link dn and up
    for x in range(BOARD_SIZE - 1):
      for y in range(BOARD_SIZE - 1):
        if x == 0:
          self.board[x][y].dn = self.board[x+1][y]
        elif x == BOARD_SIZE - 1:
          self.board[x][y].up = self.board[x-1][y]
        else:
          self.board[x][y].dn = self.board[x+1][y]
          self.board[x][y].up = self.board[x-1][y]
    # Link right and left
    for x in range(BOARD_SIZE - 1):
      for y in range(BOARD_SIZE - 1):
        if y == 0:
          self.board[x][y].right = self.board[x][y+1]
        elif y == BOARD_SIZE - 1:
          self.board[x][y].left = self.board[x][y-1]
        else:
          self.board[x][y].right = self.board[x][y+1]
          self.board[x][y].left = self.board[x][y-1]
    
    

  def is_alight(self, row, column):
    return self.board[row][column] in self.lights

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
      head = head.left
      self.switchOnTraverse(head, goLeft)
      head = head.right
      self.switchOnTraverse(head, goRight)
      head = head.dn
      self.switchOnTraverse(head, goDown)
      try:
        head = head.up
        self.switchOnTraverse(head, goUp)
      except:
        pass    
    
  # next = function that returns next (up,dn,lft,rt) link
  def switchOnTraverse(self, head, next):
    while head != None:
      if head.color == WHITE:
        head.color = LTYELLOW
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
  
  def printDown(self,x=0,y=0):
    head = self.board[x][y]
    while head is not None:
      print(head)
      head = head.dn
  
  def printRight(self,x=0,y=0):
    head = self.board[x][y]
    while head is not None:
      print(head, end="   ")
      head = head.right

  def printLeft(self,x=0,y=0):
    head = self.board[x][y]
    while head is not None:
      print(head, end="   ")
      head = head.left

  def printUp(self,x=0,y=0):
    head = self.board[x][y]
    while head is not None:
      print(head)
      head = head.up


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