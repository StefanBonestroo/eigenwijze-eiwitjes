import random

# Determines possible neighboring positions
def possibilityCheck(amino, aminoCoordinates, dimension):

    # X & Y's for increased readability
    x = 0
    y = 1
    z = 2

    # Get's location of previous amino acid
    currentLocation = aminoCoordinates[amino - 1]

    if dimension == '2D':
        # Defines possible locations for the current amino acid
        left = ((currentLocation[x] - 1), currentLocation[y])
        right = ((currentLocation[x] + 1), currentLocation[y])
        up = (currentLocation[x], (currentLocation[y] + 1))
        down = (currentLocation[x], (currentLocation[y] - 1))

        return [left, right, up, down]


    elif dimension == '3D':
        # Defines possible locations for the current amino acid
        left = ((currentLocation[x] - 1), currentLocation[y], currentLocation[z])
        right = ((currentLocation[x] + 1), currentLocation[y], currentLocation[z])
        up = (currentLocation[x], (currentLocation[y] + 1), currentLocation[z])
        down = (currentLocation[x], (currentLocation[y] - 1), currentLocation[z])
        front = (currentLocation[x], (currentLocation[y]), (currentLocation[z] + 1))
        back = (currentLocation[x], (currentLocation[y]), (currentLocation[z] - 1))

        return [left, right, up, down, front, back]


def validityCheck(possibilities, aminoCoordinates, algorithm, amino):

    if len(possibilities) == 4:

        if algorithm == 'randomizer':
            while True:
                direction = random.choice(possibilities)

                # Prevents a folding where it traps itself
                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

        elif algorithm == 'simulated annealing':

            if (aminoCoordinates[amino - 1] in possibilities and\
            aminoCoordinates[amino + 1] in possibilities) and aminoCoordinates[amino]\
            in [aminoCoordinates[amino - 1], aminoCoordinates[amino + 1]]:
                return True


    if len(possibilities) == 6:

        if algorithm == 'randomizer':

            while True:
                direction = random.choice(possibilities)

                left = possibilities[0]
                right = possibilities[1]
                up = possibilities[2]
                down = possibilities[3]
                front = possibilities[4]
                back = possibilities[5]

                # Prevents a folding where it traps itself
                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates and\
                front in aminoCoordinates and back in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

        elif algorithm == 'simulated annealing':

            if (aminoCoordinates[amino - 1] in possibilities and\
            aminoCoordinates[amino + 1] in possibilities) and aminoCoordinates[amino]\
            in [aminoCoordinates[amino - 1], aminoCoordinates[amino + 1]]:
                return True
