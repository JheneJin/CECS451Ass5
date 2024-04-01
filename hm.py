import sys

#Aidan Mara
#CECS 451
#Assignment 5: HMM


#HMM Filtering or Prediction
def filter(pX, p_X, e0 , pEX,p_EX,eList):
  #Set Initial to Prob of given
  ei = e0

  #For every evidence
  for evidence in eList:
    #Summation side of the formula
    sum_pX = {
      #summation rain i true * current prob of evidence and the opposite
        True: (pX[True] * ei[True] + pX[True] * ei[False]),
        False: (pX[False] * ei[True] + p_X[False] * ei[False])
    }

    ei = {
      #set new ei to prob of sensor * prediction
        True: (sum_pX[True] * pEX[evidence]),
        False: (sum_pX[False] * p_EX[evidence])
    }

    #normalize and set to new ei, but i subtracted to make sure its always total prob of 1
    ei[True] = ei[True]/(ei[True]+ei[False])
    ei[False] = 1-ei[True]

  #return latest one
  return ei


# input_filename = sys.argv[1]
input_filename = "test.txt"

with open(input_filename, 'r') as file:
  for line in file:
    data = line.strip().split(',')

    a, b, c, d, f = map(float, data[:5])
    eList = data[5:]

    pX = {True: b, False: 1 - b}
    p_X = {True: c, False: 1 - c}

    e0 = {True: a, False: 1 - a}

    pEX = {True: d, False: 1 - d}
    p_EX = {True: f, False: 1 - f}


    eList2 = []

    for e in eList:
      if e == 't':
        eList2.append(True)
      else:
        eList2.append(False)

    prob = filter(pX,p_X,e0,pEX,p_EX,eList2)

    print(f"{line[:-1]}--><{prob[True]:.4f},{prob[False]:.4f}>")