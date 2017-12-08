# This function takes a folded protein and refolds a fragment of a defined length
# in a randomized matter.
import random

from classes import Protein
from random import randint
from functions import calculateFolding, visualizeFolding
from Algorithms import helpers
from Algorithms import randomizer

def fragmentRandomizer (Protein, trieMax, dimension, fragment):

    tries = 0

    # Get the best protein from a 100 random foldings
    output = randomizer(Protein, 100, dimension)
    Protein.aminoCoordinates = output[0]
    Protein.strength = output[1]

    origPro = Protein
    oldScore = OrigPro.strength

    while tries < trieMax:

        # Define start as random amino acid at least a fragment length before the end of the protein.
        start = len(origPro.proteinChain)
        # print('stoppoint: ', (len(origPro.proteinChain) - fragment))
        while start >= (len(origPro.proteinChain) - fragment):
            start = randint(0, (len(origPro.proteinChain) - fragment))

        stop = start + fragment
        shifts = []

        for amino in range(start, stop):
            # Append the shift in coordinates
            if dimension == '2D':
                shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
                origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1]))
            else:
                shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
                origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1],
                origPro.aminoCoordinates[amino + 1][2] - origPro.aminoCoordinates[amino][2]))

        check = 0
        while(check == 0):
            # Initialize a list of new coordinates for the fragment
            newCoordinates = [(origPro.aminoCoordinates[start][0],origPro.aminoCoordinates[start][1])]

            # Find a new coordinate for every aminoacid of the fragment
            az = 0
            while az <= fragment:

                newCtries = 0

                while newCtries < len(shifts):

                    # Break when there was no coordinate added for last az
                    # Break if there are already (fragmentlen) coordinates in newCoordinates and they are identical to original coordinates
                    if az == len(newCoordinates) or (az == fragment-1 and newCoordinates == origPro.aminoCoordinates[start:stop]):
                        break

                    shifts = shifts # dit was nodig om de random.shuffle te laten werken
                    random.shuffle(shifts)

                    # print('az: ', az, ', start: ', start, 'newCoordinates: ', newCoordinates)
                    newShift = (shifts[newCtries])
                    # new coordinate that will be tested for validity
                    newC = (newCoordinates[az][0] + newShift[0] , newCoordinates[az][1] + newShift[1])

                    if (newC not in origPro.aminoCoordinates[0:start + az]
                    and newC not in origPro.aminoCoordinates[stop + 1:]
                    and newC not in newCoordinates):
                        # Found a possible coordinate -> remove this shift from possibilities for the other amino acids
                        shifts.remove(newShift)

                        # Add new coordinate
                        newCoordinates.append(newC)
                        break

                    newCtries += 1

                # print(az)
                if az == len(newCoordinates) and az != fragment:
                    break
                az +=1
            # If it finds new possible coordinates, check the score change
            if len(newCoordinates) == fragment + 1:

                # Create protein with these coordinates for the fragments
                newPro = Protein(origPro.proteinChain)
                newPro.aminoCoordinates = origPro.aminoCoordinates[0:start ]
                newPro.aminoCoordinates.extend(newCoordinates)
                newPro.aminoCoordinates.extend(origPro.aminoCoordinates[stop + 1:])

                # Compare score with old protein
                newPro.strength = calculateFolding(newPro.aminoCoordinates, newPro.proteinChain)

                if newPro.strength > origPro.strength:
                    origPro = newPro
                    visualizeFolding(origPro)

                # Probability of acceptance

            check = 1


        tries +=1
