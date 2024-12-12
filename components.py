import random
import json

def initialise_board(size=10):
    '''Creates board with empty squares

    Args: 
        size: Size of the board, size x size.

    Returns:
        The 2D list containing squares of type None.
    '''
    #iterate through and add list inside list for number of rows/columns equal to size parameter
    board = [[None]*size for i in range(size)]
    return board

def create_battleships(filename='battleships.txt'):
    '''Creates a dictionary containing all types of battleships and their sizes.

    Args:
        filename: Name of text file containing data.
    
    Returns:
        Dictionary containing name of each battleship and their size.
    '''
    #read battleships text file
    file = open(filename,"r")
    battleships = {}
    file = file.readlines()
    #adds each line into new list, separating it by a colon 
    for i in file:
       temp = []
       temp = i.split(':')
       #strips whitespace from end of word
       temp[1] = temp[1].strip()
       battleships[temp[0]] = int(temp[1])
    return battleships

def place_battleships(board,ships,algorithm='simple'):
    '''Places battleships on the board, using a specific method.

    Args:
        board: List of lists representing empty board.

        ships: All ships in the game to be placed.

        algorithm: Method of placing ships onto board: simple, random or custom.
    
    Returns:
        New board containing every battleship.
    '''
    size = len(board) - 1
    total_ships = len(ships)
    keys,values = zip(*ships.items())
    #simple algorithm
    if(algorithm == 'simple'):
       #iterates through each row 
       for i in range(0,total_ships):
          #adds battleship name to index up to its value in dictionary
          for j in range(0,values[i]):
             board[i][j] = keys[i]
    #random algorithm
    elif(algorithm == 'random'):
        for i in range(0,total_ships):
            valid_list = []
            orientation = ['h','v']
            count = 0
            #chooses random orientation for ship
            choice = random.choice(orientation)
            if(choice == 'h'):
                row = random.randint(0,size)
                col = random.randint(0,size-values[i])
                while(count < values[i]):
                    if(board[row][col] == None):
                        valid_list.append(row)
                        valid_list.append(col)
                        col += 1
                        count += 1
                    else:
                        #if not empty, then reset and try again in another position
                        valid_list = []
                        count = 0
                        row = random.randint(0,size)
                        col = random.randint(0,size-values[i])
            elif(choice == 'v'):
                row = random.randint(0,size-values[i])
                col = random.randint(0,size)
                while(count < values[i]):
                    if(board[row][col] == None):
                        valid_list.append(row)
                        valid_list.append(col)
                        row += 1
                        count += 1
                    else:
                        valid_list = []
                        count = 0
                        row = random.randint(0,size-values[i])
                        col = random.randint(0,size)
            index = 0
            #places ships on board 
            for x in valid_list:
                if(index % 2 == 0):
                    y = valid_list[index+1]
                    board[x][y] = keys[i]
                index += 1

    elif(algorithm=='custom'):
        placement = {}
        #use placement configuration file
        with open('placement.json',mode='r') as f:
            file = json.load(f)
            for key,value in file.items():
                placement[key] = value 
        #iterate through each key and value pair in dictionary
        for ship,coords in placement.items():
            startx,starty,orient = coords
            startx = int(startx)
            starty = int(starty)
            ship_size = ships[ship]
            if(orient == 'h'):
                for j in range(ship_size):
                    board[starty][startx+j] = ship
            elif(orient == 'v'):
                for k in range(ship_size):
                    board[starty+k][startx] = ship
    return board