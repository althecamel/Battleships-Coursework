from flask import Flask, request, render_template, jsonify, redirect, json
import components
import game_engine
import mp_game_engine

global data
#stores coordinates of where player has been attacked
player_hit_coords = []
firstRun = True
#create base empty board and ships
player_board = components.initialise_board()
player_ships = components.create_battleships()
#ai board using random placement algorithm
ai_board = components.initialise_board()
ai_ships = components.create_battleships()
ai_board = components.place_battleships(ai_board,ai_ships,'random')

app = Flask(__name__)

@app.route('/placement', methods=['GET','POST'])
def placement_interface():
    '''
    '''
    #global data
    if(request.method == 'GET'):
        return render_template('placement.html',ships=player_ships,board_size=len(player_board))
    elif(request.method == 'POST'):
        #convert json object to a dictionary of ships 
        data = request.get_json()
        with open('placement.json',mode='w') as json_file:
            json.dump(data,json_file)
        return jsonify({'message': 'Received'}), 200

@app.route('/', methods=['GET'])
def root():
    '''
    '''
    #change global variable of player board -updates every time its called
    #global ai_board
    #global board
    global firstRun
    global player
    if(request.method == 'GET'):
        #updated board with ships from 'data'
        if(firstRun == True):
            firstRun = False
            return redirect('http://127.0.0.1:5000/placement',code=302)
        #go to main game page
        player = components.place_battleships(player_board,player_ships,'custom')
        return render_template('main.html',player_board=player)

@app.route('/attack', methods=['GET'])
def process_attack():
    '''
    '''
    global player_hit_coords
    if(request.method == 'GET'):
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        coords = (x,y)
        #check hit on AI board
        if([x,y] in player_hit_coords):
            raise()
        else:
            player_hit_coords.append([x,y])
        #whether player hit an ai ship
        attack = game_engine.attack(coords,ai_board,player_ships)
        if(attack == True):
            
            hit = True
            player_hit_coords.append([x,y])
        else:
            hit = False
            player_hit_coords.append([x,y])
        #ai attack on player's board
        ai_attack = mp_game_engine.generate_attack(player)
        if(all(all(x is None for x in row) for row in ai_board) == True):
            finished = True 
            winner = 1
        elif(all(all(x is None for x in row) for row in player) == True):
            finished = True
            winner = 2
        else:
            finished = False
        if(finished == True):
            if(winner == 1):
                return jsonify({'hit': hit, 
                                'AI_Turn': ai_attack, 
                                'finished': 'Game Over, Player wins!'
                                })
            elif(winner == 2):
                return jsonify({'hit': hit,
                                'AI_Turn': ai_attack,
                                'finished': 'Game Over, AI wins!'})
        else:
            return jsonify({'hit': hit,
                            'AI_Turn': ai_attack
                            })

#global namespace
if(__name__ == '__main__'):
    app.run()