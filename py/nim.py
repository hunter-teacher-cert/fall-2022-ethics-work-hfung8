# nim.py
# Harrison Fung
# CSCI 77800 Fall 2022
# collaborators: Harrison Fung 
# consulted: 

from random import randint
# game of nim 
stones = randint(1,10)
#print(stones)

while True:
  turn = int(input("How many stones are you taking?"))
  turn2 = int(input("How many stones are you taking?"))
  
  player1 = stones - turn
  stones -= turn
  #print(stones)  
  player2 = stones - turn2
  stones -= turn2
  #print(stones)
  if (player1 < 0):
    print("Congrats player 2, you won the game!")
    break
  elif (player2 < 0):
    print("Congrats player 1, you won the game!")
    break
