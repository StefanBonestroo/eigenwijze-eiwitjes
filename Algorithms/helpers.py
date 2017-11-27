import random

# Determines possible neighboring positions
def possibilityCheck(amino, aminoCoordinates):

    # X & Y's for increased readability
    x = 0
    y = 1

    # Get's location of previous amino acid
    currentLocation = aminoCoordinates[amino - 1]

    # Defines possible locations for the current amino acid
    left = ((currentLocation[x] - 1), currentLocation[y])
    right = ((currentLocation[x] + 1), currentLocation[y])
    up = (currentLocation[x], (currentLocation[y] + 1))
    down = (currentLocation[x], (currentLocation[y] - 1))

    return left, right, up, down

def validityCheck(left, right, up, down, aminoCoordinates, algorithm):

    neighbors = [left, right, up, down]

    if algorithm[0] == 'randomizer':
        while True:
            direction = random.choice(neighbors)

            # Prevents a folding where it traps itself
            if left in aminoCoordinates and right in aminoCoordinates and\
            up in aminoCoordinates and down in aminoCoordinates:
                return None

            # Will not add a location if it's taken by another amino acid
            elif direction not in aminoCoordinates:
                return direction

    elif algorithm[0] == 'simulated annealing':

        if (aminoCoordinates[algorithm - 1] in neighbors and\
        aminoCoordinates[algorithm + 1] in neighbors) and aminoCoordinates[algorithm]\
        in [aminoCoordinates[algorithm - 1], aminoCoordinates[algorithm + 1]]:
            return True
