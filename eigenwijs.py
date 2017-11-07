# Heuristieken 2017
# Branch and bound
# https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
from random import randint

class Protein:

    def __init__(self, proteinChain):

        self.proteinChain = proteinChain
        self.proteinDict = {}
        self.bestProteinDict = None
        self.strength = None

        for round in range(len(proteinChain)):
            self.proteinDict[round] = (0, 0), proteinChain[round], round

        makeChainStructure(len(proteinChain))

        # protie = Protein("HHPPHH")
        # print (protie.proteinDict)
        # print (protie.proteinDict[2][1])

    def makeChainStructure(self, amount):
        for Amino in range(1,amount):
            currentLocation = self.visulizeFolding.exist[Amino - 1]
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1)
            downt = (currentLocation[0], (currentLocation[1] + 1))
            # downt = (currentLocation[0], (currentLocation[1] - 1))
            while True:
                x = randint(1,4)
                if x == 1 and left not in self.visulizeFolding.exist: # links
                    self.visualizeFolding.exist.add(left)
                    self.proteinDict[Amino][0] = left
                    break
                elif x == 2 and right not in self.visulizeFolding.exist: # rechts
                    self.visualizeFolding.exist.add(right)
                    self.proteinDict[Amino][0] = right
                    break
                elif x == 3 and up not in self.visulizeFolding.exist: # boven
                    self.visualizeFolding.exist.add(up)
                    self.proteinDict[Amino][0] = up
                    break
                elif x == 4 and downt not in self.visulizeFolding.exist: # onder
                    self.visualizeFolding.exist.add(downt)
                    self.proteinDict[Amino][0] = downt
                    break
                elif [left, right, up, downt] in self.visualizeFolding.exist: # Als fouwing vast loopt
                    Amino = amaount
                    break

        self.calculateFolding(self.proteinDict, amount)

    def calculateFolding (self, values, amount):
        strength = 0
        for Amino in amount:
            location = values[amino][0]
            left = (location[0] - 1, location[1])
            right = (location[0] + 1, location[1])
            up = (location[0], location[1] + 1)
            downt = (location[0], location[1] - 1)
            for checks in amount:
                if values[Amino][1] = "H":
                    position = values[Amino][2]
                    if values[checks][0] in [left, right, up, downt] and values[checks][1] == "H" and values[checks][2] not in [positon, position - 1, position + 1]:
                        strength += 0.5
        self.bestFolding(strength, values)

    def visualizeFolding (self):
        self.exist = [(0, 0)]     # met hierin [(1,0), (3,2)]

    # stores the calculate folding and visualize folding of the best posible folding done
    def bestFolding (self, strength, values):
        if self.strength == None:
            self.bestProteinDict = values
            self.strength = strength
        elif self.strength < strength:
            self.bestProteinDict = values
            self.strength = strength

main():
    protie = Protein("PPHHHPHHHPH")
    print (protie.bestProteinDict)

if __name__ == "__main__":
    main()
