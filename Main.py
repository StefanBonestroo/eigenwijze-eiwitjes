#!/usr/bin/env python
import sys

import timeit
import matplotlib.pyplot as plot

from classes import Protein
from functions import visualizeFolding
from Algorithms.randomizer import randomizer
# from Algorithms.simulatedAnnealing import simulatedAnnealing

def main():

    # Ensure proper usage
    if len(sys.argv) < 4:
        print('')
        print('Usage: ')
        print('')
        print(' Argument 1: protein string to be folded, e.a. \"HHPHPHP\"')
        print(' Argument 2: desired algorithm -> \'randomizer\', \'depth-first\', \'fragment randomizer\'')
        print(' Argument 3: desired folding dimensions -> \'2D\' or \'3D\'')
        print('')
        return

    # Stores 'totalTime'(X) and 'bestScore' (Y)
    best = [0, 0]
    totaltime = 0
    testX = [0]
    testY = [0]

    proteinString = sys.argv[1]
    runningAlgorithm = sys.argv[2]
    dimension = sys.argv[3]

    eggwhite = Protein(proteinString)

    # Records starting time
    start = round(timeit.default_timer(), 2)

    # Runs AND samples (the output of) the algorithm function 10,000 times

    for i in range(1,1000):

        # Starts timer for a single algorithm function run
        startloop = round(timeit.default_timer(), 2)

        if runningAlgorithm == 'randomizer':
            # Runs the randomizer algorithm (10 tries)
            output = randomizer(eggwhite, 10, dimension)
        elif runningAlgorithm == 'depth-first':
            # Runs the depth-first algorithm
            output = depthFirst(eggwhite, dimension)
        elif runningAlgorithm == 'fragment randomizer':
            # Runs an algorithm that tweaks fragments of a randomized protein
            output = fragmentRandomizer(eggwhite, dimension)

        # Ends timer and calculates time
        endloop = round(timeit.default_timer(), 2)
        totaltime += (endloop-startloop)

        # Updates the best score
        if best[1] < output[1]:
            best = output

        # Adds sampled times and scores to be plotted later
        testX.append(totaltime)
        testY.append(best[1])

    # Records stop time
    stop = round(timeit.default_timer(), 2)

    print('I found this solution in ' + str(round((stop - start), 2)) + ' seconds.')

    # Store the best output
    eggwhite.aminoCoordinates = best[0]
    eggwhite.strength = best[1]

    # Visualizes the best folding
    visualizeFolding(eggwhite)

    # Initiate experimental plot
    experimental = plot.figure()

    # Visualizes the samples
    plot.scatter(testX, testY)
    plot.show()

if __name__ == "__main__":
    main()
