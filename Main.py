#!/usr/bin/env python
import sys

import timeit
import matplotlib.pyplot as plot

from classes import Protein
from functions import visualizeFolding
from functions import printUsage
from Algorithms.randomizer import randomizer

# from Algorithms.simulatedAnnealing import simulatedAnnealing

def main():

    # Ensure proper usage
    if len(sys.argv) < 4:
        printUsage()
        return
    elif sys.argv[2] not in ['randomizer','depth-first','fragment randomizer'] or\
    sys.argv[3] not in ['2D','3D']:
        printUsage()
        return

    proteinString = sys.argv[1]
    runningAlgorithm = sys.argv[2]
    dimension = sys.argv[3]

    # Optionality of tries argument (default: 10000)
    if runningAlgorithm == 'randomizer':
        if len(sys.argv) == 5:
            tries = int(sys.argv[4])
        else:
            tries = 10000

    # Stores 'totalTime'(X) and 'bestScore' (Y)
    best = [0, 0]
    totaltime = 0
    testX = [0]
    testY = [0]

    # Initiate object
    eggwhite = Protein(proteinString)

    # Records starting time
    start = round(timeit.default_timer(), 2)

    if runningAlgorithm == 'randomizer':
        # Runs the randomizer algorithm
        output = randomizer(eggwhite, tries, dimension)
    elif runningAlgorithm == 'depth-first':
        # Runs the depth-first algorithm (only in 3D)
        output = depthFirst(eggwhite)
    elif runningAlgorithm == 'fragment randomizer':
        # Runs an algorithm that tweaks fragments of a randomized protein
        output = fragmentRandomizer(eggwhite, dimension)

    # Records stop time
    stop = round(timeit.default_timer(), 2)

    # Updates the best score
    if best[1] < output[1]:
        best = output

    print('I found this solution in ' + str(round((stop - start), 2)) + ' seconds.')

    # Store the best output
    eggwhite.aminoCoordinates = best[0]
    eggwhite.strength = best[1]

    # Visualizes the best folding
    visualizeFolding(eggwhite)

if __name__ == "__main__":
    main()
