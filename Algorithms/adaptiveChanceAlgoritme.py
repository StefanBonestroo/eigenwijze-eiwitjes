from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding

# Sla data op in --> [(0,0,0),(0,0,0)]

# make random x times a protein (x depends on length of the string) NOT

# go into this algoritme

# Make a random protein
# during making the random protein make an array with all the locations that would result in a strength adjustment
    # looking like [(0,1,0),(0,1,0),(0,1,1)] or [[(0,1,0),2],[(0,1,1),1]]
        # in possibilityCheck for item in array (hierboven): if left == item: adjust(left) etc
# in validityCheck build in directions in an array [(0,1,0), (-1,0,0) etc]
    #deze word bij de bestFolding opgeslagen
    #nu bij het maken van een random protein als er geen verbindingen kunnen worden gemaakt geef een grotere neiging om
        #vouwingen te maken zoals bij de bestfolding
            #Hoe meer het op best folding lijkt hoe groter de kans is op een betere folding.
                #deze misschien pas na x aantal foldings toepassen zodat deze al een beetje een goede structuur heeft.
#Loopen deze zooi

# store the bestScore till Now
    # store the directions

def addeptiveChance (Protein, tries, dimension):

    if dimension == '2D':
        aminoCoordinates = [(0,0),(0,1)]
    elif dimension == '3D':
        aminoCoordinates = [(0,0,0),(0,0,1)]

    tries = tries
    success = 0
    stuck = 0
    loops = 0

    bestScore = 0
    bestFolding = []

    while success < tries:

        for amino in range(2,len(Protein.proteinChain)):

            # Generate possibilities for neighboring locations
            possibilities = possibilityCheck(amino, aminoCoordinates)

            # Randomly picks one of the directions, checks if it's valid, and adds it to 'aminoCoordinates'
            valid = validityCheck(possibilities, aminoCoordinates, 'randomizer', amino)
            if valid != None:
                aminoCoordinates.append(valid)
            else:
                stuck = 1
                break

        if stuck == 0:
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

        # Resets values for a new try
        loops += 1
        stuck = 0
        if dimension == '2D':
            aminoCoordinates = [(0,0),(0,1)]
        elif dimension == '3D':
            aminoCoordinates = [(0,0,0),(0,0,1)]

    # print(loops)
    return [bestFolding, bestScore]

def validityCheckAdaptive(possibilities, aminoCoordinates, algorithm, amino):

    if len(possibilities) == 4:

        if algorithm == 'randomizer':
            while True:
                direction = random.choice(possibilities)

                # Prevents a folding where it traps itself
                left = possibilities[0]
                right = possibilities[1]
                up = possibilities[2]
                down = possibilities[3]

                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

    if len(possibilities) == 6:

        if algorithm == 'randomizer':

            while True:
                direction = random.choice(possibilities)

                # Prevents a folding where it traps itself
                left = possibilities[0]
                right = possibilities[1]
                up = possibilities[2]
                down = possibilities[3]
                front = possibilities[4]
                back = possibilities[5]

                if left in aminoCoordinates and right in aminoCoordinates and\
                up in aminoCoordinates and down in aminoCoordinates and\
                front in aminoCoordinates and back in aminoCoordinates:
                    return None

                # Will not add a location if it's taken by another amino acid
                elif direction not in aminoCoordinates:
                    return direction

# Doel --> mieren en Addaptive Chance samen zetten in een algoritme
# Addaptive heeft voorsprong maar als deze niet word gebruikt word er gekozen voor het mieren principe.
