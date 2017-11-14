# Heuristieken 2017
# Branch and bound
# https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
from random import randint

class Protein:

    def __init__(self, proteinChain, loops):

        self.proteinChain = proteinChain
        self.proteinDict = {'x-cord': [], 'y-cord': [], 'type': []}
        self.tries = loops

        self.bestProteinDict = None
        self.strength = 0
        self.exist = [(0, 0), (0, 1)]

        for round in range(len(proteinChain)):
            self.proteinDict["x-cord"].append(0)
            self.proteinDict["y-cord"].append(0)
            self.proteinDict["type"].append(proteinChain[round])

        self.makeChainStructure(self.proteinDict, len(proteinChain))

    def makeChainStructure(self, values, amount):
        for amino in range(2,amount):
            currentLocation = self.exist[amino - 1]
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1))
            down = (currentLocation[0], (currentLocation[1] - 1))
            # down = (currentLocation[0], (currentLocation[1] - 1))
            while True:
                x = randint(1,4)
                if x == 1 and left not in self.exist: # links
                    self.exist.append(left)
                    self.proteinDict['x-cord'][amino] = left[0]
                    self.proteinDict['y-cord'][amino] = left[1]
                    break
                elif x == 2 and right not in self.exist: # rechts
                    self.exist.append(right)
                    self.proteinDict['x-cord'][amino] = right[0]
                    self.proteinDict['y-cord'][amino] = right[1]
                    break
                elif x == 3 and up not in self.exist: # boven
                    self.exist.append(up)
                    self.proteinDict['x-cord'][amino] = up[0]
                    self.proteinDict['y-cord'][amino] = up[1]
                    break
                elif x == 4 and down not in self.exist: # onder
                    self.exist.append(down)
                    self.proteinDict['x-cord'][amino] = down[0]
                    self.proteinDict['y-cord'][amino] = down[1]
                    break
            elif [left, up, down, right] in self.exist:
                    self.reset()


        self.calculateFolding(self.proteinDict, amount)

    def calculateFolding (self, values, amount):
        strength = 0
        for amino in range(amount):
            location = (values['x-cord'][amino], values['y-cord'][amino])
            surrounding = [(location[0] - 1, location[1]), (location[0] + 1, location[1]), (location[0], location[1] + 1), (location[0], location[1] - 1)]
            if values['type'][amino] == 'H':
                # position = values['type'][amino]
                for checks in range(amount):
                    if values['type'][checks] == "H" and (values['x-cord'][checks], values['y-cord'][checks]) in surrounding and (amino - checks) not in [-1, 0, 1]:
                        strength += 0.5
        self.bestFolding(strength, values, self.tries)

    # def visualizeFolding (self):

    # stores the calculate folding and visualize folding of the best posible folding done
    def bestFolding (self, strength, values, loops):
        if self.strength < strength:
            self.bestProteinDict = values
            self.strength = strength

        if loops > 0:
            self.tries = loops - 1
            self.reset()

    def reset (self):
        self.exist = [(0, 0), (0, 1)]
        self.makeChainStructure(self.proteinDict, len(self.proteinChain))

def main():
    protie = Protein("HHPHHHPHPHHHPH", 2)
    print (protie.bestProteinDict)
    print (protie.strength)

if __name__ == "__main__":
    main()
