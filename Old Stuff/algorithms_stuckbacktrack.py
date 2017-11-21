# fileheaders

import random
from functions import calculateFolding

def randomizer (Protein, tries):

    aminoCoordinates = [(0,0),(0,1)]

    x = 0
    y = 1
    success = 0
    stuck = 0
    stuck_count = 0
    loops = 0
    bestScore = 0
    bestFolding = []

    while success != tries:
        # start with second amino acid
        amino = 1

        while amino < len(Protein.proteinChain):

            # Get's location of previous amino acid
            currentLocation = aminoCoordinates[amino]

            # Defines possible locations for the next amino acid
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1))
            down = (currentLocation[0], (currentLocation[1] - 1))

            # Catches folding where it traps itself
            if left in aminoCoordinates and right in aminoCoordinates and\
            up in aminoCoordinates and down in aminoCoordinates and\
            stuck_count <= 4:
                stuck = 1
                stuck_count += 1
                # go two steps back
                amino = amino - 2
                aminoCoordinates = aminoCoordinates[0:amino+1]

            elif left in aminoCoordinates and right in aminoCoordinates and\
            up in aminoCoordinates and down in aminoCoordinates and\
            stuck_count >= 3:
                break

            else:
                # Randomly picks one of the directions, checks if it's valid, and adds it to 'aminoCoordinates'
                while True:
                    direction = random.choice([left, right, up, down])

                    # Will not add a location if it's taken by another amino acid
                    if direction not in aminoCoordinates:
                        aminoCoordinates.append(direction)
                        amino += 1
                        break

        if stuck == 0:
            # Calculates the folding score
            oneScore = calculateFolding(aminoCoordinates, Protein.proteinChain)

            # Updates 'bestScore' and 'bestFolding' if the folding is better, and
            # resets the coordinates
            if oneScore > bestScore:
                bestScore = oneScore
                bestFolding = aminoCoordinates

            # Add one succes
            success += 1
            # reset stuck_count
            stuck_count = 0
        loops += 1
        stuck = 0
        aminoCoordinates = [(0,0),(0,1)]

    print(loops)
    return [bestFolding, bestScore]
