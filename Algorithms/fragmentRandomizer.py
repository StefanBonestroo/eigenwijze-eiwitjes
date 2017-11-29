
from random import randint
from functions import calculateFolding
from Algorithms import helpers

def fragmentRandomizer (Protein, fragment):
    if len(Protein.proteinChain) < (fragment - 2):
        print("fragment is to big for fragmentRandomizer to sample fragment from protein")

    start = randint(0, (len(Protein.proteinChain) - fragment))
    stop = start + fragment
    xShifts = []
    yShifts = []
    print("!!!!!!!!!!!!!!!!!1")
    for amino in range(start, stop):
        xShifts.append(Protein.aminoCoordinates[amino + 1][0]-Protein.aminoCoordinates[amino][0])
        yShifts.append(Protein.aminoCoordinates[amino + 1][1]-Protein.aminoCoordinates[amino][1])

    print(xShifts)
    print(yShifts)
