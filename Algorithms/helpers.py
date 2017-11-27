import random

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

    if algorithm == 'randomizer':
        while True:
            direction = random.choice([left, right, up, down])

            # Prevents a folding where it traps itself
            if left in aminoCoordinates and right in aminoCoordinates and\
            up in aminoCoordinates and down in aminoCoordinates:
                return None

            # Will not add a location if it's taken by another amino acid
            elif direction not in aminoCoordinates:
                return direction
    elif algorithm == 'simulated annealing':
