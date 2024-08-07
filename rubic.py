import rubic_plot
import rubic_move
import rubic_evaluate
import random
import matplotlib.pyplot as plt 
# import math

# 8 rows and 8 columns per face
rows, cols = 8, 8

# GitHub test modification commit
# define faces
#
#       F1
#    F2 F3 F4 F5
#       F6

F1=[['.' for i in range(cols)] for j in range(rows)]
F2=[[' ' for i in range(cols)] for j in range(rows)]
F3=[[' ' for i in range(cols)] for j in range(rows)]
F4=[[' ' for i in range(cols)] for j in range(rows)]
F5=[[' ' for i in range(cols)] for j in range(rows)]
F6=[[' ' for i in range(cols)] for j in range(rows)]

# enter start condition

F1=[[' ', 'R', 'R', 'Y', 'Y', 'Y', 'Y', ' '],
    ['R', 'R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['R', 'R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    [' ', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', ' ']]

F2=[[' ', 'W', 'W', 'G', 'G', 'G', 'G', ' '],
    ['W', 'W', 'W', 'G', 'G', 'G', 'G', 'G'],
    ['W', 'W', 'W', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'B', 'B', 'B'],
    ['G', 'G', 'G', 'G', 'G', 'B', 'B', 'B'],
    [' ', 'G', 'G', 'G', 'G', 'B', 'B', ' ']]

F3=[[' ', 'Y', 'Y', 'W', 'W', 'W', 'W', ' '],
    ['Y', 'Y', 'Y', 'W', 'W', 'W', 'W', 'W'],
    ['Y', 'Y', 'Y', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    [' ', 'W', 'W', 'W', 'W', 'W', 'W', ' ']]

F4=[[' ', 'V', 'V', 'B', 'B', 'B', 'B', ' '],
    ['V', 'V', 'V', 'B', 'B', 'B', 'B', 'B'],
    ['V', 'V', 'V', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'G', 'G', 'G'],
    ['B', 'B', 'B', 'B', 'B', 'G', 'G', 'G'],
    [' ', 'B', 'B', 'B', 'B', 'G', 'G', ' ']]

F5=[[' ', 'G', 'G', 'V', 'V', 'V', 'V', ' '],
    ['G', 'G', 'G', 'V', 'V', 'V', 'V', 'V'],
    ['G', 'G', 'G', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'R', 'R', 'R'],
    ['V', 'V', 'V', 'V', 'V', 'R', 'R', 'R'],
    [' ', 'V', 'V', 'V', 'V', 'R', 'R', ' ']]

F6=[[' ', 'B', 'B', 'R', 'R', 'R', 'R', ' '],
    ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'V', 'V', 'V'],
    ['R', 'R', 'R', 'R', 'R', 'V', 'V', 'V'],
    [' ', 'R', 'R', 'R', 'R', 'V', 'V', ' ']]


cube= F1, F2, F3, F4, F5, F6
rubic_plot.plot(cube)
rubic_evaluate.evaluate(cube)

# faces to choose from
faces=['front', 'back', 'left', 'right', 'top', 'bottom']
# directions to rotate
directions=['+', '-']

numMoves = 100
# compose a serie of moves
moves=[]

for i in range(numMoves):
    #random face
    randomFace = random.choice(faces)
    #random direction
    randomDirection = random.choice(directions)

    move =[randomFace, randomDirection]
    moves.append(move)

# Plot settings
marker='r.' # red point
size=2

# Perform the serie of moves
for i in range(numMoves):
    oldscore=rubic_evaluate.evaluate(cube)
    cube = rubic_move.rotate(cube, moves[i][0], moves[i][1])
    score=rubic_evaluate.evaluate(cube)
    if score == -1 and oldscore != -1:
        print("Color count error after move", moves[i][0], moves[i][1])
    plt.plot(i, score, marker, markersize=size) 

rubic_plot.plot(cube)

#plt.axis('equal')
#plt.ylim([0, 10])
# function to show the plot 
plt.show() 