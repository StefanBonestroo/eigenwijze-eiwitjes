# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from classes import Protein
from random import randint
from functions import calculateFolding, visualizeFolding
from Algorithms import helpers, randomizer
from Algorithms.randomizer import randomizer
from Algorithms.fragmentFunctions import middleFragment, endFragment,beginFragment
# from math import expm

def fragmentRandomizer (inputPro, fragment, dimension, trieMax):

    if len(inputPro.proteinChain) < (fragment - 2):
        raise Exception('fragment is to big for fragmentRandomizer to sample fragment from protein')

    if fragment <= 2:
         raise Exception('fragment must be at least 2')

    # Get the best protein from a 100 random foldings

    output = randomizer(inputPro, 1, dimension)
    inputPro.aminoCoordinates = output[0]
    inputPro.strength = output[1]

    origPro = inputPro
    # print(origPro.aminoCoordinates)
    oldScore = origPro.strength # waar is dit voor dan?
    # print(oldScore)
    # error if something went wrong in randomizer
    if len(origPro.aminoCoordinates) != len(origPro.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    tries = 0
    while tries < trieMax:

        # define start as random amino acid at least a fragment length before the end of the protein.
        start = len(origPro.proteinChain)
        # print('stoppoint: ', (len(origPro.proteinChain) - fragment))
        while start > (len(origPro.proteinChain) - fragment):
            start = randint(0, (len(origPro.proteinChain) - fragment))

        # if(start == 0):
        #     newCoordinates = beginFragment(origPro, fragment, dimension)
        if(start == len(origPro.proteinChain) - fragment):
            newCoordinates = endFragment(origPro, start, fragment, dimension)
        elif(start < len(origPro.proteinChain) - fragment):
             middleInfo = middleFragment(origPro, start, fragment, dimension)
             newCoordinates = middleInfo[0]
        # else() iets fout gegaan
        #     error

        if newCoordinates != 'none':
                # create protein with these coordinates for the fragments
                newPro = Protein(origPro.proteinChain)

                # startFragment
                # if(start == 0):
                #     newPro.aminoCoordinates = newCoordinates
                #     newPro.aminoCoordinates.extend(origPro.aminoCoordinates[fragment:])
                #     print('testje', newPro.aminoCoordinates)

                if(start == len(origPro.proteinChain) - fragment):
                    newPro.aminoCoordinates = origPro.aminoCoordinates[0 : start]
                    newPro.aminoCoordinates.extend(newCoordinates)

                # middlefragment
                elif(start < len(origPro.proteinChain) - fragment):
                    newPro.aminoCoordinates = origPro.aminoCoordinates[0 : start]
                    newPro.aminoCoordinates.extend(newCoordinates)
                    newPro.aminoCoordinates.extend(origPro.aminoCoordinates[middleInfo[1] + 1:])

                # compare score with old protein
                # print('!!!', newPro.aminoCoordinates, newPro.proteinChain)
                newPro.strength = calculateFolding(newPro.aminoCoordinates, newPro.proteinChain)
                # calculate probability of acceptance

                if newPro.strength >= origPro.strength:
                    if newPro.strength > origPro.strength:
                        # print(newPro.strength)
                        visualizeFolding(newPro)

                    origPro = newPro

        tries +=1
    return(origPro.aminoCoordinates, origPro.strength)

# from math import expm
# p =  - math.expm()
