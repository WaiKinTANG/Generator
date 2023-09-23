import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
currentmaze = -1
maze= []
pos = [-1,-1]
lastmove = 'up'
def recorder(id,width,nearby):
    global currentmaze
    global maze
    global pos
    if id != currentmaze:
        currentmaze = id
        maze = [["#"]*(2*width-1)]*(2*width-1)
        for i in range(3):
            for j in range(3):
                maze[width-2+i][width-2+j] = nearby[i][j]
        pos = [(width - 1),(width - 1)]
    else:
        if (lastmove == 'up'):
            pos[0]-=1
            for i in range(3):
                    if maze[pos[0]-1][pos[1]-1+i] == "#":
                        maze[pos[0]-1][pos[1]-1+i]= nearby[0][i]
            
        elif (lastmove == 'down'):
            pos[0]+=1
            for i in range(3):
                    if maze[pos[0]+1][pos[1]-1+i] == "#":
                        maze[pos[0]+1][pos[1]-1+i]= nearby[2][i]
        elif (lastmove == 'left'):
            pos[1]-=1
            for i in range(3):
                    if maze[pos[0]-1+i][pos[1]-1] == "#":
                        maze[pos[0]-1+i][pos[1]-1]= nearby[i][0]
        elif (lastmove == 'right'):
            pos[1]+=1
            for i in range(3):
                    if maze[pos[0]-1+i][pos[1]+1] == "#":
                        maze[pos[0]-1+i][pos[1]+1]= nearby[i][2]
        maze[pos][pos] = 2
    for i in range(len(maze)):
        logging.info(maze[i])
        
def numpath(nearby):
    return (nearby[0][1]==1) + (nearby[1][0]==1) + (nearby[2][1]==1) + (nearby[1][2]==1)

def left(lastmove):
    if lastmove == 'up':
        return 'left'
    elif lastmove == 'left':
        return 'down'
    elif lastmove == 'down':
        return 'right' 
    elif lastmove == 'right':
        return 'up'
    
def check(nearby,move):
    if move == 'up':
        if nearby[0][1] == 0:
            return False
    elif move == 'left':
        if nearby[1][0] == 0:
            return False
    elif move == 'down':
        if nearby[2][1] == 0:
            return False
    elif move == 'right':
        if nearby[1][2] == 0:
            return False
    return True

def walker(num, nearby, lastmove):
    if (nearby[2][1] == 3) and lastmove != 'up':
        return 'down'

    elif (nearby[0][1] == 3) and lastmove != 'down':
        return 'up'

    elif (nearby[1][0] == 3) and lastmove != 'right':
        return 'left'
    
    elif (nearby[1][2] == 3) and lastmove != 'left':
        return 'right'
    
    if num <=2:
        if (nearby[2][1] == 1) and lastmove != 'up':
            return 'down'

        elif (nearby[0][1] == 1) and lastmove != 'down':
            return 'up'

        elif (nearby[1][0] == 1) and lastmove != 'right':
            return 'left'
    
        elif (nearby[1][2] == 1) and lastmove != 'left':
            return 'right'
        
    else:
        if (check(nearby,left(lastmove))):
            return left(lastmove)
        elif check(nearby,lastmove):
            return lastmove
        elif check(nearby, left(left(left(lastmove)))):
            return left(left(left(lastmove)))
        else:
            return left(left(lastmove))
         


@app.route('/maze', methods=['POST'])
def mazerun():
    global lastmove
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("nearby")
    width = data.get("mazeWidth")
    id = data.get("mazeID")
    logging.info("data sent for evaluation {}".format(input_value))
    recorder(id,width,input_value)
    result = dict()

    result["playerAction"] = walker(numpath(input_value),input_value,lastmove)

    
    
    
    lastmove = result["playerAction"]

    logging.info("My result :{}".format(result))
    return json.dumps(result)
