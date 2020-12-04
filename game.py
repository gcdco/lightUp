import node
from colors import WHITE, BLACK, GREEN, RED

BOARD_SIZE = 7

class Game:
  def __init__(self, lines):
    self.board = []
    
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
        if typeSpace == 'b':
          bspace = node.BlackNode()
          self.board[row][column] = bspace
        if len(typeSpace) == 2:
          nspace = node.NumberedNode(typeSpace[1])
          self.board[row][column] = nspace
          #self.board[row].append(lines[row].pop(0))
    
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