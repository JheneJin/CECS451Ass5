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
        eArr = []
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
                eArr.append(True)
            else:
                eArr.append(False)
        # run filter for every row
        probabilityDict = filterAlgo(a, b, c, d, f, eArr)
        print(f"{a},{b},{c},{d},{f},{','.join(evidenceArr)}--><{probabilityDict[True]: .4f},{probabilityDict[False]:.4f}>" )


def filterAlgo(a, b, c, d, f, evidenceArr):
    #0.5, 0.5
    x0 = {True: a, False: 1 - a}
    #0.7, 0.3
    xT = {True: b, False: c}
    notxT = {True: 1 - b, False: 1 - c}

    # #set xT to inital x0
    x = x0

    for i in range(len(evidenceArr)):
        if evidenceArr[i] == True:
            #0.9, 0.2
            eT = {True: d, False: f}
        else:
            eT = {True: 1- d, False: 1 - f}
        
        #change the prediction and tempProb
        prediction = {True: xT[True] * x[True] + xT[False] * x[False], False: notxT[True] * x[True] + notxT[False] * x[False]}
        tempProb = {True: prediction[True] * eT[True], False: prediction[False] * eT[False]}
        alpha = 1 / (tempProb[True] + tempProb[False])
        prob = {True: tempProb[True] * alpha, False: tempProb[False] * alpha}
        x = prob
    return x

while True:
    if len(sys.argv) == 2:
        continue
    else:
        break

fileName = "cpt_test.txt"
# fileName = sys.argv[1]
cpt = readTxt(fileName)
filter(cpt)
