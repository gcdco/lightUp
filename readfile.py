### readFile.py
### 
### Read a textfile
### 

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