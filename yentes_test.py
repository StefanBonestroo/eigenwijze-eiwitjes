# Heuristieken 2017
# Branch and bound
# https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
from random import randint

class Protein:

    def __init__(self, proteinChain, loops):

        self.proteinChain = proteinChain
        self.proteinDict = {'x-cord': [], 'y-cord': [], 'type': []}
        self.tries = loops

direct = random.choice([amino_zuur.left,amino_zuur.right,amino_zuur.upper,amino_zuur.lower])
    print
    if direct == amino_zuur.left:
        new_position = (coordinates[len(coordinates) - 1][0] - 1,coordinates[len(coordinates) - 1][1])
    elif direct == amino_zuur.right:
        new_position = (coordinates[len(coordinates) - 1][0] + 1,coordinates[len(coordinates) - 1][1])
    elif direct == amino_zuur.down:
        new_position = (coordinates[len(coordinates) - 1][0],coordinates[len(coordinates) - 1][1] - 1)
    elif direct == amino_zuur.upper:
        new_position = (coordinates[len(coordinates) - 1][0],coordinates[len(coordinates) - 1][1] + 1)

    coordinates.append(new_position)
    print coordinates
    counter += 1
    direct = Amino(counter)
    self.makeChainStructure(direct, counter, coordinates)
