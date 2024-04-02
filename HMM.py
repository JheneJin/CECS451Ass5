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
        #get the whole row
        row = cpt[i]
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
        d = float(row[3])
        f = float(row[4])
        #extracts e values from the rest of the row
        evidenceArr = row[5:]
        #pass in the value into filter algorithm
        probabilityDict = filterAlgo(a, b, c, d, f, evidenceArr)
        #output cpt row and it's output
        print(f"{a},{b},{c},{d},{f},{','.join(evidenceArr)}--><{probabilityDict[True]:.4f},{probabilityDict[False]:.4f}>" )

def filterAlgo(a, b, c, d, f, evidenceArr):
    #intialized the x0, xT, and not_xT
    x0 = {True: a, False: 1 - a}
    xT = {True: b, False: c}
    not_xT = {True: 1 - b, False: 1 - c}

    #set x to inital x0
    x = x0

    #loop thru evidenceArr
    for i in range(len(evidenceArr)):
        #equal true use d and f
        if evidenceArr[i] == "t":
            eT = {True: d, False: f}
        #use 1-d and 1 -f
        else:
            eT = {True: 1- d, False: 1 - f}
        #calculate the true and false for prediction using xT, not_xT, and x
        prediction = {True: xT[True] * x[True] + xT[False] * x[False], False: not_xT[True] * x[True] + not_xT[False] * x[False]}
        #calculate prob for True and False before alpha using prediction and eT
        tempProb = {True: prediction[True] * eT[True], False: prediction[False] * eT[False]}
        #calculate alpha
        alpha = 1 / (tempProb[True] + tempProb[False])
        #normalize the tempProb using alpha for True and false
        prob = {True: tempProb[True] * alpha, False: tempProb[False] * alpha}
        #update x throughtout the loop
        x = prob
    #return x when loop is done
    return x

#only takes in two arugments HMM.py and txt file, one or three arguments will print the error statements
if len(sys.argv) == 2:
    fileName = sys.argv[1]
    cpt = readTxt(fileName)
    filter(cpt)
else:
    print("Incorrect number of arguments in terminal")
    print("To use properly, enter python HMM.py <fileName>")
