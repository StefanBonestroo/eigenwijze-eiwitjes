import random

def possibilityCheck(amino, aminoCoordinates):

    # Get's location of previous amino acid
    currentLocation = aminoCoordinates[amino - 1]

    # Defines possible locations for the current amino acid
    left = ((currentLocation[0] - 1), currentLocation[1])
    right = ((currentLocation[0] + 1), currentLocation[1])
    up = (currentLocation[0], (currentLocation[1] + 1))
    down = (currentLocation[0], (currentLocation[1] - 1))

    return left, right, up, down


def validityCheck(left, right, up, down, aminoCoordinates):

    while True:
        direction = random.choice([left, right, up, down])

        # Prevents a folding where it traps itself
        if left in aminoCoordinates and right in aminoCoordinates and\
        up in aminoCoordinates and down in aminoCoordinates:
            return None

        # Will not add a location if it's taken by another amino acid
        elif direction not in aminoCoordinates:
            return direction
