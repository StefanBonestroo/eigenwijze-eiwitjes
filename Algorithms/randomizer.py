from classes import Protein
from Algorithms.helpers import possibilityCheck, calculateFolding, validityCheck

def randomizer (inputProtein, tries, dimension):

    if dimension == '2D':
        aminoCoordinates = [(0,0),(0,1)]
    elif dimension == '3D':
        aminoCoordinates = [(0,0,0),(0,0,1)]

    tries = tries
    success = 0
    stuck = 0
    loops = 0

    bestScore = 0
    bestFolding = []

    while success < tries:

        for amino in range(2,len(inputProtein.proteinChain)):

            # Generate possibilities for neighboring locations
            possibilities = possibilityCheck(amino, aminoCoordinates)

            # Randomly picks one of the directions, checks if it's valid,
            # and adds it to 'aminoCoordinates'
            valid = validityCheck(possibilities, aminoCoordinates, 'randomizer')
            if valid != None:
                aminoCoordinates.append(valid)
            else:
                stuck = 1
                break

        if stuck == 0:
            # Calculates the folding score
            oneScore = calculateFolding(aminoCoordinates, inputProtein.proteinChain)

            # Updates 'bestScore' and 'bestFolding' if the folding is better, and
            # resets the coordinates
            if success == 0:
                bestScore = oneScore
                bestFolding = aminoCoordinates
            elif oneScore > bestScore:
                bestScore = oneScore
                bestFolding = aminoCoordinates

            # Add one succes
            success += 1

        # Resets values for a new try
        loops += 1
        stuck = 0
        if dimension == '2D':
            aminoCoordinates = [(0,0),(0,1)]
        elif dimension == '3D':
            aminoCoordinates = [(0,0,0),(0,0,1)]

    # print(loops)
    bestPro = Protein(inputProtein.proteinChain)
    bestPro.aminoCoordinates = bestFolding
    bestPro.strength = bestScore
    return bestPro
