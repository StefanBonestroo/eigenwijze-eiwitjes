import copy
from functions import calculateFolding
from functions import calculateFolding

# PseudoCode:

# pakt het eiwit en zet het in groepen van 8

def checkAllLong(Protein):

    succes = 0
    proteinChain = Protein.proteinChain
    Length = len(proteinChain)
    # worden de verschillende vormen van de beste strength bewaard samen met 5 vormen van slechtere
    # bestStrength = []
    # secondStrength = []
    # thrithStrength = []
    # fourthStrength = []
    # fifthStrength = []
    # beans = [bestStrength, secondStrength, thrithStrength, fourthStrength, fifthStrength]

    beans = []
    # newbeans = []

    fragments = []
    fragmentsCode = []

    while (Length/8) >= len(fragments):
        fragments.append(options[(size-8):size])
        fragmentsCode.append(proteinCain[(size-8):size])
        size += 8

    print (fragmentsCode)
    counter = length - 1
    for fragment in range(len(fragments)):

        # beans = newbeans
        # newbeans = []
        directions = []
        lengthbean = len(beans[0])
        for bean in beans:
            x = bean[lengthbean-2][0] - bean[lengthbean-1][0]
            y = bean[lengthbean-2][1] - bean[lengthbean-1][1]
            z = bean[lengthbean-2][2] - bean[lengthbean-1][2]
            directions.append((x,y,z)

        options = []
        for aminos in range(len(fragments[fragment])):
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
            and not ('3,3,3,3' in str(options)) and not ('4,4,4,4' in str(options)) and xnl > options.count(0):
                solution = folder(options,fragmentsCode[fragment],fragment,beans,directions)
                if solution != None:
                    # Calculates the folding score
                    oneScore = calculateFolding(solution, Protein.proteinChain, beans)

                    # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                    # resets the coordinates
                    if succes == 0:
                        bestScore = oneScore
                        bestFolding = solution

                    elif oneScore >= bestScore:
                        bestScore = oneScore
                        bestFolding = solution

                    # Add one succes
                    succes += 1

        beans = []
        beans.append(bestFolding)
    return [bestFolding, bestScore]

def folder(directions, Protein, usage, beans, pointer):
    aminoCoordinates = [[0,0,0]]
    span = len(directions)
    for aminozuur in range(span):
        if aminozuur == 0:
            if usage == 0:
                direction == (0,1,0)
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

    length = len(beans[0]) - 1
    if usage != 0:
        for bean in beans:
            tuples = []
            for item in range(1,len(aminoCoordinates)):
                aminoCoordinates[item][0] += bean[length - span + item][0]
                aminoCoordinates[item][1] += bean[length - span + item][1]
                aminoCoordinates[item][2] += bean[length - span + item][2]
                bean.append(aminoCoordinates[item])
            tuples.append([tuple(l) for l in bean])
            if len(set(tuples[0])) == len(aminoCoordinates):
                return bean
            else:
                return None
    else:
        tuples = []
        tuples.append([tuple(l) for l in aminoCoordinates])
        # print (tuples)

        if len(set(tuples[0])) == len(aminoCoordinates):
            return aminoCoordinates[0:span]
        else:
            return None
