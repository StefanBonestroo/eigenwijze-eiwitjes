
# Prints the correct usage (in a pretty way)
def printUsage():
        print('\nUsage: \n')
        print(' Argument 1: protein string to be folded, e.a. \"HHPHPHP\"')
        print(' Argument 2: desired algorithm -> \'randomizer\', \'depth-first\', \'fragment-randomizer\'')
        print(' Argument 3: desired folding dimensions -> \'2D\' or \'3D\'')
        print(' Argument 4: *optional argument \'tries\' for \'randomizer\' and \'fragment-randomizer\'')
        print(' Argument 5: *optional argument \'fragmentLength\' for \'fragment-randomizer\'\n')


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
