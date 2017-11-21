#!/usr/bin/env python

from classes import Protein
from functions import visualizeFolding
from algorithms import randomizer
import timeit

# ALLEEN NODIG OM TE BEREKENEN
# X voor de X cordinaten
# Y voor de Y cordinaten
testX = [0]
testY = [0]

eggwhite = Protein("HPHPPHHPHPPHPHHPPHPH")
start = round(timeit.default_timer(), 2)
for i in range(0,10):
    best = [0, 0]
    totaltime = 0
    if i == 0:
        for rounds in range(1,10000):
            startloop = round(timeit.default_timer(), 2)
            output = randomizer(eggwhite, 10)
            endloop = round(timeit.default_timer(), 2)
            totaltime += (endloop-startloop)
            if best[1] < output[1]:
                best = output
            testX.append(totaltime)
            testY.append(best[1])
    else:
        for rounds in range(1,10000):
            startloop = round(timeit.default_timer(), 2)
            output = randomizer(eggwhite, 10)
            endloop = round(timeit.default_timer(), 2)
            totaltime += (endloop-startloop)
            if best[1] < output[1]:
                best = output
            testX[rounds] = ((testX[rounds] + totaltime)/2)
            testY[rounds] = ((testY[rounds] + best[1])/2)

stop = round(timeit.default_timer(), 2)
print stop-start
print testY

# 0.68 bij HHHHPPHHHH 100000 loops zonder for loops
# 0.78 Bij HHHHPPHHHH at 100000 loops in for loop
# 7.3 bij HHHHPPHHHH at 100000 loops zonder for loop
# 7.5 Bij HHHHPPHHHH at 100000 loops in for loop
