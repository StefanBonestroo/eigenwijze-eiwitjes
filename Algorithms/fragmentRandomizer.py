# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from random import randint
from functions import calculateFolding
from Algorithms import helpers

def fragmentRandomizer (Protein, fragment, dimension, tries):
    # input checks
    if dimension != ('2D' or '3D'):
        raise Exception('dimension has to be 2D or 3D')

    if len(Protein.aminoCoordinates) != len(Protein.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    if len(Protein.proteinChain) < (fragment - 2):
        raise Exception('fragment is to big for fragmentRandomizer to sample fragment from protein')

    if fragment <= 2:
         raise Exception('fragment must be at least 2')

    # define start as random amino acid at least a fragment length before the end of the protein.
    start = len(Protein.proteinChain)
    # print('stoppoint: ', (len(Protein.proteinChain) - fragment))
    while start >= (len(Protein.proteinChain) - fragment):
        start = randint(0, (len(Protein.proteinChain) - fragment))

    stop = start + fragment
    shifts = []
    # print('start: ')
    print(start)
    # print('stop: ')
    print(stop)
    # print('coordinaten: ')
    print(Protein.aminoCoordinates)

    for amino in range(start, stop):
        print('amino: ',amino)
        # append the shift in coordinates
        if dimension == '2D':
            shifts.append((Protein.aminoCoordinates[amino + 1][0] - Protein.aminoCoordinates[amino][0],
            Protein.aminoCoordinates[amino + 1][1] - Protein.aminoCoordinates[amino][1]))
        else:
            shifts.append((Protein.aminoCoordinates[amino + 1][0] - Protein.aminoCoordinates[amino][0],
            Protein.aminoCoordinates[amino + 1][1] - Protein.aminoCoordinates[amino][1],
            Protein.aminoCoordinates[amino + 1][2] - Protein.aminoCoordinates[amino][2]))

    check = 0
    while(check == 0):
        # initialize a list of new coordinates for the fragment
        newCoordinates = [(Protein.aminoCoordinates[start][0],Protein.aminoCoordinates[start][1])]

        # find a new coordinate for every aminoacid of the fragment
        az = 0
        while az <= fragment:

            newCtries = 0

            while newCtries < len(shifts):
                shifts = shifts # dit was nodig om de random.shuffle te laten werken
                random.shuffle(shifts)

                if az >= len(newCoordinates):
                    break

                # print('az: ', az, ', start: ', start, 'newCoordinates: ', newCoordinates)
                newShift = (shifts[newCtries])
                # new coordinate that will be tested for validity
                newC = (Protein.aminoCoordinates[az + start][0] + newShift[0] , Protein.aminoCoordinates[az + start][1] + newShift[1])

                if newC not in Protein.aminoCoordinates[0:start + az] and newC not in Protein.aminoCoordinates[stop:]:
                    # found a possible coordinate -> remove this shift from possibilities for the other amino acids
                    shifts.remove(newShift)

                    # add new coordinate
                    newCoordinates.append(newC)
                    # print('found new coordinate',newCoordinates ,' for amino acid', az)
                    break

                newCtries += 1
            az +=1


        # implement new coordinates using slicing
        # for c in newCoordinates:

        check = 0
