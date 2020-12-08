readme.txt

https://en.wikipedia.org/wiki/Light_Up_(puzzle)

Directions from wikipedia:
"Light Up is played on a rectangular grid of white and black cells. The player places light bulbs in white cells such that no two bulbs shine on each other, until the entire grid is lit up. A bulb sends rays of light horizontally and vertically, illuminating its entire row and column unless its light is blocked by a black cell. A black cell may have a number on it from 0 to 4, indicating how many bulbs must be placed adjacent to its four sides; for example, a cell with a 4 must have four bulbs around it, one on each side, and a cell with a 0 cannot have a bulb next to any of its sides. An unnumbered black cell may have any number of light bulbs adjacent to it, or none. Bulbs placed diagonally adjacent to a numbered cell do not contribute to the bulb count."

This game uses pygame for GUI and to enter a solution.
Solutions to the provided boards have been included in the folder "Examples"
Note: verification algorith is located in "game.py" as method "verify()"

To run (on windows):
 1. navigate to folder (windows or mac)
 2. install pygame if not already installed.(https://www.pygame.org/wiki/GettingStarted)
 3. to run use command in terminal (windows): py main.py
 4. to exit hit exit button

Click on white board pieces to set a light. Once all the spaces are lit and requirements met, hit verify. The results are printed to the screen underneath the button you clicked. The results are also printed (True/False) to the terminal

Changing Boards:
  To change the boards, replace the contents of "boards.txt" with any of the contents from the included "boards#.txt" files. Restart the game from the terminal after changing boards.