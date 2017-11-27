import random
from functions import calculateFolding

def randomizer (Protein, tries):

    aminoCoordinates = [(0,0),(0,1)]

    x = 0
    y = 1
    success = 0
    stuck = 0
    loops = 0

    bestScore = 0
    bestFolding = []

    while success != tries:

        for amino in range(2, len(Protein.proteinChain)):
            # Get's location of previous amino acid
            currentLocation = aminoCoordinates[amino - 1]

            # Defines possible locations for the current amino acid
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1))
            down = (currentLocation[0], (currentLocation[1] - 1))

            # Randomly picks one of the directions, checks if it's valid, and adds it to 'aminoCoordinates'
            while True:
                direction = random.choice([left, right, up, down])

                # Prevents a folding where it traps itself
                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates:
                    stuck = 1
                    break

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    aminoCoordinates.append(direction)
                    break


            if stuck == 1:
                break

        if stuck == 0:
            # Calculates the folding score
            oneScore = calculateFolding(aminoCoordinates, Protein.proteinChain)

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
        aminoCoordinates = [(0,0),(0,1)]

    # print(loops)
    return [bestFolding, bestScore]

#######################################################################
# Function that randomizes certain folds within an already folded
# protein. 
#######################################################################

def randomOptimize (Protein, tries):
