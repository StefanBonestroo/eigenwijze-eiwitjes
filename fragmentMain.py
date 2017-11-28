#!/usr/bin/env python
import matplotlib.pyplot as plot

from classes import Protein
from functions import visualizeFolding
from Algorithms.randomizer import randomizer
from Algorithms.fragmentRandomizer import fragmentRandomizer

def main():

    eggwhite = Protein('HPHPPHHPHPPHPPHHHHHHHHPPPH')

    # Runs the algorithm function (10 tries)
    output = randomizer(eggwhite, 100)
    print(output)
    eggwhite.aminoCoordinates = output[0]
    eggwhite.strength = output[1]
    fragmentRandomizer(eggwhite, 4)


    # visualizeFolding(eggwhite)

if __name__ == "__main__":
    main()
