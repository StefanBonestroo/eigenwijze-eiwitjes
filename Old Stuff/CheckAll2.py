import timeit
import copy
from classes import Protein
from Algorithms.helpers import calculateFolding

def depthFirst(inputPro):

    succes = 0
    bestScore = 0
    bestFolding = []

    # 0 == staigth; 1 == up; 2 == down; 3 == left; 4 == right;
    options = []
    counter = len(inputPro.proteinChain)
    maxRange = int(counter/3)
    for aminos in range(counter):
        options.append(0)
    counter -= 1

    while options[0] != 1:
        options[counter] += 1
        if options[counter] == 6:
            cancel = 0
            while True:
                if options[counter - cancel] == 6:
                    options[counter - cancel] = 0
                    options[(counter - cancel) - 1] += 1
                else:
                    break
                cancel += 1

        stuck = 0
        item = 0
        while stuck == 0 and item < (len(options) - 1):
            if (options[item] + options[item+1]) == 5:
                stuck = 1
            elif item < (counter - 4) and stuck == 0:
                if all(p in options[(item):(item+4)] for p in ([0,5,2,3] and [0,1,5,4] and [1,4,3,2])):
                    stuck = 1
                elif item < (counter - 6) and stuck == 0:
                    if len(set(options[(item):(item+6)])) == 6:
                        stuck = 1
            item += 1


        # if 6 verschillende getallen achter erlkaar crash of als 4 getallen en dan missend (0, 5 of 1, 4 of 2, 3)
        if stuck == 0:
            # print ("came here")
            solution = folder(options)
            if solution != None:
                # Calculates the folding score
                oneScore = calculateFolding(solution, inputPro.proteinChain)

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

    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    return bestPro

def folder(directions):
    aminoCoordinates = [[0,0,0],[1,0,0]]
    # print(directions)
    span = len(directions)
    for aminozuur in range(1,span):
        aminoCoordinates.append(copy.copy(aminoCoordinates[aminozuur]))
        if directions[aminozuur] == 0: # x + 1
            aminoCoordinates[aminozuur+1][0] += 1
        elif directions[aminozuur] == 5: # x - 1
            aminoCoordinates[aminozuur+1][0] -= 1
        elif directions[aminozuur] == 1: # y + 1
            aminoCoordinates[aminozuur+1][1] += 1
        elif directions[aminozuur] == 4: # y - 1
            aminoCoordinates[aminozuur+1][1] -= 1
        elif directions[aminozuur] == 2: # z + 1
            aminoCoordinates[aminozuur+1][2] += 1
        elif directions[aminozuur] == 3: # z - 1
            aminoCoordinates[aminozuur+1][0] -= 1

    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])
    # print (tuples)

    if len(set(tuples[0])) == len(aminoCoordinates):
        return aminoCoordinates
    else:
        return None
