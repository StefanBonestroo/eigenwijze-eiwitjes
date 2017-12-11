# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from classes import Protein
from random import randint
from functions import calculateFolding, visualizeFolding
from Algorithms import helpers, randomizer
from Algorithms.randomizer import randomizer
# from math import expm

def fragmentRandomizer (inputPro, fragment, dimension, trieMax):

    if len(inputPro.proteinChain) < (fragment - 2):
        raise Exception('fragment is to big for fragmentRandomizer to sample fragment from protein')

    if fragment <= 2:
         raise Exception('fragment must be at least 2')

    # Get the best protein from a 100 random foldings

    output = randomizer(inputPro, 1000, dimension)
    inputPro.aminoCoordinates = output[0]
    inputPro.strength = output[1]

    origPro = inputPro
    print(origPro.aminoCoordinates)
    oldScore = origPro.strength
    # error if something went wrong in randomizer
    if len(origPro.aminoCoordinates) != len(origPro.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    tries = 0
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
                shifts = shifts # dit was nodig om de random.shuffle te laten werken
                random.shuffle(shifts)

                # trie different shifts for this az
                while newCtries < len(shifts):

                    # break when there was no coordinate added for last az
                    # break if there are already (fragmentlen) coordinates in newCoordinates and they are identical to original coordinates
                    if az == len(newCoordinates) or (az == fragment - 1 and newCoordinates == origPro.aminoCoordinates[start:stop]):
                        break

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

                        # a possible shift was found, so break the while loop
                        break

                    # shift created an already excisting coordinate so try again
                    newCtries += 1

                # (could not find a shift for last az?)
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
                # calculate probability of acceptance

                if newPro.strength >= origPro.strength:
                    print('hiya')
                    if newPro.strength > origPro.strength:
                        print('howdy')
                        visualizeFolding(origPro)

                    origPro = newPro

                # probability of acceptance

            check = 1

        tries +=1
