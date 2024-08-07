def countColors(face):
    numB, numG, numR, numV, numW, numY = 0, 0, 0, 0, 0, 0
    for i in range(8):
        for j in range(8):
            if(face[i][j] == "B"): numB = numB + 1
            if(face[i][j] == "G"): numG = numG + 1
            if(face[i][j] == "R"): numR = numR + 1
            if(face[i][j] == "V"): numV = numV + 1
            if(face[i][j] == "W"): numW = numW + 1
            if(face[i][j] == "Y"): numY = numY + 1
    return numB, numG, numR, numV, numW, numY

def evaluate(cube):
    score=0.0
    #count the number of equal colors in each face
    #print("Max colors     : ", end="")
    for face in range(6):
        numB, numG, numR, numV, numW, numY = 0, 0, 0, 0, 0, 0
        maximum = max(countColors(cube[face]))
        score = score + maximum/60
        #print(face+1, "=", maximum, ", ", end="")

    # verify all colors are accounted for
    numB, numG, numR, numV, numW, numY = 0, 0, 0, 0, 0, 0
    for face in range(6):
        colors = countColors(cube[face])
        numB, numG, numR, numV, numW, numY = numB+colors[0], numG+colors[1], numR+colors[2], numV+colors[3], numW+colors[4], numY+colors[5]
    # print("Counted colors : B =", numB, ", G =", numG, ", R =", numR, ", V =", numV, ", W =", numW, ", Y =", numY)
    if numB !=60 : score = -1
    if numR !=60 : score = -1
    if numY !=60 : score = -1
    if numW !=60 : score = -1
    if numG !=60 : score = -1
    if numV !=60 : score = -1

    # print("Score          :", "{0:0.3f}".format(score))
            
    return score
