import copy

from Algorithms.helpers import calculateFolding
from classes import Protein

def checkAllLong(inputPro):
    """ Checks all combinations the protein can have up to 8 aminoAcids. After that
    checks all combinations of the next 8 amino acids and adds them together. This happens
    till the whole protein is folded."""

    # sets some values that are going to be used later
    bestFolding = 0
    proteinChain = inputPro.proteinChain
    length = len(proteinChain)

    # sets the variables where the beans are going to be stored in
    bestBean = []
    secondBean = []
    thirdBean = []
    beans = []

    # divides the proteinChain in groups of 7.
    fragmentsCode = []
    size = 0
    while (length/7) > len(fragmentsCode):
        size += 7
        fragmentsCode.append(proteinChain[(size-7):size])

    # sets the current fragment that is going to be used for depthFirst
    currentFragment = fragmentsCode[0]

    # itterates over the fragments
    for fragment in range(len(fragmentsCode)):
        # for every round bestScore is resets to 0
        bestScore = 0

        counter = len(fragmentsCode[fragment])

        # directions are needed to add the first aminoAcid of a new fragment
        directions = [(0,0,0)]
        if fragment != 0:
            lengthbean = len(beans[0])
            # gets the direction of the last aminoAcid of the pervious fragment
            for bean in beans:
                x = bean[lengthbean-2][0] - bean[lengthbean-1][0]
                y = bean[lengthbean-2][1] - bean[lengthbean-1][1]
                z = bean[lengthbean-2][2] - bean[lengthbean-1][2]
                directions.append((x,y,z))
            currentFragment += fragmentsCode[fragment]

        # used to check every posible form of the protein
        options = []
        for aminos in range(len(fragmentsCode[fragment])+1):
            options.append(0)

        # itterate over all the possible combination outcomes where:
        # 1 = up, 2 = down, 3 = left and 4 = right
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
            # if there are more than 3, 1/2/3/4's in the string it is most likely get stuck.
            if options.count(1) <= 3 and options.count(2) <= 3 and\
               options.count(3) <= 3 and options.count(4) <= 3:
                # folds the protein
                solution = folderLong(options,fragment,directions)

                if fragment != 0:
                    length = len(beans[0]) - 1
                    beanTotal = copy.deepcopy(beans)
                    copySolution = copy.deepcopy(solution)
                    # goes over the beans and adds the new folded proteins
                    for bean in range(len(beanTotal)):
                        tuples = []
                        for item in range(1,len(copySolution)):
                            add = (copySolution[item][0] + beanTotal[bean][length][0]),\
                            (copySolution[item][1] + beanTotal[bean][length][1]),\
                            (copySolution[item][2] + beanTotal[bean][length][2])
                            beanTotal[bean].append(add)
                        # if there are no duplicate coordinates
                        if len(set(beanTotal[bean])) == len(currentFragment):
                            # calculates the strength of the given structure
                            oneScore = calculateFolding(beanTotal[bean], currentFragment)
                            # saves it if the strength is good enough
                            if oneScore > bestScore:

                                bestScore = oneScore
                                bestFolding = beanTotal[bean]
                                thirdBean = secondBean
                                secondBean = bestBean[0:10]
                                bestBean = []
                                bestBean.append(beanTotal[bean])

                            elif oneScore == bestScore and (len(bestBean) != 20):

                                bestBean.append(beanTotal[bean])

                            elif oneScore <= (bestScore - 1) and\
                                 oneScore >= (bestScore - 2) and (len(secondBean) != 10):

                                secondBean.append(beanTotal[bean])

                            elif oneScore >= (bestScore - 5) and\
                                 oneScore < (bestScore - 2) and (len(thirdBean) != 10):

                                thirdBean.append(beanTotal[bean])
                else:
                    # makes tuples of the given coordinates
                    tuples = []
                    tuples.append([tuple(l) for l in solution])

                    # if there are no duplicate coordinates
                    if len(set(tuples[0])) == len(solution):
                        # calculates the strength of the given structure
                        oneScore = calculateFolding(tuples[0], currentFragment)
                        # saves it if the strength is good enough
                        if oneScore > bestScore:

                            bestScore = oneScore
                            bestFolding = tuples[0]
                            thirdBean = secondBean
                            secondBean = bestBean[0:10]
                            bestBean = []
                            bestBean.append(tuples[0])

                        elif oneScore == bestScore and (len(bestBean) != 20):

                            bestBean.append(tuples[0])

                        elif oneScore == (bestScore - 1) and (len(secondBean) != 10):

                            secondBean.append(tuples[0])

                        elif oneScore == (bestScore - 2) and (len(thirdBean) != 10):

                            thirdBean.append(tuples[0])

        # adds the different beans to beans and empty's the stores for next round
        beans = bestBean + secondBean + thirdBean
        bestBean, secondBean, thirdBean = [], [], []

    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding

    return bestPro



def folderLong(directions, usage, pointer):
    """ Folds the protein given the directions of each protein """

    # Makes a variable for the coordinates and determines the length of the given string
    aminoCoordinates = [[0,0,0]]
    span = len(directions)

    # For each aminoacid that has to be added
    for aminoAcid in range(1,span):

        coordinateAmino = aminoAcid - 1

        # Gets the direction of the first aminoacid
        if aminoAcid == 1:
            if usage == 0:
                direction = (0,1,0)
            else:
                direction = pointer[aminoAcid]
        else:
            direction = ((aminoCoordinates[coordinateAmino][0] - \
                        aminoCoordinates[coordinateAmino - 1][0]),\
                        (aminoCoordinates[coordinateAmino][1] - \
                        aminoCoordinates[coordinateAmino - 1][1]),\
                        (aminoCoordinates[coordinateAmino][2] - \
                        aminoCoordinates[coordinateAmino - 1][2]))

        # Adds the new coodinate
        aminoCoordinates.append(copy.copy(aminoCoordinates[coordinateAmino]))

        # Changes the coordinate to its right place
        if directions[aminoAcid] == 0: # straight
            aminoCoordinates[aminoAcid][0] += direction[0]
            aminoCoordinates[aminoAcid][1] += direction[1]
            aminoCoordinates[aminoAcid][2] += direction[2]

        elif directions[aminoAcid] == 1 or directions[aminoAcid] == 2: # up # down

            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid][1] += direction[0]
                else:
                    aminoCoordinates[aminoAcid][1] -= direction[0]

            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid][1] -= direction[2]
                else:
                    aminoCoordinates[aminoAcid][1] += direction[2]

            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminoAcid] == 1:
                    aminoCoordinates[aminoAcid][0] -= direction[1]
                else:
                    aminoCoordinates[aminoAcid][0] += direction[1]

        elif directions[aminoAcid] == 3 or directions[aminoAcid] == 4: # left, right
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid][2] += direction[0]
                else:
                    aminoCoordinates[aminoAcid][2] -= direction[0]

            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid][2] += direction[1]
                else:
                    aminoCoordinates[aminoAcid][2] -= direction[1]

            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminoAcid] == 3:
                    aminoCoordinates[aminoAcid][0] -= direction[2]
                else:
                    aminoCoordinates[aminoAcid][0] += direction[2]

    # Returns the coordinates
    if usage == 0:
        return aminoCoordinates[0:(span-1)]
    else:
        return aminoCoordinates
