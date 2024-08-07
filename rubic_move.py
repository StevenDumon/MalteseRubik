def rotate(cube, face, direction):
    #       F1
    #    F2 F3 F4 F5
    #       F6

    cols, rows = 8, 8
    
    temp=[['.' for i in range(cols)] for j in range(rows)]
    F1=cube[0]
    F2=cube[1]
    F3=cube[2]
    F4=cube[3]
    F5=cube[4]
    F6=cube[5]

    # print ("Rotate cube face", face, "in the", direction, "direction.")

    if face=="left":
        if direction=="-":
            # Rotate columns one (0), two (1) and three (2)
            for i in range(rows):
                temp[i][0] = F3[i][0]   # hold initial face F3 values of column 1
                temp[i][1] = F3[i][1]   # hold initial face F3 values of column 2
                temp[i][2] = F3[i][2]   # hold initial face F3 values of column 3
                
                F3[i][0] = F1[i][0]     # move column 1 face F1 to F3
                F3[i][1] = F1[i][1]     # move column 2 face F1 to F3
                F3[i][2] = F1[i][2]     # move column 3 face F1 to F3
                
                F1[i][0] = F5[i][0]     # move column 1 face F5 to F1
                F1[i][1] = F5[i][1]     # move column 2 face F5 to F1
                F1[i][2] = F5[i][2]     # move column 3 face F5 to F1
                
                F5[i][0] = F6[i][0]     # move column 1 face F6 to F5
                F5[i][1] = F6[i][1]     # move column 2 face F6 to F5
                F5[i][2] = F6[i][2]     # move column 3 face F6 to F5
                
                F6[i][0] = temp[i][0]   # move column 1 face F3 to F6, apply initial F3 values
                F6[i][1] = temp[i][1]   # move column 2 face F3 to F6, apply initial F3 values
                F6[i][2] = temp[i][2]   # move column 3 face F3 to F6, apply initial F3 values

            # Rotate middle columns (3 and 4), half-way
            temp[0][3], temp[1][3], temp[2][3], temp[3][3] = F3[0][3], F3[1][3], F3[2][3], F3[3][3]  # hold initial face F3 values of column 4 top half
            temp[0][4], temp[1][4], temp[2][4], temp[3][4] = F3[0][4], F3[1][4], F3[2][4], F3[3][4]  # hold initial face F3 values of column 5 top half

            F3[0][3], F3[1][3], F3[2][3], F3[3][3] = F1[4][3], F1[5][3], F1[6][3], F1[7][3]         # bottom half of F1 to top of F3
            F3[0][4], F3[1][4], F3[2][4], F3[3][4] = F1[4][4], F1[5][4], F1[6][4], F1[7][4]         # bottom half of F1 to top of F3
            F1[4][3], F1[5][3], F1[6][3], F1[7][3] = F1[0][3], F1[1][3], F1[2][3], F1[3][3]         # top half of F1 to bottom half of F1
            F1[4][4], F1[5][4], F1[6][4], F1[7][4] = F1[0][4], F1[1][4], F1[2][4], F1[3][4]         # top half of F1 to bottom half of F1
            F1[0][3], F1[1][3], F1[2][3], F1[3][3] = F5[4][3], F5[5][3], F5[6][3], F5[7][3]         # bottom half of F5 to top of F1
            F1[0][4], F1[1][4], F1[2][4], F1[3][4] = F5[4][4], F5[5][4], F5[6][4], F5[7][4]         # bottom half of F5 to top of F1
            F5[4][3], F5[5][3], F5[6][3], F5[7][3] = F5[0][3], F5[1][3], F5[2][3], F5[3][3]         # top half of F5 to bottom half of F5
            F5[4][4], F5[5][4], F5[6][4], F5[7][4] = F5[0][4], F5[1][4], F5[2][4], F5[3][4]         # top half of F5 to bottom half of F5
            F5[0][3], F5[1][3], F5[2][3], F5[3][3] = F6[4][3], F6[5][3], F6[6][3], F6[7][3]         # bottom half of F6 to top of F5
            F5[0][4], F5[1][4], F5[2][4], F5[3][4] = F6[4][4], F6[5][4], F6[6][4], F6[7][4]         # bottom half of F6 to top of F5
            F6[4][3], F6[5][3], F6[6][3], F6[7][3] = F6[0][3], F6[1][3], F6[2][3], F6[3][3]         # top half of F6 to bottom half of F6
            F6[4][4], F6[5][4], F6[6][4], F6[7][4] = F6[0][4], F6[1][4], F6[2][4], F6[3][4]         # top half of F6 to bottom half of F6
            F6[0][3], F6[1][3], F6[2][3], F6[3][3] = F3[4][3], F3[5][3], F3[6][3], F3[7][3]         # bottom half of F3 to top of F6
            F6[0][4], F6[1][4], F6[2][4], F6[3][4] = F3[4][4], F3[5][4], F3[6][4], F3[7][4]         # bottom half of F3 to top of F6
            F3[4][3], F3[5][3], F3[6][3], F3[7][3] = temp[0][3], temp[1][3], temp[2][3], temp[3][3] # initial top half of F3 to bottom half of F3
            F3[4][4], F3[5][4], F3[6][4], F3[7][4] = temp[0][4], temp[1][4], temp[2][4], temp[3][4] # initial top half of F6 to bottom half of F3

            # Rotate face F2, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F2[i][j]
                    F2[i][j] = F2[rows-i-1][j]
                    F2[rows-i-1][j] = F2[rows-i-1][cols-j-1]
                    F2[rows-i-1][cols-j-1] = F2[i][cols-j-1]
                    F2[i][cols-j-1] = temp[i][j]
        # end of move left -
        if direction=="+":
            # Rotate columns one (0), two (1) and three (2)
            for i in range(rows):
                temp[i][0] = F3[i][0]   # hold initial face F3 values of column 1
                temp[i][1] = F3[i][1]   # hold initial face F3 values of column 2
                temp[i][2] = F3[i][2]   # hold initial face F3 values of column 3
                
                F3[i][0] = F6[i][0]     # move column 1 face F6 to F3
                F3[i][1] = F6[i][1]     # move column 2 face F6 to F3
                F3[i][2] = F6[i][2]     # move column 3 face F6 to F3
                
                F6[i][0] = F5[i][0]     # move column 1 face F5 to F6
                F6[i][1] = F5[i][1]     # move column 2 face F5 to F6
                F6[i][2] = F5[i][2]     # move column 3 face F5 to F6
                
                F5[i][0] = F1[i][0]     # move column 1 face F1 to F5
                F5[i][1] = F1[i][1]     # move column 2 face F1 to F5
                F5[i][2] = F1[i][2]     # move column 3 face F1 to F5
                
                F1[i][0] = temp[i][0]   # move column 2 face F3 to F1, apply initial F3 values
                F1[i][1] = temp[i][1]   # move column 2 face F3 to F1, apply initial F3 values
                F1[i][2] = temp[i][2]   # move column 2 face F3 to F1, apply initial F3 values

            # Rotate middle columns (3 and 4), half-way
            #scenario:
            #   1. bottom half F3 to temp
            #   2. top half F6 to bottom half F3
            #   3. bottom half F6 to top half F6
            #   4. top half F5 to bottom half F6
            #   5. bottom half F5 to top half F5
            #   6. top half F1 to bottom half F5
            #   7. bottom half F1 to top half F1
            #   8. top half F3 to bottom half F1
            #   9. temp to top half F3

            temp[4][3], temp[5][3], temp[6][3], temp[7][3] = F3[4][3], F3[5][3], F3[6][3], F3[7][3]  # 1. bottom half F3 to temp
            temp[4][4], temp[5][4], temp[6][4], temp[7][4] = F3[4][4], F3[5][4], F3[6][4], F3[7][4]  # 1. bottom half F3 to temp

            F3[4][3], F3[5][3], F3[6][3], F3[7][3] = F6[0][3], F6[1][3], F6[2][3], F6[3][3]         # 2. top half F6 to bottom half F3
            F3[4][4], F3[5][4], F3[6][4], F3[7][4] = F6[0][4], F6[1][4], F6[2][4], F6[3][4]         # 2. top half F6 to bottom half F3

            F6[0][3], F6[1][3], F6[2][3], F6[3][3] = F6[4][3], F6[5][3], F6[6][3], F6[7][3]         # 3. bottom half F6 to top half F6
            F6[0][4], F6[1][4], F6[2][4], F6[3][4] = F6[4][4], F6[5][4], F6[6][4], F6[7][4]         # 3. bottom half F6 to top half F6

            F6[4][3], F6[5][3], F6[6][3], F6[7][3] = F5[0][3], F5[1][3], F5[2][3], F5[3][3]         # 4. top half F5 to bottom half F6
            F6[4][4], F6[5][4], F6[6][4], F6[7][4] = F5[0][4], F5[1][4], F5[2][4], F5[3][4]         # 4. top half F5 to bottom half F6

            F5[0][3], F5[1][3], F5[2][3], F5[3][3] = F5[4][3], F5[5][3], F5[6][3], F5[7][3]         # 5. bottom half F5 to top half F5
            F5[0][4], F5[1][4], F5[2][4], F5[3][4] = F5[4][4], F5[5][4], F5[6][4], F5[7][4]         # 5. bottom half F5 to top half F5

            F5[4][3], F5[5][3], F5[6][3], F5[7][3] = F1[0][3], F1[1][3], F1[2][3], F1[3][3]         # 6. top half F1 to bottom half F5
            F5[4][4], F5[5][4], F5[6][4], F5[7][4] = F1[0][4], F1[1][4], F1[2][4], F1[3][4]         # 6. top half F1 to bottom half F5

            F1[0][3], F1[1][3], F1[2][3], F1[3][3] = F1[4][3], F1[5][3], F1[6][3], F1[7][3]         # 7. bottom half F1 to top half F1
            F1[0][4], F1[1][4], F1[2][4], F1[3][4] = F1[4][4], F1[5][4], F1[6][4], F1[7][4]         # 7. bottom half F1 to top half F1

            F1[4][3], F1[5][3], F1[6][3], F1[7][3] = F3[0][3], F3[1][3], F3[2][3], F3[3][3]         # 8. top half F3 to bottom half F1
            F1[4][4], F1[5][4], F1[6][4], F1[7][4] = F3[0][4], F3[1][4], F3[2][4], F3[3][4]         # 8. top half F3 to bottom half F1

            F3[0][3], F3[1][3], F3[2][3], F3[3][3] = temp[4][3], temp[5][3], temp[6][3], temp[7][3] # 9. temp to top half F3
            F3[0][4], F3[1][4], F3[2][4], F3[3][4] = temp[4][3], temp[5][3], temp[6][3], temp[7][3] # 9. temp to top half F3

            # Rotate face F2, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F2[i][j]
                    F2[i][j] = F2[i][cols-j-1]
                    F2[i][cols-j-1] = F2[rows-i-1][cols-j-1]
                    F2[rows-i-1][cols-j-1] = F2[rows-i-1][j]
                    F2[rows-i-1][j] = temp[i][j]
        # end of move left +
    #end of if face to rotate is left
    if face=="right":
        if direction=="-":
            # Rotate columns six (5), seven (6) and eight (7)
            for i in range(rows):
                temp[i][5] = F3[i][5]  # hold initial face F3 values of column 5
                temp[i][6] = F3[i][6]  # hold initial face F3 values of column 6
                temp[i][7] = F3[i][7]  # hold initial face F3 values of column 7
                
                F3[i][5] = F1[i][5]    # move column 5 face F1 to F3
                F3[i][6] = F1[i][6]    # move column 6 face F1 to F3
                F3[i][7] = F1[i][7]    # move column 7 face F1 to F3
                
                F1[i][5] = F5[i][5]    # move column 5 face F5 to F1
                F1[i][6] = F5[i][6]    # move column 6 face F5 to F1
                F1[i][7] = F5[i][7]    # move column 7 face F5 to F1
                
                F5[i][5] = F6[i][5]    # move column 5 face F6 to F5
                F5[i][6] = F6[i][6]    # move column 6 face F6 to F5
                F5[i][7] = F6[i][7]    # move column 7 face F6 to F5
                
                F6[i][5] = temp[i][5]  # move column 5 face F3 to F6, apply initial F3 values
                F6[i][6] = temp[i][6]  # move column 6 face F3 to F6, apply initial F3 values
                F6[i][7] = temp[i][7]  # move column 7 face F3 to F6, apply initial F3 values

            # Rotate middle columns (3 and 4), half-way
            temp[0][3], temp[1][3], temp[2][3], temp[3][3] = F3[0][3], F3[1][3], F3[2][3], F3[3][3]  # hold initial face F3 values of column 4 top half
            temp[0][4], temp[1][4], temp[2][4], temp[3][4] = F3[0][4], F3[1][4], F3[2][4], F3[3][4]  # hold initial face F3 values of column 5 top half

            F3[0][3], F3[1][3], F3[2][3], F3[3][3] = F1[4][3], F1[5][3], F1[6][3], F1[7][3]         # bottom half of F1 to top of F3
            F3[0][4], F3[1][4], F3[2][4], F3[3][4] = F1[4][4], F1[5][4], F1[6][4], F1[7][4]         # bottom half of F1 to top of F3
            F1[4][3], F1[5][3], F1[6][3], F1[7][3] = F1[0][3], F1[1][3], F1[2][3], F1[3][3]         # top half of F1 to bottom half of F1
            F1[4][4], F1[5][4], F1[6][4], F1[7][4] = F1[0][4], F1[1][4], F1[2][4], F1[3][4]         # top half of F1 to bottom half of F1
            F1[0][3], F1[1][3], F1[2][3], F1[3][3] = F5[4][3], F5[5][3], F5[6][3], F5[7][3]         # bottom half of F5 to top of F1
            F1[0][4], F1[1][4], F1[2][4], F1[3][4] = F5[4][4], F5[5][4], F5[6][4], F5[7][4]         # bottom half of F5 to top of F1
            F5[4][3], F5[5][3], F5[6][3], F5[7][3] = F5[0][3], F5[1][3], F5[2][3], F5[3][3]         # top half of F5 to bottom half of F5
            F5[4][4], F5[5][4], F5[6][4], F5[7][4] = F5[0][4], F5[1][4], F5[2][4], F5[3][4]         # top half of F5 to bottom half of F5
            F5[0][3], F5[1][3], F5[2][3], F5[3][3] = F6[4][3], F6[5][3], F6[6][3], F6[7][3]         # bottom half of F6 to top of F5
            F5[0][4], F5[1][4], F5[2][4], F5[3][4] = F6[4][4], F6[5][4], F6[6][4], F6[7][4]         # bottom half of F6 to top of F5
            F6[4][3], F6[5][3], F6[6][3], F6[7][3] = F6[0][3], F6[1][3], F6[2][3], F6[3][3]         # top half of F6 to bottom half of F6
            F6[4][4], F6[5][4], F6[6][4], F6[7][4] = F6[0][4], F6[1][4], F6[2][4], F6[3][4]         # top half of F6 to bottom half of F6
            F6[0][3], F6[1][3], F6[2][3], F6[3][3] = F3[4][3], F3[5][3], F3[6][3], F3[7][3]         # bottom half of F3 to top of F6
            F6[0][4], F6[1][4], F6[2][4], F6[3][4] = F3[4][4], F3[5][4], F3[6][4], F3[7][4]         # bottom half of F3 to top of F6
            F3[4][3], F3[5][3], F3[6][3], F3[7][3] = temp[0][3], temp[1][3], temp[2][3], temp[3][3] # initial top half of F3 to bottom half of F3
            F3[4][4], F3[5][4], F3[6][4], F3[7][4] = temp[0][4], temp[1][4], temp[2][4], temp[3][4] # initial top half of F6 to bottom half of F3

            # Rotate face F4, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F4[i][j]
                    F4[i][j] = F4[i][cols-j-1]
                    F4[i][cols-j-1] = F4[rows-i-1][cols-j-1]
                    F4[rows-i-1][cols-j-1] = F4[rows-i-1][j]
                    F4[rows-i-1][j] = temp[i][j]            
        # end of move right -
        if direction=="+":
            # Rotate columns six (5), seven (6) and eight (7)
            for i in range(rows):
                temp[i][5] = F3[i][5]   # hold initial face F3 values of column 1
                temp[i][6] = F3[i][6]   # hold initial face F3 values of column 2
                temp[i][7] = F3[i][7]   # hold initial face F3 values of column 3
                
                F3[i][5] = F6[i][5]     # move column 1 face F6 to F3
                F3[i][6] = F6[i][6]     # move column 2 face F6 to F3
                F3[i][7] = F6[i][7]     # move column 3 face F6 to F3
                
                F6[i][5] = F5[i][5]     # move column 1 face F5 to F6
                F6[i][6] = F5[i][6]     # move column 2 face F5 to F6
                F6[i][7] = F5[i][7]     # move column 3 face F5 to F6
                
                F5[i][5] = F1[i][5]     # move column 1 face F1 to F5
                F5[i][6] = F1[i][6]     # move column 2 face F1 to F5
                F5[i][7] = F1[i][7]     # move column 3 face F1 to F5
                
                F1[i][5] = temp[i][5]   # move column 2 face F3 to F1, apply initial F3 values
                F1[i][6] = temp[i][6]   # move column 2 face F3 to F1, apply initial F3 values
                F1[i][7] = temp[i][7]   # move column 2 face F3 to F1, apply initial F3 values

            # Rotate middle columns (3 and 4), half-way
            #scenario:
            #   1. bottom half F3 to temp
            #   2. top half F6 to bottom half F3
            #   3. bottom half F6 to top half F6
            #   4. top half F5 to bottom half F6
            #   5. bottom half F5 to top half F5
            #   6. top half F1 to bottom half F5
            #   7. bottom half F1 to top half F1
            #   8. top half F3 to bottom half F1
            #   9. temp to top half F3

            temp[4][3], temp[5][3], temp[6][3], temp[7][3] = F3[4][3], F3[5][3], F3[6][3], F3[7][3]  # 1. bottom half F3 to temp
            temp[4][4], temp[5][4], temp[6][4], temp[7][4] = F3[4][4], F3[5][4], F3[6][4], F3[7][4]  # 1. bottom half F3 to temp

            F3[4][3], F3[5][3], F3[6][3], F3[7][3] = F6[0][3], F6[1][3], F6[2][3], F6[3][3]         # 2. top half F6 to bottom half F3
            F3[4][4], F3[5][4], F3[6][4], F3[7][4] = F6[0][4], F6[1][4], F6[2][4], F6[3][4]         # 2. top half F6 to bottom half F3

            F6[0][3], F6[1][3], F6[2][3], F6[3][3] = F6[4][3], F6[5][3], F6[6][3], F6[7][3]         # 3. bottom half F6 to top half F6
            F6[0][4], F6[1][4], F6[2][4], F6[3][4] = F6[4][4], F6[5][4], F6[6][4], F6[7][4]         # 3. bottom half F6 to top half F6

            F6[4][3], F6[5][3], F6[6][3], F6[7][3] = F5[0][3], F5[1][3], F5[2][3], F5[3][3]         # 4. top half F5 to bottom half F6
            F6[4][4], F6[5][4], F6[6][4], F6[7][4] = F5[0][4], F5[1][4], F5[2][4], F5[3][4]         # 4. top half F5 to bottom half F6

            F5[0][3], F5[1][3], F5[2][3], F5[3][3] = F5[4][3], F5[5][3], F5[6][3], F5[7][3]         # 5. bottom half F5 to top half F5
            F5[0][4], F5[1][4], F5[2][4], F5[3][4] = F5[4][4], F5[5][4], F5[6][4], F5[7][4]         # 5. bottom half F5 to top half F5

            F5[4][3], F5[5][3], F5[6][3], F5[7][3] = F1[0][3], F1[1][3], F1[2][3], F1[3][3]         # 6. top half F1 to bottom half F5
            F5[4][4], F5[5][4], F5[6][4], F5[7][4] = F1[0][4], F1[1][4], F1[2][4], F1[3][4]         # 6. top half F1 to bottom half F5

            F1[0][3], F1[1][3], F1[2][3], F1[3][3] = F1[4][3], F1[5][3], F1[6][3], F1[7][3]         # 7. bottom half F1 to top half F1
            F1[0][4], F1[1][4], F1[2][4], F1[3][4] = F1[4][4], F1[5][4], F1[6][4], F1[7][4]         # 7. bottom half F1 to top half F1

            F1[4][3], F1[5][3], F1[6][3], F1[7][3] = F3[0][3], F3[1][3], F3[2][3], F3[3][3]         # 8. top half F3 to bottom half F1
            F1[4][4], F1[5][4], F1[6][4], F1[7][4] = F3[0][4], F3[1][4], F3[2][4], F3[3][4]         # 8. top half F3 to bottom half F1

            F3[0][3], F3[1][3], F3[2][3], F3[3][3] = temp[4][3], temp[5][3], temp[6][3], temp[7][3] # 9. temp to top half F3
            F3[0][4], F3[1][4], F3[2][4], F3[3][4] = temp[4][3], temp[5][3], temp[6][3], temp[7][3] # 9. temp to top half F3

            # Rotate face F4, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F4[i][j]
                    F4[i][j] = F4[rows-i-1][j]
                    F4[rows-i-1][j] = F4[rows-i-1][cols-j-1]
                    F4[rows-i-1][cols-j-1] = F4[i][cols-j-1]
                    F4[i][cols-j-1] = temp[i][j]

        # end of move right +
    #end of if face to rotate is right
    if face=="front":
        if direction=="-":
            # Rotate rows six (5), seven (6) and eight (7) of F1
            for j in range(cols):
                temp[5][j] = F1[5][j]   # hold initial face F1 values of column 6
                temp[6][j] = F1[6][j]   # hold initial face F1 values of column 7
                temp[7][j] = F1[7][j]   # hold initial face F1 values of column 8
                
                F1[5][j] = F2[j][5]     # move F2 colum to F1 row
                F1[6][j] = F2[j][6]     # move F2 colum to F1 row
                F1[7][j] = F2[j][7]     # move F2 colum to F1 row
                
                F2[j][5] = F6[2][j]     # move F6 row to F2 column
                F2[j][6] = F6[1][j]     # move F6 row to F2 column
                F2[j][7] = F6[0][j]     # move F6 row to F2 column
                
                F6[2][j] = F4[cols-j-1][2]     # move F4 column to F6 row
                F6[1][j] = F4[cols-j-1][1]     # move F4 column to F6 row
                F6[0][j] = F4[cols-j-1][0]     # move F4 column to F6 row
                
                F4[cols-j-1][2] = temp[5][j]   # move column 6 face F1 to F4, apply initial F1 values
                F4[cols-j-1][1] = temp[6][j]   # move column 7 face F1 to F4, apply initial F1 values
                F4[cols-j-1][0] = temp[7][j]   # move column 8 face F1 to F4, apply initial F1 values

            # Rotate middle columns/rows (3 and 4), half-way
            # Scenario
            # 1. F1 left half to temp
            # 2. F2 top half to F1 left half
            # 3. F2 bottom half to F2 top half
            # 4. F6 left half to F2 bottom half
            # 5. F6 right half to F6 left half
            # 6. F4 bottom half to F6 right half
            # 7. F4 top half to F4 bottom half
            # 8. F1 right half to F4 top half
            # 9. temp to F1 right half

            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F1[3][0], F1[3][1], F1[3][2], F1[3][3]  # 1. F1 left half to temp
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F1[4][0], F1[4][1], F1[4][2], F1[4][3]  # 1. F1 left half to temp

            F1[3][0], F1[3][1], F1[3][2], F1[3][3] = F2[0][3], F2[1][3], F2[2][3], F2[3][3]          # 2. F2 top half to F1 left half
            F1[4][0], F1[4][1], F1[4][2], F1[4][3] = F2[0][4], F2[1][4], F2[2][4], F2[3][4]          # 2. F2 top half to F1 left half

            F2[0][3], F2[1][3], F2[2][3], F2[3][3] = F2[4][3], F2[5][3], F2[6][3], F2[7][3]          # 3. F2 bottom half to F2 top half
            F2[0][4], F2[1][4], F2[2][4], F2[3][4] = F2[4][4], F2[5][4], F2[6][4], F2[7][4]          # 3. F2 bottom half to F2 top half

            F2[4][3], F2[5][3], F2[6][3], F2[7][3] = F6[3][0], F6[3][1], F6[3][2], F6[3][3]          # 4. F6 left half to F2 bottom half
            F2[4][4], F2[5][4], F2[6][4], F2[7][4] = F6[4][0], F6[4][1], F6[4][2], F6[4][3]          # 4. F6 left half to F2 bottom half

            F6[3][0], F6[3][1], F6[3][2], F6[3][3] = F6[3][4], F6[3][5], F6[3][6], F6[3][7]          # 5. F6 right half to F6 left half
            F6[4][0], F6[4][1], F6[4][2], F6[4][3] = F6[4][4], F6[4][5], F6[4][6], F6[4][7]          # 5. F6 right half to F6 left half

            F6[3][4], F6[3][5], F6[3][6], F6[3][7] = F4[4][3], F4[5][3], F4[6][3], F4[7][3]          # 6. F4 bottom half to F6 right half
            F6[4][4], F6[4][5], F6[4][6], F6[4][7] = F4[4][4], F4[5][4], F4[6][4], F4[7][4]          # 6. F4 bottom half to F6 right half

            F4[4][3], F4[5][3], F4[6][3], F4[7][3] = F4[0][3], F4[1][3], F4[2][3], F4[3][3]          # 7. F4 top half to F4 bottom half
            F4[4][4], F4[5][4], F4[6][4], F4[7][4] = F4[0][4], F4[1][4], F4[2][4], F4[3][4]          # 7. F4 top half to F4 bottom half

            F4[0][3], F4[1][3], F4[2][3], F4[3][3] = F1[3][4], F1[3][5], F1[3][6], F1[3][7]          # 8. F1 right half to F4 top half
            F4[0][4], F4[1][4], F4[2][4], F4[3][4] = F1[4][4], F1[4][5], F1[4][6], F1[4][7]          # 8. F1 right half to F4 top half

            F1[3][4], F1[3][5], F1[3][6], F1[3][7] = temp[3][0], temp[3][1], temp[3][2], temp[3][3]  # 9. temp to F1 right half
            F1[4][4], F1[4][5], F1[4][6], F1[4][7] = temp[4][0], temp[4][1], temp[4][2], temp[4][3]  # 9. temp to F1 right half
            # Rotate face F3, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F3[i][j]
                    F3[i][j] = F3[rows-i-1][j]
                    F3[rows-i-1][j] = F3[rows-i-1][cols-j-1]
                    F3[rows-i-1][cols-j-1] = F3[i][cols-j-1]
                    F3[i][cols-j-1] = temp[i][j]

        # end of move front -
        if direction=="+":
            # Rotate rows six (5), seven (6) and eight (7) of F1
            for j in range(cols):
                temp[5][j] = F1[5][j]   # hold initial face F1 values of column 6
                temp[6][j] = F1[6][j]   # hold initial face F1 values of column 7
                temp[7][j] = F1[7][j]   # hold initial face F1 values of column 8
                
                F1[5][j] = F4[j][2]     # move column 6 face F4 to F1
                F1[6][j] = F4[j][1]     # move column 7 face F4 to F1
                F1[7][j] = F4[j][0]     # move column 8 face F4 to F1
                
                F4[j][2] = F6[2][cols-j-1]     # move column 6 face F6 to F4
                F4[j][1] = F6[1][cols-j-1]     # move column 7 face F6 to F4
                F4[j][0] = F6[0][cols-j-1]     # move column 8 face F6 to F4
                
                F6[2][cols-j-1] = F2[cols-j-1][5]     # move column 6 face F2 to F6
                F6[1][cols-j-1] = F2[cols-j-1][6]     # move column 7 face F2 to F6
                F6[0][cols-j-1] = F2[cols-j-1][7]     # move column 8 face F2 to F6
                
                F2[cols-j-1][5] = temp[5][j]   # move column 6 face F1 to F2, apply initial F1 values
                F2[cols-j-1][6] = temp[6][j]   # move column 7 face F1 to F2, apply initial F1 values
                F2[cols-j-1][7] = temp[7][j]   # move column 8 face F1 to F2, apply initial F1 values

            # Rotate middle columns (3 and 4), half-way
            # Scenario
            # 1. F1 left half to temp
            # 2. F1 right half to F1 left half
            # 3. F4 top half to F1 right half
            # 4. F4 bottom half to F4 top half
            # 5. F6 right half to F4 bottom half
            # 6. F6 left half to F6 right half
            # 7. F2 bottom half to F6 left half
            # 8. F2 top half to F2 bottom half
            # 9. temp to F2 top half

            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F1[3][0], F1[3][1], F1[3][2], F1[3][3]  # 1. F1 left half to temp
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F1[4][0], F1[4][1], F1[4][2], F1[4][3]  # 1. F1 left half to temp

            F1[3][0], F1[3][1], F1[3][2], F1[3][3] = F1[3][4], F1[3][5], F1[3][6], F1[3][7]          # 2. F1 right half to F1 left half
            F1[4][0], F1[4][1], F1[4][2], F1[4][3] = F1[4][4], F1[4][5], F1[4][6], F1[4][7]          # 2. F1 right half to F1 left half

            F1[3][4], F1[3][5], F1[3][6], F1[3][7] = F4[0][3], F4[1][3], F4[2][3], F4[3][3]          # 3. F4 top half to F1 right half
            F1[4][4], F1[4][5], F1[4][6], F1[4][7] = F4[0][4], F4[1][4], F4[2][4], F4[3][4]          # 3. F4 top half to F1 right half

            F4[0][3], F4[1][3], F4[2][3], F4[3][3] = F4[4][3], F4[5][3], F4[6][3], F4[7][3]          # 4. F4 bottom half to F4 top half
            F4[0][4], F4[1][4], F4[2][4], F4[3][4] = F4[4][4], F4[5][4], F4[6][4], F4[7][4]          # 4. F4 bottom half to F4 top half

            F4[4][3], F4[5][3], F4[6][3], F4[7][3] = F6[3][4], F6[3][5], F6[3][6], F6[3][7]          # 5. F6 right half to F4 bottom half
            F4[4][4], F4[5][4], F4[6][4], F4[7][4] = F6[4][4], F6[4][5], F6[4][6], F6[4][7]          # 5. F6 right half to F4 bottom half

            F6[3][4], F6[3][5], F6[3][6], F6[3][7] = F6[3][0], F6[3][1], F6[3][2], F6[3][3]          # 6. F6 left half to F6 right half
            F6[4][4], F6[4][5], F6[4][6], F6[4][7] = F6[4][0], F6[4][1], F6[4][2], F6[4][3]          # 6. F6 left half to F6 right half

            F6[3][0], F6[3][1], F6[3][2], F6[3][3] = F2[4][3], F2[5][3], F2[6][3], F2[7][3]          # 7. F2 bottom half to F6 left half
            F6[4][0], F6[4][1], F6[4][2], F6[4][3] = F2[4][4], F2[5][4], F2[6][4], F2[7][4]          # 7. F2 bottom half to F6 left half

            F2[4][3], F2[5][3], F2[6][3], F2[7][3] = F2[0][3], F2[1][3], F2[2][3], F2[3][3]          # 8. F2 top half to F2 bottom half
            F2[4][4], F2[5][4], F2[6][4], F2[7][4] = F2[0][4], F2[1][4], F2[2][4], F2[3][4]          # 8. F2 top half to F2 bottom half

            F2[0][3], F2[1][3], F2[2][3], F2[3][3] = temp[3][0], temp[3][1], temp[3][2], temp[3][3]  # 9. temp to F2 top half
            F2[0][4], F2[1][4], F2[2][4], F2[3][4] = temp[4][0], temp[4][1], temp[4][2], temp[4][3]  # 9. temp to F2 top half

            # Rotate face F3, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F3[i][j]
                    F3[i][j] = F3[i][cols-j-1]
                    F3[i][cols-j-1] = F3[rows-i-1][cols-j-1]
                    F3[rows-i-1][cols-j-1] = F3[rows-i-1][j]
                    F3[rows-i-1][j] = temp[i][j]
        # end of move front +
    #end of if face to rotate is front
    if face=="back":
        if direction=="-":
            for j in range(cols):
                temp[0][j] = F1[0][j]   # hold initial face F1 values of column 6
                temp[1][j] = F1[1][j]   # hold initial face F1 values of column 7
                temp[2][j] = F1[2][j]   # hold initial face F1 values of column 8
                
                F1[0][j] = F2[cols-j-1][0]     # move F2 colum to F1 row
                F1[1][j] = F2[cols-j-1][1]     # move F2 colum to F1 row
                F1[2][j] = F2[cols-j-1][2]     # move F2 colum to F1 row
                
                F2[cols-j-1][0] = F6[7][cols-j-1]     # move F6 row to F2 column
                F2[cols-j-1][1] = F6[6][cols-j-1]     # move F6 row to F2 column
                F2[cols-j-1][2] = F6[5][cols-j-1]     # move F6 row to F2 column
                
                F6[7][cols-j-1] = F4[j][7]     # move F4 column to F6 row
                F6[6][cols-j-1] = F4[j][6]     # move F4 column to F6 row
                F6[5][cols-j-1] = F4[j][5]     # move F4 column to F6 row
                
                F4[j][7] = temp[0][j]   # move column 6 face F1 to F4, apply initial F1 values
                F4[j][6] = temp[1][j]   # move column 7 face F1 to F4, apply initial F1 values
                F4[j][5] = temp[2][j]   # move column 8 face F1 to F4, apply initial F1 values

            # Rotate middle columns/rows (3 and 4), half-way
            # Scenario
            # 1. F1 left half to temp
            # 2. F2 top half to F1 left half
            # 3. F2 bottom half to F2 top half
            # 4. F6 left half to F2 bottom half
            # 5. F6 right half to F6 left half
            # 6. F4 bottom half to F6 right half
            # 7. F4 top half to F4 bottom half
            # 8. F1 right half to F4 top half
            # 9. temp to F1 right half

            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F1[3][0], F1[3][1], F1[3][2], F1[3][3]  # 1. F1 left half to temp
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F1[4][0], F1[4][1], F1[4][2], F1[4][3]  # 1. F1 left half to temp

            F1[3][0], F1[3][1], F1[3][2], F1[3][3] = F2[0][3], F2[1][3], F2[2][3], F2[3][3]          # 2. F2 top half to F1 left half
            F1[4][0], F1[4][1], F1[4][2], F1[4][3] = F2[0][4], F2[1][4], F2[2][4], F2[3][4]          # 2. F2 top half to F1 left half

            F2[0][3], F2[1][3], F2[2][3], F2[3][3] = F2[4][3], F2[5][3], F2[6][3], F2[7][3]          # 3. F2 bottom half to F2 top half
            F2[0][4], F2[1][4], F2[2][4], F2[3][4] = F2[4][4], F2[5][4], F2[6][4], F2[7][4]          # 3. F2 bottom half to F2 top half

            F2[4][3], F2[5][3], F2[6][3], F2[7][3] = F6[3][0], F6[3][1], F6[3][2], F6[3][3]          # 4. F6 left half to F2 bottom half
            F2[4][4], F2[5][4], F2[6][4], F2[7][4] = F6[4][0], F6[4][1], F6[4][2], F6[4][3]          # 4. F6 left half to F2 bottom half

            F6[3][0], F6[3][1], F6[3][2], F6[3][3] = F6[3][4], F6[3][5], F6[3][6], F6[3][7]          # 5. F6 right half to F6 left half
            F6[4][0], F6[4][1], F6[4][2], F6[4][3] = F6[4][4], F6[4][5], F6[4][6], F6[4][7]          # 5. F6 right half to F6 left half

            F6[3][4], F6[3][5], F6[3][6], F6[3][7] = F4[4][3], F4[5][3], F4[6][3], F4[7][3]          # 6. F4 bottom half to F6 right half
            F6[4][4], F6[4][5], F6[4][6], F6[4][7] = F4[4][4], F4[5][4], F4[6][4], F4[7][4]          # 6. F4 bottom half to F6 right half

            F4[4][3], F4[5][3], F4[6][3], F4[7][3] = F4[0][3], F4[1][3], F4[2][3], F4[3][3]          # 7. F4 top half to F4 bottom half
            F4[4][4], F4[5][4], F4[6][4], F4[7][4] = F4[0][4], F4[1][4], F4[2][4], F4[3][4]          # 7. F4 top half to F4 bottom half

            F4[0][3], F4[1][3], F4[2][3], F4[3][3] = F1[3][4], F1[3][5], F1[3][6], F1[3][7]          # 8. F1 right half to F4 top half
            F4[0][4], F4[1][4], F4[2][4], F4[3][4] = F1[4][4], F1[4][5], F1[4][6], F1[4][7]          # 8. F1 right half to F4 top half

            F1[3][4], F1[3][5], F1[3][6], F1[3][7] = temp[3][0], temp[3][1], temp[3][2], temp[3][3]  # 9. temp to F1 right half
            F1[4][4], F1[4][5], F1[4][6], F1[4][7] = temp[4][0], temp[4][1], temp[4][2], temp[4][3]  # 9. temp to F1 right half
            # Rotate face F5, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F5[i][j]
                    F5[i][j] = F5[rows-i-1][j]
                    F5[rows-i-1][j] = F5[rows-i-1][cols-j-1]
                    F5[rows-i-1][cols-j-1] = F5[i][cols-j-1]
                    F5[i][cols-j-1] = temp[i][j]


        # end of move back -
        if direction=="+":
            # Rotate rows one (0), two (1) and three (2) of F1
            for j in range(cols):
                temp[0][j] = F1[0][j]   # hold initial face F1
                temp[1][j] = F1[1][j]   # hold initial face F1
                temp[2][j] = F1[2][j]   # hold initial face F1
                
                F1[0][j] = F4[j][7]     # move F4 column to row F1
                F1[1][j] = F4[j][6]     # move F4 column to row F1
                F1[2][j] = F4[j][5]     # move F4 column to row F1
                
                F4[j][7] = F6[7][cols-j-1]     # move F6 row to F4 column
                F4[j][6] = F6[6][cols-j-1]     # move F6 row to F4 column
                F4[j][5] = F6[5][cols-j-1]     # move F6 row to F4 column
                
                F6[7][cols-j-1] = F2[cols-j-1][0]     # move F2 column to F6 row
                F6[6][cols-j-1] = F2[cols-j-1][1]     # move F2 column to F6 row
                F6[5][cols-j-1] = F2[cols-j-1][2]     # move F2 column to F6 row
                
                F2[cols-j-1][0] = temp[0][j]   # move column 6 face F1 to F2, apply initial F1 values
                F2[cols-j-1][1] = temp[1][j]   # move column 7 face F1 to F2, apply initial F1 values
                F2[cols-j-1][2] = temp[2][j]   # move column 8 face F1 to F2, apply initial F1 values

            # Rotate middle columns (3 and 4), half-way
            # Scenario
            # 1. F1 left half to temp
            # 2. F1 right half to F1 left half
            # 3. F4 top half to F1 right half
            # 4. F4 bottom half to F4 top half
            # 5. F6 right half to F4 bottom half
            # 6. F6 left half to F6 right half
            # 7. F2 bottom half to F6 left half
            # 8. F2 top half to F2 bottom half
            # 9. temp to F2 top half

            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F1[3][0], F1[3][1], F1[3][2], F1[3][3]  # 1. F1 left half to temp
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F1[4][0], F1[4][1], F1[4][2], F1[4][3]  # 1. F1 left half to temp

            F1[3][0], F1[3][1], F1[3][2], F1[3][3] = F1[3][4], F1[3][5], F1[3][6], F1[3][7]          # 2. F1 right half to F1 left half
            F1[4][0], F1[4][1], F1[4][2], F1[4][3] = F1[4][4], F1[4][5], F1[4][6], F1[4][7]          # 2. F1 right half to F1 left half

            F1[3][4], F1[3][5], F1[3][6], F1[3][7] = F4[0][3], F4[1][3], F4[2][3], F4[3][3]          # 3. F4 top half to F1 right half
            F1[4][4], F1[4][5], F1[4][6], F1[4][7] = F4[0][4], F4[1][4], F4[2][4], F4[3][4]          # 3. F4 top half to F1 right half

            F4[0][3], F4[1][3], F4[2][3], F4[3][3] = F4[4][3], F4[5][3], F4[6][3], F4[7][3]          # 4. F4 bottom half to F4 top half
            F4[0][4], F4[1][4], F4[2][4], F4[3][4] = F4[4][4], F4[5][4], F4[6][4], F4[7][4]          # 4. F4 bottom half to F4 top half

            F4[4][3], F4[5][3], F4[6][3], F4[7][3] = F6[3][4], F6[3][5], F6[3][6], F6[3][7]          # 5. F6 right half to F4 bottom half
            F4[4][4], F4[5][4], F4[6][4], F4[7][4] = F6[4][4], F6[4][5], F6[4][6], F6[4][7]          # 5. F6 right half to F4 bottom half

            F6[3][4], F6[3][5], F6[3][6], F6[3][7] = F6[3][0], F6[3][1], F6[3][2], F6[3][3]          # 6. F6 left half to F6 right half
            F6[4][4], F6[4][5], F6[4][6], F6[4][7] = F6[4][0], F6[4][1], F6[4][2], F6[4][3]          # 6. F6 left half to F6 right half

            F6[3][0], F6[3][1], F6[3][2], F6[3][3] = F2[4][3], F2[5][3], F2[6][3], F2[7][3]          # 7. F2 bottom half to F6 left half
            F6[4][0], F6[4][1], F6[4][2], F6[4][3] = F2[4][4], F2[5][4], F2[6][4], F2[7][4]          # 7. F2 bottom half to F6 left half

            F2[4][3], F2[5][3], F2[6][3], F2[7][3] = F2[0][3], F2[1][3], F2[2][3], F2[3][3]          # 8. F2 top half to F2 bottom half
            F2[4][4], F2[5][4], F2[6][4], F2[7][4] = F2[0][4], F2[1][4], F2[2][4], F2[3][4]          # 8. F2 top half to F2 bottom half

            F2[0][3], F2[1][3], F2[2][3], F2[3][3] = temp[3][0], temp[3][1], temp[3][2], temp[3][3]  # 9. temp to F2 top half
            F2[0][4], F2[1][4], F2[2][4], F2[3][4] = temp[4][0], temp[4][1], temp[4][2], temp[4][3]  # 9. temp to F2 top half

            # Rotate face F5, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F5[i][j]
                    F5[i][j] = F5[i][cols-j-1]
                    F5[i][cols-j-1] = F5[rows-i-1][cols-j-1]
                    F5[rows-i-1][cols-j-1] = F5[rows-i-1][j]
                    F5[rows-i-1][j] = temp[i][j]
        # end of move back +
    #end of if face to rotate is back
    if face=="top":
        if direction=="-":
            # Rotate rows one (0), two (1) and three (2)
            for i in range(rows):
                temp[0][i] = F3[0][i]   # hold initial face F3 values of row 1
                temp[1][i] = F3[1][i]   # hold initial face F3 values of row 2
                temp[2][i] = F3[2][i]   # hold initial face F3 values of row 3
                
                F3[0][i] = F4[0][i]     # move F4 to F3
                F3[1][i] = F4[1][i]     # move F4 to F3
                F3[2][i] = F4[2][i]     # move F4 to F3
                
                F4[0][i] = F5[0][rows-i-1]     # move F5 to F4
                F4[1][i] = F5[1][rows-i-1]     # move F5 to F4
                F4[2][i] = F5[2][rows-i-1]     # move F5 to F4
                
                F5[0][rows-i-1] = F2[0][i]     # move F2 to F5
                F5[1][rows-i-1] = F2[1][i]     # move F2 to F5
                F5[2][rows-i-1] = F2[2][i]     # move F2 to F5
                
                F2[0][i] = temp[0][i]   # move F3 to F2, apply initial F3 values
                F2[1][i] = temp[1][i]   # move F3 to F2, apply initial F3 values
                F2[2][i] = temp[2][i]   # move F3 to F2, apply initial F3 values

            # Rotate middle rows (3 and 4), half-way
            temp[3][4], temp[3][5], temp[3][6], temp[3][7] = F3[3][4], F3[3][5], F3[3][6], F3[3][7]  # hold initial face F3 values of row right half
            temp[4][4], temp[4][5], temp[4][6], temp[4][7] = F3[4][4], F3[4][5], F3[4][6], F3[4][7]  # hold initial face F3 values of row right half

            F3[3][4], F3[3][5], F3[3][6], F3[3][7] = F4[3][0], F4[3][1], F4[3][2], F4[3][3]         # left half of F4 to right half of F3
            F3[4][4], F3[4][5], F3[4][6], F3[4][7] = F4[4][0], F4[4][1], F4[4][2], F4[4][3]         # left half of F4 to right half of F3
            F4[3][0], F4[3][1], F4[3][2], F4[3][3] = F4[3][4], F4[3][5], F4[3][6], F4[3][7]         # right half of F4 to left half of F4
            F4[4][0], F4[4][1], F4[4][2], F4[4][3] = F4[4][4], F4[4][5], F4[4][6], F4[4][7]         # right half of F4 to left half of F4
            F4[3][4], F4[3][5], F4[3][6], F4[3][7] = F5[3][7], F5[3][6], F5[3][5], F5[3][4]         # left half of F5 to right of F4
            F4[4][4], F4[4][5], F4[4][6], F4[4][7] = F5[4][7], F5[4][6], F5[4][5], F5[4][4]         # left half of F5 to right of F4
            F5[3][7], F5[3][6], F5[3][5], F5[3][4] = F5[3][3], F5[3][2], F5[3][1], F5[3][0]         # right half of F5 to left half of F5
            F5[4][7], F5[4][6], F5[4][5], F5[4][4] = F5[4][3], F5[4][2], F5[4][1], F5[4][0]         # right half of F5 to left half of F5
            F5[3][3], F5[3][2], F5[3][1], F5[3][0] = F2[3][0], F2[3][1], F2[3][2], F2[3][3]         # left half of F2 to right of F5
            F5[4][3], F5[4][2], F5[4][1], F5[4][0] = F2[4][0], F2[4][1], F2[4][2], F2[4][3]         # left half of F2 to right of F5
            F2[3][0], F2[3][1], F2[3][2], F2[3][3] = F2[3][4], F2[3][5], F2[3][6], F2[3][7]         # right half of F2 to left half of F2
            F2[4][0], F2[4][1], F2[4][2], F2[4][3] = F2[4][4], F2[4][5], F2[4][6], F2[4][7]         # right half of F2 to left half of F2
            F2[3][4], F2[3][5], F2[3][6], F2[3][7] = F3[3][0], F3[3][1], F3[3][2], F3[3][3]         # left half of F3 to right of F2
            F2[4][4], F2[4][5], F2[4][6], F2[4][7] = F3[4][0], F3[4][1], F3[4][2], F3[4][3]         # left half of F3 to right of F2
            F3[3][0], F3[3][1], F3[3][2], F3[3][3] = temp[3][4], temp[3][5], temp[3][6], temp[3][7] # initial right half of F3 to left half of F3
            F3[4][0], F3[4][1], F3[4][2], F3[4][3] = temp[4][4], temp[4][5], temp[4][6], temp[4][7] # initial right half of F3 to left half of F3

            # Rotate face F1, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F1[i][j]
                    F1[i][j] = F1[rows-i-1][j]
                    F1[rows-i-1][j] = F1[rows-i-1][cols-j-1]
                    F1[rows-i-1][cols-j-1] = F1[i][cols-j-1]
                    F1[i][cols-j-1] = temp[i][j]

        # end of move top -
        if direction=="+":
            # Rotate rows one (0), two (1) and three (2)
            for i in range(rows):
                temp[0][i] = F3[0][i]   # hold initial face F3 values of row 1
                temp[1][i] = F3[1][i]   # hold initial face F3 values of row 2
                temp[2][i] = F3[2][i]   # hold initial face F3 values of row 3
                
                F3[0][i] = F2[0][i]     # move F2 to F3
                F3[1][i] = F2[1][i]     # move F2 to F3
                F3[2][i] = F2[2][i]     # move F2 to F3
                
                F2[0][i] = F5[0][rows-i-1]     # move F5 to F2
                F2[1][i] = F5[1][rows-i-1]     # move F5 to F2
                F2[2][i] = F5[2][rows-i-1]     # move F5 to F2
                
                F5[0][rows-i-1] = F4[0][i]     # move F4 to F5
                F5[1][rows-i-1] = F4[1][i]     # move F4 to F5
                F5[2][rows-i-1] = F4[2][i]     # move F4 to F5
                
                F4[0][i] = temp[0][i]   # move F3 to F4, apply initial F3 values
                F4[1][i] = temp[1][i]   # move F3 to F4, apply initial F3 values
                F4[2][i] = temp[2][i]   # move F3 to F4, apply initial F3 values

            # Rotate middle rows (3 and 4), half-way
            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F3[3][0], F3[3][1], F3[3][2], F3[3][3]  # hold initial face F3 values of row left half
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F3[4][0], F3[4][1], F3[4][2], F3[4][3]  # hold initial face F3 values of row left half

            F3[3][0], F3[3][1], F3[3][2], F3[3][3] = F2[3][4], F2[3][5], F2[3][6], F2[3][7]         # right half of F2 to left half of F3
            F3[4][0], F3[4][1], F3[4][2], F3[4][3] = F2[4][4], F2[4][5], F2[4][6], F2[4][7]         # right half of F2 to left half of F3
            F2[3][4], F2[3][5], F2[3][6], F2[3][7] = F2[3][0], F2[3][1], F2[3][2], F2[3][3]         # left half of F2 to right half of F2
            F2[4][4], F2[4][5], F2[4][6], F2[4][7] = F2[4][0], F2[4][1], F2[4][2], F2[4][3]         # left half of F2 to right half of F2
            F2[3][0], F2[3][1], F2[3][2], F2[3][3] = F5[3][3], F5[3][2], F5[3][1], F5[3][0]         # right half of F5 to left of F2
            F2[4][0], F2[4][1], F2[4][2], F2[4][3] = F5[4][3], F5[4][2], F5[4][1], F5[4][0]         # right half of F5 to left of F2
            F5[3][3], F5[3][2], F5[3][1], F5[3][0] = F5[3][7], F5[3][6], F5[3][5], F5[3][4]         # left half of F5 to right half of F5
            F5[4][3], F5[4][2], F5[4][1], F5[4][0] = F5[4][7], F5[4][6], F5[4][5], F5[4][4]         # left half of F5 to right half of F5
            F5[3][7], F5[3][6], F5[3][5], F5[3][4] = F4[3][4], F4[3][5], F4[3][6], F4[3][7]         # right half of F4 to left of F5
            F5[4][7], F5[4][6], F5[4][5], F5[4][4] = F4[4][4], F4[4][5], F4[4][6], F4[4][7]         # right half of F4 to left of F5
            F4[3][4], F4[3][5], F4[3][6], F4[3][7] = F4[3][0], F4[3][1], F4[3][2], F4[3][3]         # left half of F4 to right half of F4
            F4[4][4], F4[4][5], F4[4][6], F4[4][7] = F4[4][0], F4[4][1], F4[4][2], F4[4][3]         # left half of F4 to right half of F4
            F4[3][0], F4[3][1], F4[3][2], F4[3][3] = F3[3][4], F3[3][5], F3[3][6], F3[3][7]         # right half of F3 to left of F4
            F4[4][0], F4[4][1], F4[4][2], F4[4][3] = F3[4][4], F3[4][5], F3[4][6], F3[4][7]         # right half of F3 to left of F4
            F3[3][4], F3[3][5], F3[3][6], F3[3][7] = temp[3][0], temp[3][1], temp[3][2], temp[3][3] # initial left half of F3 to right half of F3
            F3[4][4], F3[4][5], F3[4][6], F3[4][7] = temp[4][0], temp[4][1], temp[4][2], temp[4][3] # initial left half of F3 to right half of F3

            # Rotate face F1, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F1[i][j]
                    F1[i][j] = F1[i][rows-j-1]
                    F1[i][rows-j-1] = F1[rows-i-1][cols-j-1]
                    F1[rows-i-1][cols-j-1] = F1[rows-i-1][j]
                    F1[rows-i-1][j] = temp[i][j]

        # end of move top +
    #end of if face to rotate is top
    if face=="bottom":
        if direction=="-":
            # Rotate rows six (5), seven (6) and eight (7)
            for i in range(rows):
                temp[5][i] = F3[5][i]   # hold initial face F3 values of row 1
                temp[6][i] = F3[6][i]   # hold initial face F3 values of row 2
                temp[7][i] = F3[7][i]   # hold initial face F3 values of row 3
                
                F3[5][i] = F4[5][i]     # move F4 to F3
                F3[6][i] = F4[6][i]     # move F4 to F3
                F3[7][i] = F4[7][i]     # move F4 to F3
                
                F4[5][i] = F5[5][rows-i-1]     # move F5 to F4
                F4[6][i] = F5[6][rows-i-1]     # move F5 to F4
                F4[7][i] = F5[7][rows-i-1]     # move F5 to F4
                
                F5[5][rows-i-1] = F2[5][i]     # move F2 to F5
                F5[6][rows-i-1] = F2[6][i]     # move F2 to F5
                F5[7][rows-i-1] = F2[7][i]     # move F2 to F5
                
                F2[5][i] = temp[5][i]   # move F3 to F2, apply initial F3 values
                F2[6][i] = temp[6][i]   # move F3 to F2, apply initial F3 values
                F2[7][i] = temp[7][i]   # move F3 to F2, apply initial F3 values

            # Rotate middle rows (3 and 4), half-way
            temp[3][4], temp[3][5], temp[3][6], temp[3][7] = F3[3][4], F3[3][5], F3[3][6], F3[3][7]  # hold initial face F3 values of row right half
            temp[4][4], temp[4][5], temp[4][6], temp[4][7] = F3[4][4], F3[4][5], F3[4][6], F3[4][7]  # hold initial face F3 values of row right half

            F3[3][4], F3[3][5], F3[3][6], F3[3][7] = F4[3][0], F4[3][1], F4[3][2], F4[3][3]         # left half of F4 to right half of F3
            F3[4][4], F3[4][5], F3[4][6], F3[4][7] = F4[4][0], F4[4][1], F4[4][2], F4[4][3]         # left half of F4 to right half of F3
            F4[3][0], F4[3][1], F4[3][2], F4[3][3] = F4[3][4], F4[3][5], F4[3][6], F4[3][7]         # right half of F4 to left half of F4
            F4[4][0], F4[4][1], F4[4][2], F4[4][3] = F4[4][4], F4[4][5], F4[4][6], F4[4][7]         # right half of F4 to left half of F4
            F4[3][4], F4[3][5], F4[3][6], F4[3][7] = F5[3][7], F5[3][6], F5[3][5], F5[3][4]         # left half of F5 to right of F4
            F4[4][4], F4[4][5], F4[4][6], F4[4][7] = F5[4][7], F5[4][6], F5[4][5], F5[4][4]         # left half of F5 to right of F4
            F5[3][7], F5[3][6], F5[3][5], F5[3][4] = F5[3][3], F5[3][2], F5[3][1], F5[3][0]         # right half of F5 to left half of F5
            F5[4][7], F5[4][6], F5[4][5], F5[4][4] = F5[4][3], F5[4][2], F5[4][1], F5[4][0]         # right half of F5 to left half of F5
            F5[3][3], F5[3][2], F5[3][1], F5[3][0] = F2[3][0], F2[3][1], F2[3][2], F2[3][3]         # left half of F2 to right of F5
            F5[4][3], F5[4][2], F5[4][1], F5[4][0] = F2[4][0], F2[4][1], F2[4][2], F2[4][3]         # left half of F2 to right of F5
            F2[3][0], F2[3][1], F2[3][2], F2[3][3] = F2[3][4], F2[3][5], F2[3][6], F2[3][7]         # right half of F2 to left half of F2
            F2[4][0], F2[4][1], F2[4][2], F2[4][3] = F2[4][4], F2[4][5], F2[4][6], F2[4][7]         # right half of F2 to left half of F2
            F2[3][4], F2[3][5], F2[3][6], F2[3][7] = F3[3][0], F3[3][1], F3[3][2], F3[3][3]         # left half of F3 to right of F2
            F2[4][4], F2[4][5], F2[4][6], F2[4][7] = F3[4][0], F3[4][1], F3[4][2], F3[4][3]         # left half of F3 to right of F2
            F3[3][0], F3[3][1], F3[3][2], F3[3][3] = temp[3][4], temp[3][5], temp[3][6], temp[3][7] # initial right half of F3 to left half of F3
            F3[4][0], F3[4][1], F3[4][2], F3[4][3] = temp[4][4], temp[4][5], temp[4][6], temp[4][7] # initial right half of F3 to left half of F3

            # Rotate face F6, counterclockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F6[i][j]
                    F6[i][j] = F6[i][rows-j-1]
                    F6[i][rows-j-1] = F6[rows-i-1][cols-j-1]
                    F6[rows-i-1][cols-j-1] = F6[rows-i-1][j]
                    F6[rows-i-1][j] = temp[i][j]

        # end of move bottom -
        if direction=="+":
            # Rotate rows six (5), seven (6) and eight (7)
            for i in range(rows):
                temp[5][i] = F3[5][i]   # hold initial face F3 values of row 1
                temp[6][i] = F3[6][i]   # hold initial face F3 values of row 2
                temp[7][i] = F3[7][i]   # hold initial face F3 values of row 3
                
                F3[5][i] = F2[5][i]     # move F2 to F3
                F3[6][i] = F2[6][i]     # move F2 to F3
                F3[7][i] = F2[7][i]     # move F2 to F3
                
                F2[5][i] = F5[5][rows-i-1]     # move F5 to F2
                F2[6][i] = F5[6][rows-i-1]     # move F5 to F2
                F2[7][i] = F5[7][rows-i-1]     # move F5 to F2
                
                F5[5][rows-i-1] = F4[5][i]     # move F4 to F5
                F5[6][rows-i-1] = F4[6][i]     # move F4 to F5
                F5[7][rows-i-1] = F4[7][i]     # move F4 to F5
                
                F4[5][i] = temp[5][i]   # move F3 to F4, apply initial F3 values
                F4[6][i] = temp[6][i]   # move F3 to F4, apply initial F3 values
                F4[7][i] = temp[7][i]   # move F3 to F4, apply initial F3 values

            # Rotate middle rows (3 and 4), half-way
            temp[3][0], temp[3][1], temp[3][2], temp[3][3] = F3[3][0], F3[3][1], F3[3][2], F3[3][3]  # hold initial face F3 values of row left half
            temp[4][0], temp[4][1], temp[4][2], temp[4][3] = F3[4][0], F3[4][1], F3[4][2], F3[4][3]  # hold initial face F3 values of row left half

            F3[3][0], F3[3][1], F3[3][2], F3[3][3] = F2[3][4], F2[3][5], F2[3][6], F2[3][7]         # right half of F2 to left half of F3
            F3[4][0], F3[4][1], F3[4][2], F3[4][3] = F2[4][4], F2[4][5], F2[4][6], F2[4][7]         # right half of F2 to left half of F3
            F2[3][4], F2[3][5], F2[3][6], F2[3][7] = F2[3][0], F2[3][1], F2[3][2], F2[3][3]         # left half of F2 to right half of F2
            F2[4][4], F2[4][5], F2[4][6], F2[4][7] = F2[4][0], F2[4][1], F2[4][2], F2[4][3]         # left half of F2 to right half of F2
            F2[3][0], F2[3][1], F2[3][2], F2[3][3] = F5[3][3], F5[3][2], F5[3][1], F5[3][0]         # right half of F5 to left of F2
            F2[4][0], F2[4][1], F2[4][2], F2[4][3] = F5[4][3], F5[4][2], F5[4][1], F5[4][0]         # right half of F5 to left of F2
            F5[3][3], F5[3][2], F5[3][1], F5[3][0] = F5[3][7], F5[3][6], F5[3][5], F5[3][4]         # left half of F5 to right half of F5
            F5[4][3], F5[4][2], F5[4][1], F5[4][0] = F5[4][7], F5[4][6], F5[4][5], F5[4][4]         # left half of F5 to right half of F5
            F5[3][7], F5[3][6], F5[3][5], F5[3][4] = F4[3][4], F4[3][5], F4[3][6], F4[3][7]         # right half of F4 to left of F5
            F5[4][7], F5[4][6], F5[4][5], F5[4][4] = F4[4][4], F4[4][5], F4[4][6], F4[4][7]         # right half of F4 to left of F5
            F4[3][4], F4[3][5], F4[3][6], F4[3][7] = F4[3][0], F4[3][1], F4[3][2], F4[3][3]         # left half of F4 to right half of F4
            F4[4][4], F4[4][5], F4[4][6], F4[4][7] = F4[4][0], F4[4][1], F4[4][2], F4[4][3]         # left half of F4 to right half of F4
            F4[3][0], F4[3][1], F4[3][2], F4[3][3] = F3[3][4], F3[3][5], F3[3][6], F3[3][7]         # right half of F3 to left of F4
            F4[4][0], F4[4][1], F4[4][2], F4[4][3] = F3[4][4], F3[4][5], F3[4][6], F3[4][7]         # right half of F3 to left of F4
            F3[3][4], F3[3][5], F3[3][6], F3[3][7] = temp[3][0], temp[3][1], temp[3][2], temp[3][3] # initial left half of F3 to right half of F3
            F3[4][4], F3[4][5], F3[4][6], F3[4][7] = temp[4][0], temp[4][1], temp[4][2], temp[4][3] # initial left half of F3 to right half of F3

            # Rotate face F6, clockwise
            for i in range(rows // 2): # // = div, integer division
                for j in range(cols //2):
                    temp[i][j] = F6[i][j]
                    F6[i][j] = F6[rows-i-1][j]
                    F6[rows-i-1][j] = F6[rows-i-1][cols-j-1]
                    F6[rows-i-1][cols-j-1] = F6[i][cols-j-1]
                    F6[i][cols-j-1] = temp[i][j]

        # end of move bottom +
    #end of if face to rotate is bottom

    # rebuild cube
    cube= F1, F2, F3, F4, F5, F6
    return cube