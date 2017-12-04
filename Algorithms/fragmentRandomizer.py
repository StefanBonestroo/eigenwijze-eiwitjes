# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from random import randint
from functions import calculateFolding
from Algorithms import helpers

def fragmentRandomizer (Protein, fragment, dimension):
    # input checks
    if dimension != ('2D' or '3D'):
        raise Exception('dimension has to be 2D or 3D')

    if len(Protein.aminoCoordinates) != len(Protein.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    if len(Protein.proteinChain) < (fragment - 2):
        print("fragment is to big for fragmentRandomizer to sample fragment from protein")

    start = randint(0, (len(Protein.proteinChain) - fragment))
    stop = start + fragment
    shifts = []
    print('start: ')
    print(start)
    print('stop: ')
    print(stop)
    print('coordinaten: ')
    print(Protein.aminoCoordinates)

    for amino in range(start, stop):
        print(amino)
        # append the shift in coordinates
        if dimension == '2D':
            shifts.append((Protein.aminoCoordinates[amino + 1][0]-Protein.aminoCoordinates[amino][0],
            Protein.aminoCoordinates[amino + 1][1]-Protein.aminoCoordinates[amino][1]))
        else:
            shifts.append((Protein.aminoCoordinates[amino + 1][0]-Protein.aminoCoordinates[amino][0],
            Protein.aminoCoordinates[amino + 1][1]-Protein.aminoCoordinates[amino][1],
            Protein.aminoCoordinates[amino + 1][2]-Protein.aminoCoordinates[amino][2]))

    check = 0
    while(check == 0):

        newCoordinates = [(Protein.aminoCoordinates[start][0],Protein.aminoCoordinates[start][1])]

        # create new coordinates of fragment
        for az in range(fragment):

            shiftChoice = random.choice(shifts)
            shifts.remove(shiftChoice)
            newC = (newCoordinates[az][0] + shiftChoice[0], newCoordinates[az][1] + shiftChoice[1])
            newCoordinates.append(newC)

        # implement new coordinates using slicing
        # for c in newCoordinates:
        check = 1
