from colors import WHITE, BLACK, GREEN, RED, YELLOW, LTYELLOW, LIGHT

## Traversal functions
##
def goLeft(h): return h.left
def goRight(h): return h.right
def goDown(h): return h.dn
def goUp(h): return h.up

# Parent class
class Node:
  def __init__(self):
    self.up = None
    self.dn = None
    self.left = None
    self.right = None
    self.color = RED

# Black square class
class BlackNode(Node):
  def __init__(self):
    Node.__init__(self)
    self.color = BLACK
  
  def __str__(self):
    return 'B'

# Black square with number
class NumberedNode(Node):
  def __init__(self,num=0):
    Node.__init__(self)
    self.value = num
    self.color = GREEN
  
  def __str__(self):
    return f'{self.value}'

# Playable space
class WhiteNode(Node):
  def __init__(self):
    Node.__init__(self)
    self.lightConflict = 0
    self.color = WHITE
  
  def switchOn(self):
    self.color = LIGHT
    
    """
    self.color = YELLOW
    self.light = True
    
    head = self.left
    self.switchOnTraverse(head, goLeft)
    head = self.right
    self.switchOnTraverse(head, goRight)
    head = self.dn
    self.switchOnTraverse(head, goDown)
    head = self.up
    self.switchOnTraverse(head, goUp)
    """
    
  # next = function that returns next (up,dn,lft,rt) link
  def switchOnTraverse(self, head, next):
    while head != None:
      if head.color == WHITE:
        head.color = LTYELLOW
        
      if head.light == True:
        head.color = YELLOW
        
      if head.color == BLACK:
        head = None
      if head.color == GREEN:
        head = None
      
      if head != None:
        head = next(head)


  def switchOff(self):
    self.color = WHITE
    #self.light = False
    
    head = self.left
    self.switchOffTraverse(head, goLeft)
    head = self.right
    self.switchOffTraverse(head, goRight)
    head = self.dn
    self.switchOffTraverse(head, goDown)
    head = self.up
    self.switchOffTraverse(head, goUp)
  
  # next = function that returns next (up,dn,lft,rt) link
  def switchOffTraverse(self, head, next):
    while head is not None:
      if head.color != BLACK:
        if head.color != GREEN:
          #if head.lightConflict > 0:
            #head.lightConflict -= 1
          head.color = WHITE
      head = next(head)

  def __str__(self):
    return 'W'