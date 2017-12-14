import timeit
import copy
from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding

# hele eiwitten laatste dingen weg halen en nieuwe bij zetten zodat niet alles opnieuw ge

def depthFirst(Protein):

    succes = 0
    bestScore = 0
    bestFolding = []

    # 0 == staigth; 1 == up; 2 == down; 3 == left; 4 == right;
    options = []
    counter = len(Protein.proteinChain)
    # xnl = int(counter/4)
    for aminos in range(1,counter):
        options.append(0)
    counter -= 2

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
        if not ('1,1,1,1' in str(options)) and not ('2,2,2,2' in str(options)) \
        and not ('3,3,3,3' in str(options)) and not ('4,4,4,4' in str(options)):    # and xnl > options.count(0)
            solution = folder(options, Protein)
            if solution != None:
                # Calculates the folding score
                oneScore = calculateFolding(solution, Protein.proteinChain)

                # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                # resets the coordinates
                if succes == 0:
                    bestScore = oneScore
                    bestFolding = solution
                elif oneScore > bestScore:
                    bestScore = oneScore
                    bestFolding = solution

                # Add one succes
                succes += 1

    return [bestFolding, bestScore]

def folder(directions, Protein):
    aminoCoordinates = [[0,0,0],[1,0,0]]
    span = len(directions)
    for aminozuur in range(1,span):
        direction = ((aminoCoordinates[aminozuur][0] - aminoCoordinates[aminozuur - 1][0]),\
        (aminoCoordinates[aminozuur][1] - aminoCoordinates[aminozuur - 1][1]),\
        (aminoCoordinates[aminozuur][2] - aminoCoordinates[aminozuur - 1][2]))
        aminoCoordinates.append(copy.copy(aminoCoordinates[aminozuur]))
        if directions[aminozuur] == 0: # straight
            aminoCoordinates[aminozuur+1][0] += direction[0]
            aminoCoordinates[aminozuur+1][1] += direction[1]
            aminoCoordinates[aminozuur+1][2] += direction[2]
        elif directions[aminozuur] == 1 or directions[aminozuur] == 2: # up # down
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][0] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][0] -= direction[0]
            elif direction == (0,1,0) or direction == (0,-1,0) or direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][1] -= direction[1]
                else:
                    aminoCoordinates[aminozuur+1][1] += direction[1]
        elif directions[aminozuur] == 3 or directions[aminozuur] == 4: # left, right
            if direction == (1,0,0) or direction == (-1,0,0) or direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][2] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][2] -= direction[0]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][0] -= direction[2]
                else:
                    aminoCoordinates[aminozuur+1][0] += direction[2]

    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])
    # print (tuples)

    if len(set(tuples[0])) == len(aminoCoordinates):
        print (aminoCoordinates)
        return aminoCoordinates
    else:
        return None

    # scipy en numpy
