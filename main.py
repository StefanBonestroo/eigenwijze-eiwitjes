#!/usr/bin/env python
#
# Protein Power by 'Eigenwijze eiwitjes'
# 'A problem solving assignment in the Heuristieken course'
#
# Date: 17/12/2017
#
# Authors:
#     Yente Stor
#     Jesse Groot
#     Stefan Bonestroo
#
# This program folds a protein string to its, possibly, most stable conformation.
# A protein is a string of P/H/C's which, when adjacent (but not covalently connected)
# provide strength, as in stability, (H-C and H-H - 1 point, C-C - 5 points).
# There are several ways to get as many points, check 'printUsage' for the
# different algorithms you can use to fold a protein.

import sys
import timeit

import matplotlib.pyplot as plot

from classes import Protein
from Algorithms.randomizer import randomizer
from Algorithms.fragmentRandomizer import fragmentRandomizer
from Algorithms.CheckAll import depthFirst, folder
from Algorithms.checkAllLong import checkAllLong, folderLong

def main():

    # Ensure proper usage
    if len(sys.argv) < 4:
        printUsage()
        return

    elif sys.argv[2] not in ['randomizer','depth-first','fragment-randomizer',\
    'depth-first-long'] or sys.argv[3] not in ['2D','3D']:
        printUsage()
        return

    proteinString = str(sys.argv[1])
    runningAlgorithm = str(sys.argv[2])
    dimension = str(sys.argv[3])

    bestPro = Protein
    bestPro.strength = 0
    bestPro.aminoCoordinates = 0

    # Optionality of tries argument (default: 10000)
    if runningAlgorithm == 'randomizer':

        if len(sys.argv) == 5:
            tries = int(sys.argv[4])
        else:
            tries = 10000

        if len(sys.argv) == 6:
            save = bool(sys.argv[6])
        else:
            save = False

    elif runningAlgorithm == 'fragment-randomizer':

        if len(sys.argv) in [5, 6, 7]:
            tries = int(sys.argv[4])

            # You can only try something a number of times
            if str(tries).isdigit() == False:
                printUsage()
                return
        else:
            tries = 1

        # Plus an optional fragment length argument
        if len(sys.argv) in [6,7]:
            fragmentLength = int(sys.argv[5])

            # Fragments can only be a number long
            if str(fragmentLength).isdigit() == False:
                printUsage()
                return
            elif fragmentLength < 3 or len(proteinString) < (fragmentLength - 2):
                print("\nFragment length must be longer than 2")
                print("Also, a fragment can't be 2 short of you protein length\n")
                return
        else:
            fragmentLength = 9

        if len(sys.argv) == 7:
            save = bool(sys.argv[7])
        else:
            save = False

    # Initiate object
    eggwhite = Protein(proteinString)

    # Records starting time
    start = round(timeit.default_timer(), 2)

    if runningAlgorithm == 'randomizer':
        # Runs the randomizer algorithm
        outputPro = randomizer(eggwhite, tries, dimension)

    elif runningAlgorithm == 'depth-first':
        # Runs the depth-first algorithm (only in 3D)
        dimension = '3D'
        save = sys.argv[4]
        outputPro = depthFirst(eggwhite)

    elif runningAlgorithm == 'depth-first-long':
        # Runs the depth-first algorithm (only in 3D)
        save = sys.argv[4]
        outputPro = depthFirst(eggwhite)
        outputPro = checkAllLong(eggwhite)


    elif runningAlgorithm == 'fragment-randomizer':
        # Runs an algorithm that tweaks fragments of a randomized protein
        outputPro = fragmentRandomizer(eggwhite, fragmentLength, dimension, tries)

    # Records stop time
    stop = round(timeit.default_timer(), 2)

    # Updates the best score
    if bestPro.strength < outputPro.strength:
        bestPro = outputPro

    print('\nI found this solution in ' + str(round((stop - start), 2)) + ' seconds.\n')

    # Visualizes the best folding
    bestPro.visualizeFolding(save)


def printUsage():
    """ Prints the usage of main.py in a pretty way. """

    print('\nUsage: \n')
    print(' Argument 1: protein string to be folded, e.a. \"HHPHPHP\"')
    print(' Argument 2: desired algorithm -> \'randomizer\', \'depth-first\', \'depth-first-long\', or \'fragment-randomizer\'')
    print(' Argument 3: desired folding dimensions -> \'2D\' or \'3D\'')
    print(' Argument 4: *optional argument \'tries\' for \'randomizer\' and \'fragment-randomizer\'')
    print(' Argument 5: *optional argument \'fragmentLength\' for \'fragment-randomizer\'\n')
    print(' Argument 6: *optional argument \'save\' -> 0 (True) or 1 (False) ?\n')

if __name__ == "__main__":
    main()
