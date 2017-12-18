import timeit
import copy
from Algorithms.helpers import calculateFolding
from classes import Protein

def depthFirst(inputPro):

    # sets some variables
    succes = 0
    bestScore = 0
    bestFolding = []
    options = []
    counter = len(inputPro.proteinChain)

    # xnl is used for pruning
    xnl = int(counter/3)

    # ands a 0 to options for the amount of aminoacids - 2 (because two
    # are already determined) + 1 because it is needed for the loop
    for aminos in range(1,counter):
        options.append(0)
    counter -= 2

    # checks all the posible comninations
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
        # prunes by checking if it doesn't goes straight to much
        if (options.count(0) < xnl):
            # folds the protein
            solution = folder(options)
            # if there is a soluction
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

    # returns the protein
    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    return bestPro

def folder(directions):
    # makes a variable for the coordinates and calculates the length of it
    aminoCoordinates = [[0,0,0],[0,1,0]]
    span = len(directions)
    # for every aminoacid that has to be placed
    for aminozuur in range(1,span):
        # determinates the direction
        if aminozuur == 1:
            direction = (0,1,0)
        else:
            direction = ((aminoCoordinates[aminozuur][0] - aminoCoordinates[aminozuur - 1][0]),\
            (aminoCoordinates[aminozuur][1] - aminoCoordinates[aminozuur - 1][1]),\
            (aminoCoordinates[aminozuur][2] - aminoCoordinates[aminozuur - 1][2]))
        # adds the new coodinate
        aminoCoordinates.append(copy.copy(aminoCoordinates[aminozuur]))
        # changes the new coordinate to its rightfull place depending on the direction
        if directions[aminozuur] == 0: # straight
            aminoCoordinates[aminozuur+1][0] += direction[0]
            aminoCoordinates[aminozuur+1][1] += direction[1]
            aminoCoordinates[aminozuur+1][2] += direction[2]
        elif directions[aminozuur] == 1 or directions[aminozuur] == 2: # up # down
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][1] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][1] -= direction[0]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][1] -= direction[2]
                else:
                    aminoCoordinates[aminozuur+1][1] += direction[2]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][0] -= direction[1]
                else:
                    aminoCoordinates[aminozuur+1][0] += direction[1]
        elif directions[aminozuur] == 3 or directions[aminozuur] == 4: # left, right
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][2] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][2] -= direction[0]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][2] += direction[1]
                else:
                    aminoCoordinates[aminozuur+1][2] -= direction[1]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][0] -= direction[2]
                else:
                    aminoCoordinates[aminozuur+1][0] += direction[2]

    # makes tupples of the coordinates before returning
    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])

    # returns the coordinates if there are no doubles
    if len(set(tuples[0])) == len(aminoCoordinates):
        return aminoCoordinates
    else:
        return None
