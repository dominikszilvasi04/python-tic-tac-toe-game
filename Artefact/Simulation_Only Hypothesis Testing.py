#Welcome this file is the simulation gamemode,
#out of the full game however with slight adjustments
#This gamemode is run a certain amount of times as the user chooses
#This is testing my hypothesis of whether the bots have an even chance of winning
#I wanted to test this as in theory they should
#However since BOT1 always goes first,
#it might not be 50/50
#In turn, this will reveal my other question whether it is,
#more beneficial for a player to be first or second
#The user has a choice of inputting the amount of times,
#they would like to run the simulation
#The more times the simulation is run the more accurate it may become.
#Enjoy!


import time
import random
import csv
def print_grid(grid):
      print("\n    1   2   3 \n")
      print("1   " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])    
      print("   ---+---+---")
      print("2   " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
      print("   ---+---+---")
      print("3   " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "\n")
      
def bot1(grid):
  existing_moves = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == " ":
        existing_moves.append((row, col))
  return existing_moves[random.randrange(len(existing_moves))]


def bot2(grid):
  existing_moves = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == " ":
        existing_moves.append((row, col))
  return existing_moves[random.randrange(len(existing_moves))]

def checkboardfull(grid):
    for i in grid:
        if " " in i:
            return False
    return True

def row_status(grid, row):
  return (grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2] and grid[row][0] != " ")

def column_status(grid, col):
  return (grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col] and grid[0][col] != " ")

def diagonal_status(grid):
    return (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != " ") or\
            (grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2] and grid[2][0] != " ")

def win_status(grid):
  for i in range(3):
    if row_status(grid, i):
      return True
    if column_status(grid, i):
      return True
  if diagonal_status(grid):
    return True
  return False

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
  bot1_file = 'Bot_Results.csv'
  while not checkboardfull(grid):
    print_grid(grid)
    print("Bot {}'s turn!".format(turn + 1)) #The {} is a placeholder, and format() is replaces the placeholder with the value of turn + 1 (which will either print bot1 or bot2 depending on go).
    time.sleep(0.01) #This adds a point zero one second delay between each of the bots turn in order to speed up process from normal game
    row, col = players[turn](grid)
    grid[row][col] = "X" if turn == 0 else "O"
    # Check if a bot won
    if win_status(grid):
      print_grid(grid)
      print("Bot 1 won!" if turn == 0 else "Bot 2 won!")
      if turn == 0:
          with open(bot1_file, mode='a', newline='') as results_file:
              results_writer = csv.writer(results_file)
              results_writer.writerow([1])
      else:
          with open(bot1_file, mode='a', newline='') as results_file:
              results_writer = csv.writer(results_file)
              results_writer.writerow([2])
      break
    turn = 1 - turn
  else:
    print_grid(grid)
    print("There is no winner, it is a tie.")
testsize = int(input("Please input how many times you would like the simulation to run: "))
for i in range(testsize):
    simulation()