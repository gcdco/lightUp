"""
 George Duensing
 cs325: HW8
 December 07, 2020
 
 sources:
  https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
  http://simpson.edu/computer-science/
  
"""
from colors import WHITE, BLACK, GREEN, RED, YELLOW, LTYELLOW, LIGHT

# Parent class
# Board Space
class Node:
  def __init__(self):
    # Links to other spaces
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

  def switchOff(self):
    self.color = WHITE
  
  # next = function that returns next (up,dn,lft,rt) link
  def switchOffTraverse(self, head, next):
    queue = []
    while head is not None:
      if head.color == LTYELLOW:
        head.color = WHITE
      elif head.color == LIGHT:
        head.color = WHITE
        queue.append(head)
      elif head.color != BLACK:
        head = None
      elif head.color != GREEN:
        head = None
      
      if head != None:
        head = next(head)
        
    for n in queue:
      n.switchOn()
      

  def __str__(self):
    return 'W'