import random
import math

from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from Algorithms.randomizer import randomizer

def simulatedAnnealing(Protein, tries, conservatism):

    # Creates a protein to work with
    randomizers = 1000
    currentProteinBest = randomizer(Protein, randomizers)

    bestFolding = currentProteinBest[0]
    bestScore = currentProteinBest[1]

    length = len(Protein.proteinChain)

    # Get current protein & score
    currentFolding = currentProteinBest[0]
    currentScore = currentProteinBest[1]

    # Set temperatures
    Temp = 1
    TempMinus = 0.05

    # Repeat until the minimal temperature is reached
    while Temp > TempMinus:

        steps = 0

        # For every temp, repeat 'tries' times
        while steps < tries:

            if bestScore < currentScore:
                bestFolding = currentFolding
                bestScore = currentScore

            overlap = False
            bondBreak = False

            distanceFromStart = 0

            # Generate neighboring solution
            amino = random.randint(0, length - 1)

            # Makes sure a change doesn't involve breaking the rules
            while (not overlap and not bondBreak) and (amino < length - 1):

                # Get possibilities for change
                left, right, up, down = possibilityCheck(amino, currentFolding)

                # Get a tweak option
                tweak = random.choice([left, right, up, down])

                # Make a possible change and calculate the score
                changedFolding = currentFolding
                changedFolding[amino] = tweak

                # Gets neighbors of the tweaked aminoacid
                left, right, up, down = possibilityCheck(amino, changedFolding)

                # If the aminoacid next up is neighboring, the chain is reconciled
                if currentFolding[amino + 1] in [left, right, up, down]:
                    break

                # Checks whether there is overlap and/or bondbreaking
                overlap = len(currentFolding) != len(set(changedFolding))
                bondBreak = validityCheck(left, right, up, down, changedFolding,\
                ['simulated annealing', amino])

                # Go to next amino acid
                distanceFromStart += 1
                amino += distanceFromStart


            if not overlap and not bondBreak and distanceFromStart != 0:
                # Calculate the score for a reconciled protein
                changedScore = calculateFolding(changedFolding, Protein.proteinChain)

                # Get the difference between scores of current and tweaked
                differenceScore = currentScore - changedScore
                # print(differenceScore)
                # print(currentScore)
                # print(changedScore)

                # Generate a probability and a random float
                acceptance = int(math.e**(differenceScore/Temp))
                randomInt = random.randint(0,length)

                # Change current if accepted
                if acceptance <= randomInt:
                    currentFolding = changedFolding
                    currentScore = changedScore

                # Add step
                steps += 1
                # print(steps)

        # Change temperature
        Temp *= conservatism
        print(bestScore)

    return [bestFolding, bestScore]
