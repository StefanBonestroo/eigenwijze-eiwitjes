#!/usr/bin/env python
import matplotlib.pyplot as plot

from classes import Protein
from functions import visualizeFolding
from Algorithms.randomizer import randomizer
from Algorithms.fragmentRandomizer import fragmentRandomizer

def main():

    eggwhite = Protein('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP')

    # Runs the algorithm function (10 tries)
    output = randomizer(eggwhite, 100, '2D')
    eggwhite.aminoCoordinates = output[0]
    eggwhite.strength = output[1]
    visualizeFolding(eggwhite)
    fragmentRandomizer(eggwhite, 5, '2D', 10000)



    # visualizeFolding(eggwhite)

if __name__ == "__main__":
    main()
