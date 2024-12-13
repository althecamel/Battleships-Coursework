import components
import game_engine
import random

global board
global players 

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

def process_attack(board,coords):
    '''Processes the given attack on the given board.

    Args:
        board: Player's board containing ships.

        coords: Coordinates of attack.

        battleships: Dictionary of battleships.

    Returns: List containing type of ship hit and the updated board.
    '''
    x = coords[0]
    y = coords[1]
    if(board[x][y] != None):
        board[x][y] = None
    return board

def ai_opponent_game_loop():
    '''
    Game loop with AI opponent.
    '''
    print("Welcome to Battleships!")
    name1 = input("Player 1's name: ")
    #change keys of players dictionary for player and computer
    ini_list = [name1,'Computer']
    players_new = dict(zip(ini_list,list(players.values())))
    #shortcut to player's board and battleships list
    player_list = players_new[name1]
    player_ships = player_list[1]
    #shortcut to computer's board and battleships list
    ai_list = players_new['Computer']
    ai_ships = ai_list[1]
    #place player's battleships with custom algorithm
    player_board = components.place_battleships(player_list[0],player_ships,'custom')
    #create ai board with random placement
    ai_board = components.place_battleships(ai_list[0],ai_ships,'random')
    #game loop
    while(check_end(player_board,ai_board) == False):
        #attack from player and process on ai's board
        coords = game_engine.cli_coordinates_input()
        x = coords[0]
        y = coords[1]
        if(ai_board[x][y] != None):
            ship = ai_board[x][y]
            ai_ships[ship] = ai_ships[ship] - 1
            if(ai_ships[ship] == 0):
                print(f"{ship} sunk!")
            else:
                print(f"{ship} hit at ({x},{y}).")
        ai_board = process_attack(ai_board,coords,ai_ships)
        #generate AI attack and process on player board
        print("Computer attack: ")
        ai_attack = generate_attack(player_board)
        x = ai_attack[0]
        y = ai_attack[1]
        if(player_board[x][y] != None):
            ship = player_board[x][y]
            player_ships[ship] = player_ships[ship] - 1
            if(player_ships[ship] == 0):
                print(f"Computer has sunk your {ship}!")
            else:
                print(f"{ship} hit by computer at ({x},{y}).")
        player_board = process_attack(player_board,ai_attack,player_ships)
        #print ascii representation of player board after ai attack
        for i in player_board:
            print(i)
    total1 = 0
    total2 = 0
    for value in player_ships.values():
        if(value == 0):
            total1 += 1
    for value in ai_ships.values():
        if(value == 0):
            total2 += 1

    if(total1 == 5):
        print("Player wins!")
    else:
        print("Computer wins!")

#global namespace
players = {}
#initialise their board and battleships
player1_board = components.initialise_board()
player2_board = components.initialise_board()
player1_battleships = components.create_battleships()
player2_battleships = components.create_battleships()
#create list containing their empty board and battleships
player1 = []
player1.append(player1_board)
player1.append(player1_battleships)
player2 = []
player2.append(player2_board)
player2.append(player2_battleships)
name1 = input("Enter player 1's name: ")
name2 = input("Enter player 2's name: ")
#assign their names as keys and list of board/battleships as values
players[name1] = player1
players[name2] = player2

ai_opponent_game_loop()