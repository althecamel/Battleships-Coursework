import components
import game_engine
import random

global board

def generate_attack(board):
    '''Generates coordinates of AI's attack.

    Returns:
        Tuple of coordinates where the AI attacks the player's board at random.
    '''
    #ensure range is within size of board
    size = len(board) - 1
    randx = random.randint(0,size)
    randy = random.randint(0,size)
    coords = (randx, randy)
    return coords

def check_end(board1,board2):
    ''''Checks whether the game has ended.

    Args:
        board1: Player board.

        board2: AI board.

    Returns:
        True if the game has finished, and False otherwise.
    '''
    total1 = 0
    total2 = 0
    for i in board1:
        for j in i:
            if(j != None):
                total1 += 1
    for i in board2:
        for j in i:
            if(j != None):
                total2 += 1
    if((total1 == 0)|(total2 == 0)):
        return True
    return False

def process_attack(board,coords,battleships):
    '''
    '''
    x = coords[0]
    y = coords[1]
    if(board[x][y] != None):
        ship = board[x][y]
        board[x][y] = None
        battleships[ship] = battleships[ship] - 1
        if(battleships[ship] == 0):
            print(f"{ship} sunk!")
        else:
            print(f"{ship} hit at ({x},{y}).")
    return board

def ai_opponent_game_loop():
    '''
    '''
    print("Welcome to Battleships!")
    #initialise board for player and computer
    board = components.initialise_board()
    #create separate dictionaries of battleships for each player
    player_battleships = components.create_battleships()
    ai_battleships = components.create_battleships()
    
    player_board = components.place_battleships(board,player_battleships,'custom')
    ai_board = components.place_battleships(board,ai_battleships,'random')
    name1 = input("Enter player 1's name: ")
    #add players to dictionary
    players[name1] = player_board
    players['Computer'] = ai_board
    #game loop
    while(check_end(players[name1],players['Computer']) == False):
        #attack from player and process on ai's board
        coords = game_engine.cli_coordinates_input()
        ai_board = process_attack(ai_board,coords,ai_battleships)
        #generate AI attack and process on player board
        print("Computer attack: ")
        ai_attack = generate_attack(player_board)
        player_board = process_attack(player_board,ai_attack,player_battleships)
        #print ascii representation of player board after ai attack
        for i in player_board:
            print(i)
    total1 = 0
    total2 = 0
    for key,value in zip(player_battleships):
        if(value == 0):
            total1 += 1
    for key,value in zip(ai_battleships):
        if(value == 0):
            total2 += 1

    if(total1 == 0):
        print("Player wins!")
    else:
        print("Computer wins!")

#global namespace
players = {}

board = components.initialise_board()
player1_battleships = components.create_battleships()
player2_battleships = components.create_battleships()
player1_board = components.place_battleships(board,player1_battleships,'random')
player2_board = components.place_battleships(board,player2_battleships,'random')
name1 = input("Enter player 1's name: ")
name2 = input("Enter player 2's name: ")
#add players to dictionary
players[name1] = player1_board
players[name2] = player2_board

