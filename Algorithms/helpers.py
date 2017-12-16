import random

# Determines possible neighboring positions
def possibilityCheck(amino, aminoCoordinates):

    # X & Y's for increased readability
    x = 0
    y = 1
    z = 2

    # Get's location of previous amino acid
    # print('checkAminoCoordinates', aminoCoordinates)
    currentLocation = aminoCoordinates[amino - 1]

    if len(aminoCoordinates[0]) == 2:
        # Defines possible locations for the current amino acid
        left = ((currentLocation[x] - 1), currentLocation[y])
        right = ((currentLocation[x] + 1), currentLocation[y])
        up = (currentLocation[x], (currentLocation[y] + 1))
        down = (currentLocation[x], (currentLocation[y] - 1))

        return [left, right, up, down]


    elif len(aminoCoordinates[0]) == 3:
        # Defines possible locations for the current amino acid
        left = ((currentLocation[x] - 1), currentLocation[y], currentLocation[z])
        right = ((currentLocation[x] + 1), currentLocation[y], currentLocation[z])
        up = (currentLocation[x], (currentLocation[y] + 1), currentLocation[z])
        down = (currentLocation[x], (currentLocation[y] - 1), currentLocation[z])
        front = (currentLocation[x], (currentLocation[y]), (currentLocation[z] + 1))
        back = (currentLocation[x], (currentLocation[y]), (currentLocation[z] - 1))

        return [left, right, up, down, front, back]

# Returns a random VALID location for the next aminoacid
def validityCheck(possibilities, aminoCoordinates, algorithm):

    if len(possibilities) == 4:

        if algorithm == 'randomizer':
            while True:
                direction = random.choice(possibilities)

                # Prevents a folding where it traps itself
                left = possibilities[0]
                right = possibilities[1]
                up = possibilities[2]
                down = possibilities[3]

                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

    if len(possibilities) == 6:

        if algorithm == 'randomizer':

            while True:
                direction = random.choice(possibilities)

                # Prevents a folding where it traps itself
                left = possibilities[0]
                right = possibilities[1]
                up = possibilities[2]
                down = possibilities[3]
                front = possibilities[4]
                back = possibilities[5]

                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates and\
                front in aminoCoordinates and back in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

# Calculates the protein stability/strength
def calculateFolding (aminoCoordinates, proteinChain):

    # X & Y's for increased readability
    x = 0
    y = 1
    z = 2

    strength = 0

    if len(aminoCoordinates[0]) == 2:

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            currentX = aminoCoordinates[focus][x]
            currentY = aminoCoordinates[focus][y]

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):
                neighborX = aminoCoordinates[partner][x]
                neighborY = aminoCoordinates[partner][y]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(currentX - neighborX) == 1) and\
                (abs(currentY - neighborY) == 0)) or\
                ((abs(currentY - neighborY) == 1) and\
                (abs(currentX - neighborX) == 0))) and\
                (focus-partner) not in [-1, 0, 1]:
                    if (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') or\
                    (proteinChain[focus] == 'C' and proteinChain[partner] == 'H') or\
                    (proteinChain[focus] == 'H' and proteinChain[partner] == 'C'):
                        strength += 0.5
                    elif proteinChain[focus] == 'C' and proteinChain[partner] == 'C':
                        strength += 2.5

        return strength


    elif len(aminoCoordinates[0]) == 3:

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            currentX = aminoCoordinates[focus][x]
            currentY = aminoCoordinates[focus][y]
            currentZ = aminoCoordinates[focus][z]

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):

                neighborX = aminoCoordinates[partner][x]
                neighborY = aminoCoordinates[partner][y]
                neighborZ = aminoCoordinates[partner][z]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(currentX - neighborX) == 1) and\
                (abs(currentY - neighborY) == 0) and\
                (abs(currentZ - neighborZ) == 0)) or\
                ((abs(currentX - neighborX) == 0) and\
                (abs(currentY - neighborY) == 1) and\
                (abs(currentZ - neighborZ) == 0)) or\
                ((abs(currentX - neighborX) == 0) and\
                (abs(currentY - neighborY) == 0) and\
                (abs(currentZ - neighborZ) == 1))) and\
                (focus - partner) not in [-1, 0, 1]:
                    if (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') or\
                    (proteinChain[focus] == 'C' and proteinChain[partner] == 'H') or\
                    (proteinChain[focus] == 'H' and proteinChain[partner] == 'C'):
                        strength += 0.5
                    elif proteinChain[focus] == 'C' and proteinChain[partner] == 'C':
                        strength += 2.5


        return strength


# def numberGenerater(number):
#     while number[0] != 3:
#         options[counter] += 1
#         if options[counter] == 5:
#             cancel = 0
#             while True:
#                 if options[counter - cancel] == 5:
#                     options[counter - cancel] = 0
#                     options[(counter - cancel) - 1] += 1
#                 else:
#                     break
#                 cancel += 1
#         if not ('1, 1, 1' in str(options)) and not ('2, 2, 2' in str(options)) \
#         and not ('3, 3, 3' in str(options)) and not ('4, 4, 4' in str(options)):
