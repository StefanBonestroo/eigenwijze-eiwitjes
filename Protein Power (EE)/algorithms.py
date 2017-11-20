from random import randint
from functions import calculateFolding

def randomizer (Protein, tries):

    aminoCoordinates = [(0,0),(0,1)]

    x = 0
    y = 1
    tries = tries
    success = 0
    stuck = 0
    loops = 0

    bestScore = 0
    bestFolding = []

    while success != tries:

        for amino in range(2,len(Protein.proteinChain)):

            # Get's location of previous amino acid
            currentLocation = aminoCoordinates[amino - 1]

            # Defines possible locations for the current amino acid
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1))
            down = (currentLocation[0], (currentLocation[1] - 1))

            # Randomly picks one of the directions, checks if it's valid, and adds it to 'aminoCoordinates'
            while True:
                direction = randint(1,4)
                # Will not add a location if it's taken by another amino acid
                if direction == 1 and left not in aminoCoordinates:
                    aminoCoordinates.append(left)
                    break
                elif direction == 2 and right not in aminoCoordinates:
                    aminoCoordinates.append(right)
                    break
                elif direction == 3 and up not in aminoCoordinates:
                    aminoCoordinates.append(up)
                    break
                elif direction == 4 and down not in aminoCoordinates:
                    aminoCoordinates.append(down)
                    break

                # Prevents a folding where it traps itself
                elif left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates:
                    stuck = 1
                    break
            if stuck == 1:
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
        loops += 1
        stuck = 0
        aminoCoordinates = [(0,0),(0,1)]

    print(loops)
    return [bestFolding, bestScore]
