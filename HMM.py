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
        filterAlgo(a, b, c, d, f, evidenceArr)


def filterAlgo(a, b, c, d, f, evidenceArr):
    x0 = {True: a, False: 1 - a}
    probXt1 = {True: b, False: 1 - b}
    probXt2 = {True: c, False: 1 - c}

    probEt1 = {True: d, False: 1 - d}
    probEt2 = {True: f, False: 1 - f}
    #set xT to inital x0
    xT = x0

while True:
    if len(sys.argv) == 2:
        continue
    else:
        break

fileName = "test.txt"
# fileName = sys.argv[1]
cpt = readTxt(fileName)
filter(cpt)


