## **_CHESS A.I._**: FishStock

### How it works:

FishStock is a decision-based artificial intelligence that plays as black against any human white player. It uses a min-max tree with an alpha-beta pruning algorithm that runs every move. When you play against FishStock it will wait for your move before making its decision, it will look ahead several moves before responding appropriately. 


<p align="center">
  <img src="https://github.com/Quinn-Barber/Chess-AI/blob/main/chessboard3.png?raw=true"/>
</p>


The engine also displays the number of pruned positions, and the algorithms work directly off of evaluations of the game board. While the displayed number may not look like much, it represents the positions that it no longer looks ahead on. The real time saved is in the several factors higher number of positions it would evaluate if it did not prune.


<p align="center">
  <img src="https://github.com/Quinn-Barber/Chess-AI/blob/main/chessboard4.png?raw=true"/>
</p>


### Downloading FishStock:

# **Step 1:**

Find the location on your computer that you would like to save FishStock to.

# **Step 2:**

If you are using Windows, open up Command Prompt and cd into where you would like to save it.
If you are using MacOS, do the same except using Terminal
If you are using Linux, do the same except using Command Line

# **Step 3:**

Enter the following command into your terminal:
`git clone https://github.com/Quinn-Barber/Chess-AI.git`
If git is not installed, it must be installed for this to work.

# **Step 4:**

Open the project in the IDE of your choice. **Recommended: PyCharm: Community Edition**

# **Step 5:**

Make sure your python interpreter is set up on Python 3.9 or 3.10, have the following libraries installed:

`chess-board`

`chess.svg`

`pygame`

# **Step 6:**

Run `play_chess.py` and move pieces by dragging and dropping the piece. You can change the depth of the engine
in the same file when it calls the `engine.py` function, as it passes a depth. If your move is not initially displayed
try waiting a bit, the engine is still a work in progress and could be slow!
Thanks!

# **Contributing**

## _**FishStock is an open-source project and is being worked on by a team of developers. If you would like to contribute, try commenting on an issue that you would like to work on and we will get back to you as soon as possible! We are using this project as a learning experience and would love for you to learn something out of it with us!**_

### _**Happy Hacking!**_
