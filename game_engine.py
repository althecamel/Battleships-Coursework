import components 
global battleships 
global board

def attack(coordinates,board,battleships):
    '''Attacks board with coordinates from player.

    Args:
        coordinates: Tuple of coordinates inputer by player.

        board: List of lists representing gameboard.

        battleships: Dictionary of battleships used in game.
    
    Returns:
        True if a ship has been hit at the coordinates given, and False if not.
    '''
    x = coordinates[0]
    y = coordinates[1]
    ship = board[x][y]
    if(ship != None):
        ship = board[x][y]
        value = battleships[ship]
        #decrements size value of ship in dictionary
        battleships[ship] = value - 1
        if(battleships[ship] == 0):
            print(ship, "sunk!")
        else:
            print(ship, f"hit at ({x},{y})")
        #updates coordinate positions on board to None
        board[x][y] = None
        return True
    return False

def cli_coordinates_input():
    '''Generates tuple of coordinates input by player.

    Returns:
        A tuple of x and y coordinates of player's attack.
    '''
    try:
        x = int(input("Please input the x-coordinate of your attack: "))
    except ValueError:
        print("Incorrect input.")
        cli_coordinates_input()
    try:
        y = int(input("Please input the y-coordinate of your attack: "))
    except ValueError:
        print("Incorrect type.")
        cli_coordinates_input()
    coords = (x,y)
    return coords

def check_end(battleships):
    '''Checks if all battleships have been sunk.

    Args: 
        battleships: Dictionary of all battleships in current state in game.

    Returns:
        True if all values in dictionary are 0, otherwise returns False.
    '''
    num_ships = 0
    total_sunk = 0
    for ship in battleships:
        num_ships += 1
        if(battleships[ship] == 0):
            total_sunk += 1
    if(total_sunk == num_ships):
        return True
    return False

def simple_game_loop():
    '''A game loop for singleplayer battleships.
    '''
    print("Welcome to Battleships!")
    #setup board with default settings
    empty_board = components.initialise_board()
    ships = components.create_battleships()
    board = components.place_battleships(empty_board,ships)
    #input coordinates
    #game loop until all battleships sunk
    while(check_end(ships) == False):
        coords = cli_coordinates_input()
        if(attack(coords,board,ships) == True):
            print(" ")
        else:
            print("Miss!")
    print("Game over. You win!")

#global namespace
if (__name__ == '__main__'):
    simple_game_loop()