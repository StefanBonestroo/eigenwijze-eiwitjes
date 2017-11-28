#!/usr/bin/env python
import timeit
import matplotlib.pyplot as plot

from classes import Protein
from functions import visualizeFolding
from Algorithms.randomizer import randomizer
# from Algorithms.simulatedAnnealing import simulatedAnnealing

def main():

    # Stores 'totalTime'(X) and 'bestScore' (Y)
    best = [0, 0]
    totaltime = 0
    testX = [0]
    testY = [0]

    eggwhite = Protein('HPHPPHHPHPPHPPHHHHHHHHPPPH')

    # Records starting time
    start = round(timeit.default_timer(), 2)

    # Runs AND samples (the ouput of) the algorithm function 10,000 times
    for i in range(1,100):

        # Starts timer for a single algorithm function run
        startloop = round(timeit.default_timer(), 2)

        # Runs the algorithm function (10 tries)
        output = randomizer(eggwhite, 100)

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

    # Visualizes the samples
    plot.scatter(testX, testY)
    plot.show()

    # Visualizes the best folding
    visualizeFolding(eggwhite)

if __name__ == "__main__":
    main()
