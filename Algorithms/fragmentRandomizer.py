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
        raise Exception('fragment is to big for fragmentRandomizer to sample fragment from protein')

    if fragment <= 2:
         raise Exception('fragment must be at least 2')

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

    #
    check = 0
    while(check == 0):
        # initialize a list of new coordinates for the fragment
        newCoordinates = [(Protein.aminoCoordinates[start][0],Protein.aminoCoordinates[start][1])]
        az = 0

        # find a new coordinate for every aminoacid of the fragment
        while az <= fragment:

            newCtries = 0
            while newCtries < len(shifts):
                random.shuffle(shifts)

                newC = (newCoordinates[az][0] + shifts[i][0], newCoordinates[az][1] + shifts[i][1])

                if newC not in Protein.coordinates[0:start] and not in Protein.coordinates[stop:]:
                    # found a possible coordinate -> remove this shift from possibilities for the other amino acids
                    shifts.remove(shiftChoice)
                    # add new coordinate
                    newCoordinates.append(newC)
                    # end the whileloop for this amino acid coordinate search
                    newCtries = shifts
                elif newCtries == (len(shifts) - 1):
                    # something here that gives a message that there are no possible coordinates for this amino acid
                elif:
                    newCtries += 1




        # implement new coordinates using slicing
        # for c in newCoordinates:
        check = 1
