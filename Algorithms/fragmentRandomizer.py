# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from classes import Protein
from random import randint
from functions import calculateFolding, visualizeFolding
from Algorithms import helpers

def fragmentRandomizer (origPro, fragment, dimension, trieMax):
    # input checks
    if dimension != ('2D' or '3D'):
        raise Exception('dimension has to be 2D or 3D')

    if len(origPro.aminoCoordinates) != len(origPro.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    if len(origPro.proteinChain) < (fragment - 2):
        raise Exception('fragment is to big for fragmentRandomizer to sample fragment from protein')

    if fragment <= 2:
         raise Exception('fragment must be at least 2')

    tries = 0
    oldScore = calculateFolding(origPro.aminoCoordinates, origPro.proteinChain)

    while tries < trieMax:

        # define start as random amino acid at least a fragment length before the end of the protein.
        start = len(origPro.proteinChain)
        # print('stoppoint: ', (len(origPro.proteinChain) - fragment))
        while start >= (len(origPro.proteinChain) - fragment):
            start = randint(0, (len(origPro.proteinChain) - fragment))

        stop = start + fragment
        shifts = []

        for amino in range(start, stop):
            # append the shift in coordinates
            if dimension == '2D':
                shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
                origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1]))
            else:
                shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
                origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1],
                origPro.aminoCoordinates[amino + 1][2] - origPro.aminoCoordinates[amino][2]))

        check = 0
        while(check == 0):
            # initialize a list of new coordinates for the fragment
            newCoordinates = [(origPro.aminoCoordinates[start][0],origPro.aminoCoordinates[start][1])]

            # find a new coordinate for every aminoacid of the fragment
            az = 0
            while az <= fragment:

                newCtries = 0

                while newCtries < len(shifts):

                    # break when there was no coordinate added for last az
                    # break if there are already (fragmentlen) coordinates in newCoordinates and they are identical to original coordinates
                    if az == len(newCoordinates) or (az == fragment-1 and newCoordinates == origPro.aminoCoordinates[start:stop]):
                        break

                    shifts = shifts # dit was nodig om de random.shuffle te laten werken
                    random.shuffle(shifts)

                    # print('az: ', az, ', start: ', start, 'newCoordinates: ', newCoordinates)
                    newShift = (shifts[newCtries])
                    # new coordinate that will be tested for validity
                    newC = (newCoordinates[az][0] + newShift[0] , newCoordinates[az][1] + newShift[1])

                    if (newC not in origPro.aminoCoordinates[0:start + az]
                    and newC not in origPro.aminoCoordinates[stop + 1:]
                    and newC not in newCoordinates):
                        # found a possible coordinate -> remove this shift from possibilities for the other amino acids
                        shifts.remove(newShift)

                        # add new coordinate
                        newCoordinates.append(newC)
                        break

                    newCtries += 1

                # print(az)
                if az == len(newCoordinates) and az != fragment:
                    break
                az +=1
            # if it finds new possible coordinates, check the score change
            if len(newCoordinates) == fragment + 1:

                # create protein with these coordinates for the fragments
                newPro = Protein(origPro.proteinChain)
                newPro.aminoCoordinates = origPro.aminoCoordinates[0:start ]
                newPro.aminoCoordinates.extend(newCoordinates)
                newPro.aminoCoordinates.extend(origPro.aminoCoordinates[stop + 1:])

                # compare score with old protein
                newPro.strength = calculateFolding(newPro.aminoCoordinates, newPro.proteinChain)

                if newPro.strength > origPro.strength:
                    origPro = newPro
                    visualizeFolding(origPro)

                # probability of acceptance

            check = 1


        tries +=1
