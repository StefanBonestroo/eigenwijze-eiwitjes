import copy
from Algorithms.helpers import calculateFolding
from classes import Protein

def depthFirst(inputPro):
    """ Checks all combinations the protein can have. Limited to a proteinlength
    of 12 (larger sizes will give running times past 6 hours per protein) """

    # Sets some variables
    succes = 0
    bestScore = 0
    bestFolding = []
    options = []
    counter = len(inputPro.proteinChain)

    # Xnl is used for pruning
    xnl = int(counter/3)

    # Ands a 0 to options for the amount of aminoacids - 2 (because two
    # are already determined) + 1 because it is needed for the loop
    for aminos in range(1,counter):
        options.append(0)

    counter -= 2

    # Checks all the posible comninations
    while options[0] != 1:

        options[counter] += 1

        if options[counter] == 5:

            cancel = 0

            while True:

                if options[counter - cancel] == 5:

                    options[counter - cancel] = 0
                    options[(counter - cancel) - 1] += 1

                else:
                    break

                cancel += 1

        # Prunes by checking if it doesn't goes straight too much
        if (options.count(0) < xnl) or (counter < 4):

            # Folds the protein
            solution = folder(options)

            # If there is a solution
            if solution != None:

                # Calculates the folding score
                oneScore = calculateFolding(solution, inputPro.proteinChain)

                # Updates 'bestScore' and 'bestFolding' if the folding is better
                if succes == 0:

                    bestScore = oneScore
                    bestFolding = solution

                elif oneScore > bestScore:

                    bestScore = oneScore
                    bestFolding = solution

                # Add one succes
                succes += 1

    # Returns the protein
    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    return bestPro

def folder(directions):
    """ Folds the protein given the directions of each protein """

    # Makes a variable for the coordinates and calculates the length of it
    aminoCoordinates = [[0,0,0],[0,1,0]]
    span = len(directions)

    # For every aminoacid that has to be placed
    for aminoAcid in range(1,span):

        # Determinates the direction
        if aminoAcid == 1:
            direction = (0,1,0)
        else:

            direction = ((aminoCoordinates[aminoAcid][0] - aminoCoordinates[aminoAcid - 1][0]),\
            (aminoCoordinates[aminoAcid][1] - aminoCoordinates[aminoAcid - 1][1]),\
            (aminoCoordinates[aminoAcid][2] - aminoCoordinates[aminoAcid - 1][2]))

        # Adds the new coodinate
        aminoCoordinates.append(copy.copy(aminoCoordinates[aminoAcid]))

        # Changes the new coordinate to its rightfull place depending on the direction.
        # 0 = straigth, 1 = up, 2 = down, 3 = left and 4 = right
        if directions[aminoAcid] == 0:

            aminoCoordinates[aminoAcid+1][0] += direction[0]
            aminoCoordinates[aminoAcid+1][1] += direction[1]
            aminoCoordinates[aminoAcid+1][2] += direction[2]

        elif directions[aminoAcid] == 1 or directions[aminoAcid] == 2:

            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid+1][1] += direction[0]
                else:
                    aminoCoordinates[aminoAcid+1][1] -= direction[0]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid+1][1] -= direction[2]
                else:
                    aminoCoordinates[aminoAcid+1][1] += direction[2]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid+1][0] -= direction[1]
                else:
                    aminoCoordinates[aminoAcid+1][0] += direction[1]

        elif directions[aminoAcid] == 3 or directions[aminoAcid] == 4:

            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid+1][2] += direction[0]
                else:
                    aminoCoordinates[aminoAcid+1][2] -= direction[0]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid+1][2] += direction[1]
                else:
                    aminoCoordinates[aminoAcid+1][2] -= direction[1]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid+1][0] -= direction[2]
                else:
                    aminoCoordinates[aminoAcid+1][0] += direction[2]

    # Makes tupples of the coordinates before returning
    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])

    # Returns the coordinates if there are no doubles
    if len(set(tuples[0])) == len(aminoCoordinates):
        return aminoCoordinates
    else:
        return None
