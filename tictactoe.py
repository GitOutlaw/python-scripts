# Left off at 5:22:50 - https://www.youtube.com/watch?v=4F2m91eKmts

# ----- Global Varaibles -----



# Game board
board = ['-'] * 9

# If game is still going
game_still_going = True

# Who won? or tie?
winner = None

# Whos turn is it
current_player = "X"


# Display Board
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
  print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
  print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')


# Play a game of tic tac toe
def play_game():

  # display intial board
  display_board()

  while game_still_going:

    # handle a single turn of an aribitrary player
    handle_turn(current_player)

    # Check if game is has ended
    check_if_game_over()
    
    # Flip to the oher player
    flip_player()

  # The game has ended
  if winner == 'X' or winner == 'O':
    print(winner + ' won.')
  elif winner == None:
    print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):
  position = input('Choose a position from 1-9: ')
  position = int(position) - 1


  board[position] = 'X'

  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  # check rows
  # check columns
  # check diagonals
  return

def check_if_tie():
  return

def flip_player():
  return


play_game()






# display board
# play game
# handle turn
# check win
  # check rows
  # check columns
  # check diagonals
# check tie
# flip player
