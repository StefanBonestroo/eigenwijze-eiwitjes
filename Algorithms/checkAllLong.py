import copy
from Algorithms.helpers import calculateFolding
from classes import Protein
# from itertools import product

# PseudoCode:

# pakt het eiwit en zet het in groepen van 8

def checkAllLong(inputPro):

    succes = 0
    bestScore = 0
    bestFolding = 0
    proteinChain = inputPro.proteinChain
    length = len(proteinChain)

    bestBean = []
    secondBean = []
    thirthBean = []
    fourthBean = []
    beans = []
    fragmentsCode = []

    size = 0
    while (length/8) > len(fragmentsCode):
        size += 8
        fragmentsCode.append(proteinChain[(size-8):size])

    currentFragment = fragmentsCode[0]
    print (fragmentsCode)

    for fragment in range(len(fragmentsCode)):
        bestScore = 0

        counter = len(fragmentsCode[fragment])
        directions = []
        if fragment != 0:
            lengthbean = len(beans[0])
            for bean in beans:
                x = bean[lengthbean-2][0] - bean[lengthbean-1][0]
                y = bean[lengthbean-2][1] - bean[lengthbean-1][1]
                z = bean[lengthbean-2][2] - bean[lengthbean-1][2]
                directions.append((x,y,z))
            currentFragment += fragmentsCode[fragment]

        options = []
        for aminos in range(len(fragmentsCode[fragment])+1):
            options.append(0)

        # for options in product([0,1,2,3,4], repeat = len(fragmentsCode[fragment])):
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
            solution = folderLong(options,fragment,directions)

            continues = 0
            if fragment != 0:
                length = len(beans[0]) - 1
                beanTotal = []
                for bean in range(len(beans)):
                    beanTotal.append(copy.deepcopy(beans[bean]))
                    copySolution = copy.deepcopy(solution)
                    tuples = []
                    for item in range(1,len(copySolution)):
                        copySolution[item][0] += beans[bean][length][0]
                        copySolution[item][1] += beans[bean][length][1]
                        copySolution[item][2] += beans[bean][length][2]
                        copySolution[item] = tuple(copySolution[item])
                        if copySolution[item] in beans[bean]:
                            break
                        beanTotal[bean].append(copySolution[item])


                    if len(set(beanTotal[bean])) == len(currentFragment):
                        oneScore = calculateFolding(beanTotal[bean], currentFragment)
                        # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                        # resets the coordinates
                        tupleLength = len(beanTotal[bean]) - 1
                        if oneScore > bestScore:
                            bestScore = oneScore
                            bestFolding = beanTotal[bean]
                            fourthBean = thirthBean
                            thirthBean = secondBean
                            secondBean = bestBean[0:10]
                            bestBean = []
                            bestBean.append(beanTotal[bean])
                        elif oneScore == bestScore and len(beanTotal[bean]) == len(currentFragment):
                            if beanCheck(beanTotal[bean], bestBean) == 0:
                                bestBean.append(beanTotal[bean])
                        elif oneScore == (bestScore - 1) and (len(secondBean) != 10):
                            if beanCheck(beanTotal[bean], secondBean) == 0:
                                secondBean.append(beanTotal[bean])
                        elif oneScore == (bestScore - 2) and (len(thirthBean) != 10):
                            if beanCheck(beanTotal[bean], thirthBean) == 0:
                                thirthBean.append(beanTotal[bean])
                        elif oneScore >= (bestScore - 5) and oneScore < (bestScore - 2) and (len(fourthBean) != 10):
                            if beanCheck(beanTotal[bean], fourthBean) == 0:
                                fourthBean.append(beanTotal[bean])
            else:
                solution = solution[0:length]
                tuples = []
                tuples.append([tuple(l) for l in solution])

                if len(set(tuples[0])) == len(solution):
                    oneScore = calculateFolding(tuples[0], currentFragment)
                    # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                    # resets the coordinates
                    if succes == 0:
                        bestScore = oneScore
                        bestFolding = tuples[0]
                    elif oneScore > bestScore:
                        bestScore = oneScore
                        bestFolding = tuples[0]
                        thirthBean == secondBean
                        secondBean == bestBean[0:5]
                        bestBean = []
                        bestBean.append(tuples[0])
                    elif oneScore == bestScore and (len(bestBean) != 20):
                        if beanCheck(tuples[0], bestBean) == 0:
                            bestBean.append(tuples[0])
                    elif oneScore == (bestScore - 1) and (len(secondBean) != 10):
                        if beanCheck(tuples[0], secondBean) == 0:
                            secondBean.append(tuples[0])
                    elif oneScore == (bestScore - 2) and (len(thirthBean) != 10):
                        if beanCheck(tuples[0], thirthBean) == 0:
                            thirthBean.append(tuples[0])

                # Add one succes
                succes += 1

        beans = bestBean + secondBean + thirthBean + fourthBean
        bestBean, secondBean, thirthBean, fourthBean = [], [], [], []

    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    print (bestPro.strength)
    print (bestPro.aminoCoordinates)
    print (inputPro.proteinChain)
    return bestPro

def beanCheck(tuplee, allBeans):
    notin = 0
    for bean in allBeans:
        if bean == tuplee:
            notin += 1
    return notin



def folderLong(directions, usage, pointer):
    aminoCoordinates = [[0,0,0]]
    span = len(directions)
    for aminozuur in range(1,span):
        coordinateAmino = aminozuur - 1
        if aminozuur == 1:
            if usage == 0:
                direction = (0,1,0)
            else:
                direction = pointer[usage]
        else:
            direction = ((aminoCoordinates[coordinateAmino][0] - aminoCoordinates[coordinateAmino - 1][0]),\
            (aminoCoordinates[coordinateAmino][1] - aminoCoordinates[coordinateAmino - 1][1]),\
            (aminoCoordinates[coordinateAmino][2] - aminoCoordinates[coordinateAmino - 1][2]))
        aminoCoordinates.append(copy.copy(aminoCoordinates[coordinateAmino]))
        if directions[aminozuur] == 0: # straight
            aminoCoordinates[coordinateAmino+1][0] += direction[0]
            aminoCoordinates[coordinateAmino+1][1] += direction[1]
            aminoCoordinates[coordinateAmino+1][2] += direction[2]
        elif directions[aminozuur] == 1 or directions[aminozuur] == 2: # up # down
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[coordinateAmino+1][1] += direction[0]
                else:
                    aminoCoordinates[coordinateAmino+1][1] -= direction[0]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 1:
                    aminoCoordinates[coordinateAmino+1][1] -= direction[2]
                else:
                    aminoCoordinates[coordinateAmino+1][1] += direction[2]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[coordinateAmino+1][0] -= direction[1]
                else:
                    aminoCoordinates[coordinateAmino+1][0] += direction[1]
        elif directions[aminozuur] == 3 or directions[aminozuur] == 4: # left, right
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[coordinateAmino+1][2] += direction[0]
                else:
                    aminoCoordinates[coordinateAmino+1][2] -= direction[0]
            elif direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[coordinateAmino+1][2] += direction[1]
                else:
                    aminoCoordinates[coordinateAmino+1][2] -= direction[1]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 3:
                    aminoCoordinates[coordinateAmino+1][0] -= direction[2]
                else:
                    aminoCoordinates[coordinateAmino+1][0] += direction[2]
    if usage == 0:
        return aminoCoordinates[0:span]

    else:
        return aminoCoordinates
