from colors import WHITE, BLACK, GREEN, RED,YELLOW

# Parent class
class Node:
  def __init__(self, w=50, h=50):
    self.width = w
    self.height = h
    self.up = None
    self.dn = None
    self.left = None
    self.right = None
  

# Black square class
class BlackNode(Node):
  def __init__(self, w=50, h=50):
    Node.__init__(self,w,h)
    self.color = BLACK
  
  def __str__(self):
    return 'B'

# Black square with number
class NumberedNode(Node):
  def __init__(self,num=0):
    Node.__init__(self)
    self.color = GREEN
    self.value = num
  
  def __str__(self):
    return f'{self.value}'

# Playable space
class WhiteNode(Node):
  def __init__(self, w=50, h=50):
    Node.__init__(self,w,h)
    self.color = WHITE
    self.light = False
  
  def switchOn(self):
    self.color = LIGHT
    head = self.left
    while (head is not None and head.color == WHITE):
      head.color = RED
      head = head.left
    head = self.right
    while (head is not None and head.color == WHITE):
      head.color = RED
      head = head.right
    head = self.up
    while (head is not None and head.color == WHITE):
      head.color = RED
      head = head.up
    head = self.dn
    while (head is not None and head.color == WHITE):
      head.color = RED
      head = head.dn
  
  def switchOff(self):
    pass

  def __str__(self):
    return 'W'