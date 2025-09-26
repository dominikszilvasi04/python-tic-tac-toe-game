#Exam number: 111123
#BACKGROUND FUNCTIONS FOR ALL GAMEMODES:
import csv
import random
import time
#This first function creates a baord that has rows and columns 1-3
def print_grid(grid):
      print("\n    1   2   3 \n")
      print("1   " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])    
      print("   ---+---+---")
      print("2   " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
      print("   ---+---+---")
      print("3   " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "\n")

#This is the player 1
def player1(grid):
  while True:
    row = input("Enter what ROW you'd like: ")
    #Next check wether input is a digit and is between 1 and 3, while not: ask to re input
    while not row.isdigit() or int(row) < 1 or int(row) > 3:
      row = input("Please try again and enter what ROW you'd like: ")
      
    #Converts data into integer
    row = int(row)
    col = input("Enter what COLUMN you'd like: ")
    while not col.isdigit() or int(col) < 1 or int(col) > 3:
      col = input("Please try again and enter what COLUMN you'd like: ")
    col = int(col)
    #Next make sure that player enters an empty
    if grid[row-1][col-1] != " ":
      print("Pick an empty box!")
    else:
      return (row-1, col-1)
#Same thing but for player 2:
def player2(grid):
  while True:
    row = input("Enter what ROW you'd like: ")
    #Next check wether input is a digit and is between 1 and 3, while not: ask to re input
    while not row.isdigit() or int(row) < 1 or int(row) > 3:
      row = input("Please try again and enter what ROW you'd like: ")
      
    #Converts data into integer
    row = int(row)
    col = input("Enter what COLUMN you'd like: ")
    while not col.isdigit() or int(col) < 1 or int(col) > 3:
      col = input("Please try again and enter what COLUMN you'd like: ")
    col = int(col)
    #Next make sure that player enters an empty
    if grid[row-1][col-1] != " ":
      print("Pick an empty box!")
    else:
      return (row-1, col-1)

#Next is the first computer bot
def bot1(grid):
  existing_moves = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == " ":
        existing_moves.append((row, col))
  return existing_moves[random.randrange(len(existing_moves))]

#Next is second computer bot
def bot2(grid):
  existing_moves = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == " ":
        existing_moves.append((row, col))
  return existing_moves[random.randrange(len(existing_moves))] #Here it generates a number between 0 and the existing_moves


#Next check wether board is full by going 1 by 1 and checking for empty spaces
def checkboardfull(grid):
    for i in grid:
        if " " in i:
            return False
    return True

#Next create status checks of board in which winners are stored:
def row_status(grid, row):
  return (grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2] and grid[row][0] != " ")

def column_status(grid, col):
  return (grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col] and grid[0][col] != " ")

def diagonal_status(grid):
    return (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != " ") or\
            (grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2] and grid[2][0] != " ")


#Next check for a winner using the previous "status" functions
def win_status(grid):
  for i in range(3):
    if row_status(grid, i):
      return True
    if column_status(grid, i):
      return True
  if diagonal_status(grid):
    return True
  return False

# Define function to write game results to CSV file
def analytics(filename, time_taken):
    with open(filename, mode='a' , newline='') as csv_file: #a = append
        writer = csv.writer(csv_file)
        writer.writerow([time_taken])


# Single Player
def singleplayer():
  #2D empty grid to start off with
  grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

  #Create variable to track time
  start = time.time()

    # Create 2 players of the game, Player 1 is X and the bot is O
  players = ["X", "O"]
  # Player X plays first. Turn function stores number of the current player
  turn = 0
  while not checkboardfull(grid):
    print_grid(grid)
    if turn == 0: #player's turn
      print("Your turn!")
      row, col = player1(grid)
      grid[row][col] = players[turn]
    else: # bot's turn
      print("Computer plays!")
      row, col = bot1(grid)
      grid[row][col] = players[turn]
        # Check if the player won
    if win_status(grid):
      print_grid(grid)
      print("You won!" if turn == 0 else "Computer won!")
      break
    turn = 1 - turn
        #TIE
  else:
      print_grid(grid)
      print("There is no winner, it is a tie.")

  #Endtimer
  end = time.time()
  #Timetaken:
  timefinish = end - start
  timefinish = round(timefinish, 2)
  print("The game took", timefinish,"seconds to finish")
  filename = "game_results(SINGLEPLAYER).csv"
  analytics(filename, timefinish)

#MULTIPLAYER
def multiplayer():
  #2D empty grid to start off with
  grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
  ]

  #Create variable to track time
  start = time.time()
  
  # Create 2 players of the game, Player 1 is X and Player 2 is O
  players = ["X", "O"]
  # Player X plays first. Turn function stores number of the current player
  turn = 0
  while not checkboardfull(grid):
    print_grid(grid)
    if turn == 0: # player 1's turn
      print("Player 1's turn!")
      row, col = player1(grid)
    else: # player 2's turn
      print("Player 2's turn!")
      row, col = player2(grid)
    grid[row][col] = players[turn]

    # Check if the player won
    if win_status(grid):
      print_grid(grid)
      print("Player 1 won!" if turn == 0 else "Player 2 won!")
      break
    turn = 1 - turn

  #TIE
  else:
    print_grid(grid)
    print("There is no winner, it is a tie.")

  #Endtimer
  end = time.time()
  #Timetaken:
  timefinish = end - start
  timefinish = round(timefinish, 2)
  print("The game took", timefinish,"seconds to finish")
  filename = "game_results(MULTIPLAYER).csv"
  analytics(filename, timefinish)

def simulation():
  # 2D empty grid to start off with
  grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
  ]
  # Create 2 players of the game, Bot 1 is X and Bot 2 is O
  players = [bot1, bot2]
  # Bot 1 plays first. Turn function stores number of the current player
  turn = 0
  while not checkboardfull(grid):
    print_grid(grid)
    print("Bot {}'s turn!".format(turn + 1)) #The {} is a placeholder, and format() is replaces the placeholder with the value of turn + 1 (which will either print bot1 or bot2 depending on go).
    time.sleep(1) #This adds a one second delay between each of the bots turn in order to make it more natural
    row, col = players[turn](grid)
    grid[row][col] = "X" if turn == 0 else "O"
    # Check if a bot won
    if win_status(grid):
      print_grid(grid)
      print("Bot 1 won!" if turn == 0 else "Bot 2 won!")
      break
    turn = 1 - turn
  else:
    print_grid(grid)
    print("There is no winner, it is a tie.")
print("Welcome to X's and O's!")
print("Please select which gamemode you would like.")
print("If you would like to play Singeplayer, please type 'single'")
print("If you would like to play Multiplayer, please type 'multi'")
print("If you would like simulation, please type 'sim'")
mode = input("Please input your choice: ")
mode = mode.lower()
while mode not in ["single", "multi", "sim"]:
    print("Please enter a valid mode.")
    mode = input()
if mode == "single":
    singleplayer()
elif mode == "multi":
    multiplayer()
else:
    simulation()