# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random
import math

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

    output = randomizer(inputPro, 10000, dimension)
    inputPro.aminoCoordinates = output[0]
    inputPro.strength = output[1]

    origPro = inputPro
    # print(origPro.aminoCoordinates)
    bestPro = origPro # waar is dit voor dan?
    # print(oldScore)
    # error if something went wrong in randomizer
    if len(origPro.aminoCoordinates) != len(origPro.proteinChain):
        raise Exception('proteinlength does not correspond to length of aminoCoordinates')

    temp = 3.5
    while temp > 0.1:

        # define start as random amino acid at least a fragment length before the end of the protein.
        start = len(origPro.proteinChain)
        # print('stoppoint: ', (len(origPro.proteinChain) - fragment))
        while start > (len(origPro.proteinChain) - fragment):
            start = randint(0, (len(origPro.proteinChain) - fragment))

        if(start == 0):
            newCoordinates = beginFragment(origPro, fragment, dimension)
        elif(start == len(origPro.proteinChain) - fragment):
            newCoordinates = endFragment(origPro, start, fragment, dimension)
        elif(start < len(origPro.proteinChain) - fragment):
            middleInfo = middleFragment(origPro, start, fragment, dimension)
            newCoordinates = middleInfo[0]

        if newCoordinates != 'none':
                # create protein with these coordinates for the fragments
                newPro = Protein(origPro.proteinChain)

                # startFragment
                if(start == 0):
                    newPro.aminoCoordinates = newCoordinates
                    newPro.aminoCoordinates.extend(origPro.aminoCoordinates[fragment:])
                    # print('testje', newPro.aminoCoordinates)

                elif(start == len(origPro.proteinChain) - fragment):
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

                probab =  min(1,(math.expm1(newPro.strength/temp)/math.expm1(origPro.strength/temp)))
                randumb = random.uniform(0,1)
                if probab > randumb:
                    print(newPro.strength)
                    origPro = newPro
                    if origPro.strength > bestPro.strength:
                        bestPro = origPro
                temp *= 0.9998


    visualizeFolding(origPro)
    return(origPro.aminoCoordinates, origPro.strength)

# from math import expm
# p =  - math.expm()
