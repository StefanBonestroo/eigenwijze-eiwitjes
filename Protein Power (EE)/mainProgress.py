#!/usr/bin/env python

from classes import Protein
from functions import visualizeFolding
from algorithms import randomizer
import timeit

# ALLEEN NODIG OM TE BEREKENEN
best = [0, 0]
totaltime = 0
# X voor de X cordinaten
# Y voor de Y cordinaten
testX = [0]
testY = [0]

eggwhite = Protein("HPHPPHHPHPPHPHHPPHPH")

start = round(timeit.default_timer(), 2)
for i in range(1,10000):
    startloop = round(timeit.default_timer(), 2)
    output = randomizer(eggwhite, 10)
    endloop = round(timeit.default_timer(), 2)
    totaltime += (endloop-startloop)
    if best[1] < output[1]:
        print("I came")
        best = output
    testX.append(totaltime)
    testY.append(best[1])
# 0.68 bij HHHHPPHHHH 100000 loops zonder for loops
# 0.78 Bij HHHHPPHHHH at 100000 loops in for loop
# 7.3 bij HHHHPPHHHH at 100000 loops zonder for loop
# 7.5 Bij HHHHPPHHHH at 100000 loops in for loop
stop = round(timeit.default_timer(), 2)
print stop-start
eggwhite.aminoCoordinates = best[0]
eggwhite.strength = best[1]

visualizeFolding(eggwhite)
