import timeit
from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding

def depthFirst(Protein):

    succes = 0
    bestScore = 0
    bestFolding = []

    # 0 == staigth; 1 == up; 2 == down; 3 == left; 4 == right;
    options = []
    counter = len(Protein.proteinChain)
    for aminos in range(counter):
        options.append(0)
    counter -= 1

    # recursion
    while options[0] != 3:
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
        and not ('3,3,3,3' in str(options)) and not ('4,4,4,4' in str(options)) \
        and not options.count(0) >= (len(options)/2):
            solution = folder(options, Protein)
            if solution != None:
                # Calculates the folding score
                oneScore = calculateFolding(solution, Protein.proteinChain)

                # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                # resets the coordinates
                if success == 0:
                    bestScore = oneScore
                    bestFolding = aminoCoordinates
                elif oneScore > bestScore:
                    bestScore = oneScore
                    bestFolding = aminoCoordinates

                # Add one succes
                success += 1

    return [bestFolding, bestScore]

def folder(directions, Protein):
    aminoCoordinates = [[0,0,0]]
    proteinChain = Protein.proteinChain
    for aminozuur in range(len(proteinChain)):
        if aminozuur == 0:
            direction = (1,0,0)
        else:
            (aminoCoordinates[aminozuur][0] - aminoCoordinates[aminozuur - 1][0],\
            aminoCoordinates[aminozuur][1] - aminoCoordinates[aminozuur - 1][1],\
            aminoCoordinates[aminozuur][2] - aminoCoordinates[aminozuur - 1][2])
        aminoCoordinates.append(aminoCoordinates[aminozuur])
        if directions[aminozuur] == 0: # straight
            # aminoCoordinates.append(aminoCoordinates[aminozuur][0] + direction[0],\
            # aminoCoordinates[aminozuur][1] + direction[1],\
            # aminoCoordinates[aminozuur][2] + direction[2])
            aminoCoordinates[aminozuur+1][0] += direction[0]
            aminoCoordinates[aminozuur+1][1] += direction[1]
            aminoCoordinates[aminozuur+1][2] += direction[2]
        elif directions[aminozuur] == 1: # up
            if direction == (1,0,0):
                aminoCoordinates[aminozuur+1][0] + 1
            elif direction == (-1,0,0):
                aminoCoordinates[aminozuur+1][1] - 1
            elif direction == (0,1,0):
                aminoCoordinates[aminozuur+1][0] - 1
            elif direction == (0,-1,0):
                aminoCoordinates[aminozuur+1][0] + 1
            elif direction == (0,0,1):
                aminoCoordinates[aminozuur+1][1] - 1
            elif direction == (0,0,-1):
                aminoCoordinates[aminozuur+1][1] + 1
        elif directions[aminozuur] == 2: # down
            if direction == (1,0,0):
                aminoCoordinates[aminozuur+1][1] - 1
            elif direction == (-1,0,0):
                aminoCoordinates[aminozuur+1][1] + 1
            elif direction == (0,1,0):
                aminoCoordinates[aminozuur+1][0] + 1
            elif direction == (0,-1,0):
                aminoCoordinates[aminozuur+1][0] - 1
            elif direction == (0,0,1):
                aminoCoordinates[aminozuur+1][1] + 1
            elif direction == (0,0,-1):
                aminoCoordinates[aminozuur+1][1] - 1
        elif directions[aminozuur] == 3: # left
            if direction == (1,0,0):
                aminoCoordinates[aminozuur+1][2] + 1
            elif direction == (-1,0,0):
                aminoCoordinates[aminozuur+1][2] - 1
            elif direction == (0,1,0):
                aminoCoordinates[aminozuur+1][2] + 1
            elif direction == (0,-1,0):
                aminoCoordinates[aminozuur+1][2] - 1
            elif direction == (0,0,1):
                aminoCoordinates[aminozuur+1][0] - 1
            elif direction == (0,0,-1):
                aminoCoordinates[aminozuur+1][0] + 1
        elif directions[aminozuur] == 4: # right
            if direction == (1,0,0):
                aminoCoordinates[aminozuur+1][2] - 1
            elif direction == (-1,0,0):
                aminoCoordinates[aminozuur+1][2] + 1
            elif direction == (0,1,0):
                aminoCoordinates[aminozuur+1][2] - 1
            elif direction == (0,-1,0):
                aminoCoordinates[aminozuur+1][2] + 1
            elif direction == (0,0,1):
                aminoCoordinates[aminozuur+1][0] + 1
            elif direction == (0,0,-1):
                aminoCoordinates[aminozuur+1][0] - 1
    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])
    if len(set(tuples[0])) == len(aminoCoordinates):
        return tuples


    if len(set(tuples[0])) == len(aminoCoordinates):
        # Calculates the folding score
        oneScore = calculateFolding(aminoCoordinates, Protein.proteinChain)

        # Updates 'bestScore' and 'bestFolding' if the folding is better, and
        # resets the coordinates
        if success == 0:
            bestScore = oneScore
            bestFolding = aminoCoordinates
        elif oneScore > bestScore:
            bestScore = oneScore
            bestFolding = aminoCoordinates

        # Add one succes
        success += 1
    else:
        return None

    aminoCoordinates = [[0,0,0]]

    return [bestFolding, bestScore]

    # scipy en numpy
