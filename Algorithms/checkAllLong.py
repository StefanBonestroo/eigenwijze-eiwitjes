import copy
from Algorithms.helpers import calculateFolding
from classes import Protein

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
        print (fragment)

        counter = len(fragmentsCode[fragment]) - 1
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
        for aminos in range(len(fragmentsCode[fragment])):
            options.append(0)

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
            and not ('3,3,3,3' in str(options)) and not ('4,4,4,4' in str(options)):
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
                            beanTotal[bean].append(copySolution[item])

                        tuples.append([tuple(l) for l in beanTotal[bean]])
                        if len(set(tuples[0])) == len(currentFragment):
                            oneScore = calculateFolding(tuples[0], currentFragment)
                            # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                            # resets the coordinates
                            tupleLength = len(tuples[0]) - 1
                            if oneScore > bestScore:
                                bestScore = oneScore
                                bestFolding = tuples[0]
                                fourthBean = thirthBean
                                thirthBean = secondBean
                                secondBean = bestBean[0:20]
                                bestBean = []
                                bestBean.append(tuples[0])
                            elif oneScore == bestScore and len(tuples[0]) == len(currentFragment):
                                if beanCheck(tuples[0], bestBean) == 0:
                                    bestBean.append(tuples[0])
                            elif oneScore == (bestScore - 1) and (len(secondBean) != 20):
                                if beanCheck(tuples[0], secondBean) == 0:
                                    secondBean.append(tuples[0])
                            elif oneScore == (bestScore - 2) and (len(thirthBean) != 20):
                                if beanCheck(tuples[0], thirthBean) == 0:
                                    thirthBean.append(tuples[0])
                            elif oneScore >= (bestScore - 5) and oneScore < (bestScore - 2) and (len(fourthBean) != 20):
                                if beanCheck(tuples[0], fourthBean) == 0:
                                    fourthBean.append(tuples[0])
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

        beans = []
        for bean in bestBean:
            beans.append(bean)
        for bean in secondBean:
            beans.append(bean)
        for bean in thirthBean:
            beans.append(bean)
        for bean in fourthBean:
            beans.append(bean)
        bestBean, secondBean, thirthBean, fourthBean = [], [], [], []

    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    print (bestPro.strength)
    print (bestPro.aminoCoordinates)
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
    for aminozuur in range(span):
        if aminozuur == 0:
            if usage == 0:
                direction = (0,1,0)
            else:
                direction = pointer[usage]
        else:
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
    if usage == 0:
        return aminoCoordinates[0:span]

    else:
        return aminoCoordinates
