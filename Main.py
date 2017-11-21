#!/usr/bin/env python

import timeit

from classes import Protein
from functions import visualizeFolding
from Algorithms.randomizer import randomizer


best = [0, 0]
totaltime = 0

# Stores 'totalTime'(X) and 'bestScore' (Y)
testX = [0]
testY = [0]

eggwhite = Protein("HPHPPHHPHPPHPHHPPHPH")

# Records starting time
start = round(timeit.default_timer(), 2)

# Runs AND samples (the ouput of) the algorithm function 10,000 times
for i in range(1,10000):

    # Starts timer for a single algorithm function run
    startloop = round(timeit.default_timer(), 2)

    # Runs the algorithm function (10 tries)
    output = randomizer(eggwhite, 10)

    # Ends timer and calculates time
    endloop = round(timeit.default_timer(), 2)
    totaltime += (endloop-startloop)

    # Updates the best score
    if best[1] < output[1]:
        best = output

    # Adds sampled times and scores to be plotted later
    testX.append(totaltime)
    testY.append(output[1])

# Records stop time
stop = round(timeit.default_timer(), 2)

print("I found this solution in" + (stop - start) + "seconds")

# Store the best output
eggwhite.aminoCoordinates = best[0]
eggwhite.strength = best[1]

# Visualizes the best folding
visualizeFolding(eggwhite)
