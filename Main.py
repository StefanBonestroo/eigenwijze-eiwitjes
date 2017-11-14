#!/usr/bin/env python

from classes import Protein
from functions import visualizeFolding
from algorithms import randomizer

eggwhite = Protein("HHHPPHHH")

output = randomizer(eggwhite, 200)
eggwhite.aminoCoordinates = output[0]
eggwhite.strength = output[1]

visualizeFolding(eggwhite)
