# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random
import math

from classes import Protein
from random import randint
from Algorithms import helpers, randomizer
from Algorithms.randomizer import randomizer
from Algorithms.helpers import possibilityCheck, validityCheck, calculateFolding

def fragmentRandomizer (inputPro, fragment, dimension, trieMax):
    """ The fragment-randomizer is a simulated annealing type algorithm, which
    tweaks random fragments to give better strengths. """

    # Get the best protein from a 100 random foldings
    go = 0

    while go == 0:

        randomPro = randomizer(inputPro, trieMax, dimension)

        if randomPro.strength != 0:
            go = 1

    origPro = randomPro
    bestPro = origPro

    invalidFold = 0
    temp = 3.5

    while temp > 0.1:

        # Define start as random amino acid
        start = len(origPro.proteinChain)

        while start > (len(origPro.proteinChain) - fragment):

            start = randint(0, (len(origPro.proteinChain) - fragment))

        if(start == 0):
            newCoordinates = beginFragment(origPro, fragment, dimension)
        elif(start == len(origPro.proteinChain) - fragment):
            newCoordinates = endFragment(origPro, start, fragment, dimension)
        elif(start < len(origPro.proteinChain) - fragment):
            middleInfo = middleFragment(origPro, start, fragment, dimension)
            newCoordinates = middleInfo[0]

        if newCoordinates != 'none':

                # Create protein with these coordinates for the fragments
                newPro = Protein(origPro.proteinChain)

                # Start fragment
                if(start == 0):

                    newPro.aminoCoordinates = newCoordinates
                    newPro.aminoCoordinates.extend(origPro.aminoCoordinates[fragment:])

                # End fragment
                elif(start == len(origPro.proteinChain) - fragment):

                    newPro.aminoCoordinates = origPro.aminoCoordinates[0 : start]
                    newPro.aminoCoordinates.extend(newCoordinates)

                # Middle fragment
                elif(start < len(origPro.proteinChain) - fragment):

                    newPro.aminoCoordinates = origPro.aminoCoordinates[0 : start]
                    newPro.aminoCoordinates.extend(newCoordinates)
                    newPro.aminoCoordinates.extend(origPro.aminoCoordinates[middleInfo[1] + 1:])


                # Compare score with old protein
                newPro.strength = calculateFolding(newPro.aminoCoordinates, newPro.proteinChain)

                # Calculate probability of acceptance (simulated annealing)
                probab = min(1,(math.expm1(newPro.strength/temp)/math.expm1(origPro.strength/temp)))

                randumb = random.uniform(0,1)

                if probab > randumb:
                    origPro = newPro
                    if origPro.strength > bestPro.strength:
                        bestPro = origPro

                temp *= 0.9998
                invalidFold = 0

        # It is undesireble for a protein to keep folding a conformation that
        # will not work, this prevents excessive folding of a doomed protein.
        else:
            invalidFold += 1
            if invalidFold > 20:
                bestPro = fragmentRandomizer(inputPro, fragment, dimension, trieMax)


    return(bestPro)

def middleFragment(origPro, start, fragment, dimension):
    """ This is a middle fragment specialized function. """

    stop = start + fragment
    shifts = []

    for amino in range(start, stop):
        # append the shift in coordinates
        if dimension == '2D':
            shifts.append((origPro.aminoCoordinates[amino + 1][0] - \
                        origPro.aminoCoordinates[amino][0],
                        origPro.aminoCoordinates[amino + 1][1] - \
                        origPro.aminoCoordinates[amino][1]))
        else:
            shifts.append((origPro.aminoCoordinates[amino + 1][0] - \
                        origPro.aminoCoordinates[amino][0],
                        origPro.aminoCoordinates[amino + 1][1] - \
                        origPro.aminoCoordinates[amino][1],
                        origPro.aminoCoordinates[amino + 1][2] - \
                        origPro.aminoCoordinates[amino][2]))

    check = 0
    while(check == 0):
        # initialize a list of new coordinates for the fragment
        if dimension == '2D':
            newCoordinates = [(origPro.aminoCoordinates[start][0], \
                            origPro.aminoCoordinates[start][1])]
        else:
            newCoordinates = [(origPro.aminoCoordinates[start][0], \
                            origPro.aminoCoordinates[start][1], \
                            origPro.aminoCoordinates[start][2])]
        # find a new coordinate for every aminoacid of the fragment
        az = 0
        while az <= fragment:

            newCtries = 0
            shifts = shifts # dit was nodig om de random.shuffle te laten werken
            random.shuffle(shifts)

            # trie different shifts for this az
            while newCtries < len(shifts):

                # break when there was no coordinate added for last az
                # break if there are already (fragmentlen) coordinates in
                # newCoordinates and they are identical to original coordinates
                if az == len(newCoordinates) or\
                 (az == fragment - 1 and newCoordinates == origPro.aminoCoordinates[start:stop]):
                    break

                newShift = (shifts[newCtries])

                # new coordinate that will be tested for validity
                if dimension == '2D':
                    newC = (newCoordinates[az][0] + newShift[0] , \
                            newCoordinates[az][1] + newShift[1])
                else:
                    newC = (newCoordinates[az][0] + newShift[0] , \
                            newCoordinates[az][1] + newShift[1], \
                            newCoordinates[az][2] + newShift[2])

                if (newC not in origPro.aminoCoordinates[0:start + az]
                and newC not in origPro.aminoCoordinates[stop + 1:]
                and newC not in newCoordinates):

                    # Found a possible coordinate -> remove this shift from
                    # possibilities for the other amino acids
                    shifts.remove(newShift)
                    newCoordinates.append(newC)

                    # A possible shift was found, so break the while loop
                    break

                # Shift created an already excisting coordinate so try again
                newCtries += 1

            # (Could not find a shift for last az?)
            if az == len(newCoordinates) and az != fragment:
                break

            az +=1
        # If it finds new possible coordinates, return them
        if len(newCoordinates) == fragment + 1:
            return(newCoordinates, stop)
        else:
            return('none', stop)


        check = 1

def endFragment(origPro, start, fragment, dimension):
    """ This is a middle fragment specialized function. """

    newCoordinates = origPro.aminoCoordinates[0:start]

    for amino in range(start, start + fragment):
        possibilities = possibilityCheck(amino, newCoordinates[0:amino])
        valid = validityCheck(possibilities, newCoordinates, 'randomizer')
        if valid != None:
            newCoordinates.append(valid)
        else:
            return 'none'
    return(newCoordinates[start:])

def beginFragment(origPro, fragment, dimension):
    """ This is a middle fragment specialized function. """

    newCoordinates = origPro.aminoCoordinates[fragment:]

    for i in range(fragment):
        possibilities = possibilityCheck(1, newCoordinates)
        valid = validityCheck(possibilities, newCoordinates, 'randomizer')
        if valid != None:
            oldCoordinates = newCoordinates
            newCoordinates = [valid]
            newCoordinates.extend(oldCoordinates)

        else:
            return 'none'
    return(newCoordinates[:fragment])
