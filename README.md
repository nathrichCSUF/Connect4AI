### Connect4AI
Connect4AI is a Player v Player and Player v AI Connect-4 game, where the aim is to connect 4 pieces of the same color in vertical, horizontal or diagnol line. This game is exclusively developed by:    
[Yash Bhambhani](www.github.com/yash-b)   
[Dustin Vuong](www.github.com/itosken)   
[Matthew Camarena](www.github.com/MatthewCamarena)   
[Nathan Richards](www.github.com/nathrichCSUF)

#### Directions:
- Download as .ZIP, extract into a folder.
- Right-click folder, and select 'Open in Terminal'.
- Install Python 3.7 from list of downloads https://www.python.org/downloads/
- Put 'pip install pygame' in terminal and press enter.
- Put 'python3 main.py' in terminal and press enter.
- Enjoy!

#### Controls:
- W: Drop piece on column.
- A: Move selector to left.
- S: Move selector to right.
- Q: Quit game.

#### Important Files:
- main.py: Main file that calls all other local modules, creates objects of each and runs the game in its chronological order. Also used for debugging by adding -d flag in terminal. 

- ai.py: Base class for AI Implementation of Minimax algorithm to decide what column should the AI drop its piece on. It calculates potential scores of its moves, and selects the column which yields the better score. Above all else, it prioritizes blocking Player's winning move unless it can win before the player. It uses multiple heuristic functions to calculate the scores and chooses the highest one.  

- board.py: Base class for the board, where it declares all sprites/sounds, number of slots, selectors, and consists of functions that initializes, creates, resets, clears, and designs the main board of connect 4. It also consists of functions that allows the player and the AI to place the piece onto a column.   

- menu.py: Base class for the main menu, which consists of sprites, and three different buttons, namely: 'Player v Player', 'Player v AI', and 'Quit.' This class describes use case for each button and activates appropriate function when the buttons are clicked. 

- settings.py: Base class for settings, which just describes two different states of the game, 'Active' and 'Inactive.'

- slot.py: Base class for slots, which describes alternating turns and their appropriate piece color (red and yellow) and other settings. 

#### Screencaps:

<a href="https://ibb.co/rvXH6mb"><img src="https://i.ibb.co/nRKjcb3/Screenshot-from-2019-12-10-01-55-47.png" alt="Screenshot-from-2019-12-10-01-55-47" border="0"></a>

<a href="https://ibb.co/wB45C36"><img src="https://i.ibb.co/xX6xGP5/Screenshot-from-2019-12-10-01-56-41.png" alt="Screenshot-from-2019-12-10-01-56-41" border="0"></a>

<a href="https://ibb.co/h2c9x4N"><img src="https://i.ibb.co/VMx90zG/Screenshot-from-2019-11-06-23-19-41.png" alt="Screenshot-from-2019-11-06-23-19-41" border="0"></a>
