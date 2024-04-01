import sys

#create a matrix of cpt file
def readTxt(file):
    cptArr = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            #split all the values in a line then appends them as values to cptArr
            #strip gets rid of /n
            values = lines[i].strip().split(',')
            cptArr.append([])
            cptArr[i].extend(values)
    return cptArr

#extract a, b, c, d, f, evidenceArr for every row in the txt file
def filter(cpt):
    for i in range(len(cpt)):
        row = cpt[i]
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
        d = float(row[3])
        f = float(row[4])
        #extracts e values from the rest of the row
        evidenceArr = row[5:]

        for i in range(len(evidenceArr)):
            #if element in evidenceArr equals t then make it True, else make it False
            if evidenceArr[i] == "t":
                evidenceArr[i] = True
            else:
                evidenceArr[i] = False
        # run filter for every row
        print(filterAlgo(a, b, c, d, f, evidenceArr))

def filterAlgo(a, b, c, d, f, evidenceArr):
    #0.5, 0.5
    x0 = {True: a, False: 1 - a}
    #0.7, 0.3
    XtCPT = {True: b, False: c}

    #0.9, 0.2
    EtCPT = {True: d, False: f}

    # #set xT to inital x0
    xT = x0

    for evidence in evidenceArr:
        #<0.7, 0.3> * 0.5
        vecX1_givenX0timesX0 = {True: (XtCPT[True] * xT[True]), False: (XtCPT[False] * xT[False])}
        #<0.3, 0.7> * 0.5
        vecX1_givenNotX0timesNotX0 = {True: XtCPT[False] * xT[False], False: XtCPT[True] * xT[False]}
        #<0.35 + 0.15, 0.15 +0.35>
        prob_X1givenX0timesX0 = {True: vecX1_givenX0timesX0[True] + vecX1_givenNotX0timesNotX0[True], False: vecX1_givenX0timesX0[False] + 
                                vecX1_givenNotX0timesNotX0[False]}
        #<0.9, 0.2) * <0.5, 0.5>
        tempProbX1_givenE1 = {True: EtCPT[True] * prob_X1givenX0timesX0[True] , False: EtCPT[False] * prob_X1givenX0timesX0[False]}

        #0.45 + 0.1
        alpha = tempProbX1_givenE1[True] + tempProbX1_givenE1[False]
        probX1_givenE1 = {True: tempProbX1_givenE1[True] * (1/ alpha), False: tempProbX1_givenE1[False] * (1/ alpha)}
        xT = probX1_givenE1

        print(vecX1_givenX0timesX0)
        print(vecX1_givenNotX0timesNotX0)
        print(prob_X1givenX0timesX0)
        print(tempProbX1_givenE1)
        print(probX1_givenE1)
    return probX1_givenE1

while True:
    if len(sys.argv) == 2:
        continue
    else:
        break

fileName = "test.txt"
# fileName = sys.argv[1]
cpt = readTxt(fileName)
filter(cpt)