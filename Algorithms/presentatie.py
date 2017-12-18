import copy
from Algorithms.helpers import calculateFolding
from classes import Protein

def depthFirst(inputPro):
    """ Checks all combinations the protein can have. But with more than 12 amino acids it will take too long. """

    code = "HPHHPHPPHH"
    eiwit = [(0,0,0),(0,1,0),(0,2,0),(1,2,0),(1,1,0),(1,0,0),(2,0,0),(2,-1,0),(1,-1,0),(0,-1,0)]

    oneScore = calculateFolding(eiwit, code)

    bestScore = oneScore
    bestFolding = eiwit

    # returns the protein
    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    return bestPro
