# Heuristieken 2017
# Branch and bound
# https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
from random import randint

class Protein:

    def __init__(self, proteinChain, loops):

        self.proteinChain = proteinChain
        self.proteinDict = {'x-cord': [], 'y-cord': [], 'type': []}
        self.tries = loops

def makeChainStructure(self, amino_zuur, counter, coordinates):
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

    class Amino:
        def __init__(self, position):
            self.position = position
            self.upper = None
            self.right = None
            self.lower = None
            self.left = None

counter = 0
coordinates= [(0,0)]
first_amino = Amino(counter)
counter = 1
#print(first_amino)

protie.makeChainStructure(first_amino, counter, coordinates)
#protie.culculateFolding
if __name__=='__main__':
    main()
