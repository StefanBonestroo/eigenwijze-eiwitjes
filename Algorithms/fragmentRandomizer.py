# This function takes a protein (that already has coordinates)
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


    for amino in range(start, stop):
        # append the shift in coordinates
        shifts.append((Protein.aminoCoordinates[amino + 1][0]-Protein.aminoCoordinates[amino][0],
        Protein.aminoCoordinates[amino + 1][1]-Protein.aminoCoordinates[amino][1]))

    print(shifts)
