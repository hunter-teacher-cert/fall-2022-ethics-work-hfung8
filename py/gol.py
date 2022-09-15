# gol.py
# Harrison Fung 
# CSCI 77800 Fall 2022
# collaborators: Harrison Fung
# consulted: https://robertheaton.com/2018/07/20/project-2-game-of-life/

import random

# easier to hold the values of dead and alive as a variable to compare with later on 
LIVE = 1 
DEAD = 0

def dead_state(width, height):
  arr = [[0 for i in range(height)] for j in range(width)]
  return arr

def random_state(width, height):
  state = dead_state(width, height)
  for x in range(0, len(state)):
    for y in range(0, len(state[0])):
        random_number = random.random()
        if random_number > 0.85:
            cell_state = LIVE
        else:
            cell_state = DEAD
        state[x][y] = cell_state
  return state

def state_width(state):
  return len(state)

def state_height(state):
  return len(state[0])

def render(state):
  display_as = {
    DEAD: ' ',
    LIVE: u"\u2588"
  }
  lines = []
  for y in range(0, state_height(state)):
    line = ''
    for x in range(0, state_width(state)):
      line += display_as[state[x][y]] * 2
    lines.append(line)
  print("\n".join(lines))

# a_dead_state = dead_state(5,5)
# a_random_state = random_state(5,5)

# render(a_random_state)
# render(a_dead_state)

# pass on the cell co-ordinates for the board here
def next_cell_value(cell_coords, state):
  x = cell_coords[0]
  y = cell_coords[1] 
  living_neighbors = 0
# we must check the row before, current row, and next row 
# we must check the column before, current column, and next column
  for i in range((x - 1), (x+1)+1):
# we must make sure that the co-ordinate is on the width of the board    
    if i < 0 or i >= len(state): continue
      
    for j in range((y - 1), (y+1)+1):
# we must make sure that the co-ordinate is on the length of the board
      if j < 0 or j >= len(state[0]): continue
# we must make sure that we're not comparing it to it's neighbor
      if i == x and j == y: continue
      
      if state[i][j] == LIVE:
        living_neighbors += 1
      
  if state[x][y] == LIVE:
    if living_neighbors <= 1:
      return DEAD
    elif living_neighbors <= 3:
      return LIVE
    else:
      return DEAD
  else:
    if living_neighbors == 3:
      return LIVE
    else:
      return DEAD
      
def next_board_state(initial_state):
  width = state_width(initial_state)
  height = state_height(initial_state)
  #update dead_state to equal actual_state of the board
  new_state = dead_state(width,height)
  for i in range(0,width):
    for j in range(0,height):
      new_state[i][j] = next_cell_value((i, j), initial_state)
  return new_state

board = random_state(5,5)
next_board = next_board_state(board)

render(board)
print(" ")
print("++++++++++++++++++++++++++")
print(" ")
render(next_board)
