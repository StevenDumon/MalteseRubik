CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

def colorChar(value):
    returnVal=""
    if (value=='Y'):
        returnVal = CYELLOW2 + value + CEND
    if (value=='W'):
        returnVal = CWHITE + value + CEND
    if (value=='R'):
        returnVal = CRED2 + value + CEND
    if (value=='G'):
        returnVal = CGREEN2 + value + CEND
    if (value=='V'):
        returnVal = CVIOLET2 + value + CEND
    if (value=='B'):
        returnVal = CBLUE2 + value + CEND
    if (value==' '):
        returnVal = '.'
    return returnVal


def plot(cube):
    #       F1
    #    F2 F3 F4 F5
    #       F6
    
    F1=cube[0]
    F2=cube[1]
    F3=cube[2]
    F4=cube[3]
    F5=cube[4]
    F6=cube[5]

    cubeSize = 8

    print ('') # empty line
    # Plot face F1
    for j in range(8):
        print ('                       ', '    ', end=""),
        for i in range(8): print(colorChar(F1[j][i]), end = "  ") # end = ... continues on same line instead of new line
        print("")
    print ('') # empty line
    # Plot faces F2, F3, F4, F5
    for j in range(8):
        for i in range(8): print(colorChar(F2[j][i]), end = "  ") # end = ... continues on same line instead of new line
        print ("    ", end=""),                                   # leave some space between faces
        for i in range(8): print(colorChar(F3[j][i]), end = "  ") # end = ... continues on same line instead of new line
        print ("    ", end=""),                                   # leave some space between faces
        for i in range(8): print(colorChar(F4[j][i]), end = "  ") # end = ... continues on same line instead of new line
        print ("    ", end=""),                                   # leave some space between faces
        for i in range(8): print(colorChar(F5[j][cubeSize-i-1]), end = "  ") # end = ... continues on same line instead of new line
        print("")                                                 # start next print on new line
    print ('') # empty line

    # Plot face F6
    for j in range(8):
        print ('                       ', '    ', end=""),
        for i in range(8): print(colorChar(F6[j][i]), end = "  ") # end = ... continues on same line instead of new line
        print("")
    print ('') # empty line

