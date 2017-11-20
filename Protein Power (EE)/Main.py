#!/usr/bin/env python

from classes import Protein
from functions import visualizeFolding
from algorithms import randomizer
import timeit

eggwhite = Protein("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH")

start = start = timeit.default_timer()
output = randomizer(eggwhite, 100000)
stop = timeit.default_timer()
print stop-start
eggwhite.aminoCoordinates = output[0]
eggwhite.strength = output[1]

visualizeFolding(eggwhite)
