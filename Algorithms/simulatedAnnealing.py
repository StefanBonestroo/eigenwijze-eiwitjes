import random
import math

from functions import calculateFolding
from Algorithms import helpers

def simulatedAnnealing(Protein, tries, conservatism):

    # Creates a protein to work with
    randomizers = 10000
    currentProteinBest = randomizer(Protein, randomizers)

    bestFolding = currentProteinBest[0]
    bestScore = currentProteinBest[1]

    length = len(Protein.proteinChain)

    # Get current protein & score
    currentFolding = currentProteinBest[0]
    currentScore = currentProteinBest[1]

    # Set temperatures
    Temp = 1
    TempMinus = 0.001

    # Repeat until the minimal temperature is reached
    while T > T_min:

        steps = 0

        # For every temp, repeat 'tries' times
        while steps < tries:
            # Generate neighboring solution
            amino = random.randint(0, length
            left, right, up, down = possibilityCheck(amino, currentFolding)
            tweak = random.choice([left, right, up, down])

            overlapPenalty = 1
            overlapOccurances = 0

            bondBreakPenalty = 1
            bondBreakOccurances = 0

            # Make a possible change and calculate the score
            changedFolding = currentFolding
            changedFolding[amino] = tweak
            changedScore = calculateFolding(changedFolding, Protein.proteinChain)

            # Checks whether there is overlap and/or bondbreaking
            overlap = len(currentFolding) != len(set(changedFolding))
            bondBreak = validityCheck(left, right, up, down, changedFolding,\
            ['simulated annealing', amino])

            # Penalizes if 2 aminoacids overlap & updates
            if overlap:
                changedScore -= overlapPenalty
                overlapOccurances += 1
                overlapPenalty += (0.5 * overlapOccurances)

            # Gets neighbors of the tweaked aminoacid
            left, right, up, down = possibilityCheck(amino, changedFolding)

            # Penalizes if covalent bonds are broken (neighbors are too far away)
            if bondBreak:
                changedScore -= bondBreakPenalty
                bondBreakOccurances += 1
                bondBreakPenalty += (0.5 * bondBreakPenalty)

            # Get the difference between scores of current and tweaked
            differenceScore = currentScore - changedScore

            # Generate a probability and a random float
            acceptance = math.pow(math.e, (differenceScore/Temp))
            randomInt = random.int(0,length)

            # Change current if accepted
            if probability > random:
                currentFolding = changedFolding
                currentScore = changedScore

            # Add step
            steps += 1

        # Change temperature
        Temp *= conservatism
