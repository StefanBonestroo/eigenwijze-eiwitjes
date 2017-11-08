# Heuristieken 2017
# Branch and bound
# https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
from random import randint
import matplotlib.pyplot as plot
import matplotlib

matplotlib.style.use('seaborn-paper')

class Protein:

    def __init__(self, proteinChain, loops):

        self.proteinChain = proteinChain
        self.proteinDict = {'x-cor': [], 'y-cor': [], 'type': []}
        self.tries = loops

        self.bestProteinDict = None
        self.strength = 0
        self.exist = [(0, 0), (0, 1)]

        for round in range(len(proteinChain)):
            if round == 1:
                self.proteinDict["y-cor"].append(1)
            else:
                self.proteinDict["y-cor"].append(0)
            self.proteinDict["x-cor"].append(0)
            self.proteinDict["type"].append(proteinChain[round])

        self.makeChainStructure(self.proteinDict, len(proteinChain))

    def makeChainStructure(self, values, amount):
        for amino in range(2,amount):
            currentLocation = self.exist[amino - 1]
            left = ((currentLocation[0] - 1), currentLocation[1])
            right = ((currentLocation[0] + 1), currentLocation[1])
            up = (currentLocation[0], (currentLocation[1] + 1))
            down = (currentLocation[0], (currentLocation[1] - 1))
            while True:
                x = randint(1,4)
                if x == 1 and left not in self.exist: # links
                    self.exist.append(left)
                    self.proteinDict['x-cor'][amino] = left[0]
                    self.proteinDict['y-cor'][amino] = left[1]
                    break
                elif x == 2 and right not in self.exist: # rechts
                    self.exist.append(right)
                    self.proteinDict['x-cor'][amino] = right[0]
                    self.proteinDict['y-cor'][amino] = right[1]
                    break
                elif x == 3 and up not in self.exist: # boven
                    self.exist.append(up)
                    self.proteinDict['x-cor'][amino] = up[0]
                    self.proteinDict['y-cor'][amino] = up[1]
                    break
                elif x == 4 and down not in self.exist: # onder
                    self.exist.append(down)
                    self.proteinDict['x-cor'][amino] = down[0]
                    self.proteinDict['y-cor'][amino] = down[1]
                    break
                elif left in self.exist and right in self.exist and up in self.exist and down in self.exist:
                    self.reset()


        self.calculateFolding(self.proteinDict, amount)

    def calculateFolding (self, values, amount):
        strength = 0
        for amino in range(amount):
            location = (values['x-cor'][amino], values['y-cor'][amino])
            surrounding = [(location[0] - 1, location[1]), (location[0] + 1, location[1]), (location[0], location[1] + 1), (location[0], location[1] - 1)]
            if values['type'][amino] == 'H':
                for checks in range(amount):
                    if values['type'][checks] == "H" and (values['x-cor'][checks], values['y-cor'][checks]) in surrounding and (amino - checks) not in [-1, 0, 1]:
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
        else:
            self.visualize(self.bestProteinDict, len(self.proteinChain))

    def reset (self):
        self.exist = [(0, 0), (0, 1)]
        self.makeChainStructure(self.proteinDict, len(self.proteinChain))

    def visualize (self, output, lengthoutput):
        for one in range(lengthoutput):
            for two in range(lengthoutput):

                current_x = output['x-cor'][one]
                neighbor_x = output['x-cor'][two]
                current_y = output['y-cor'][one]
                neighbor_y = output['y-cor'][two]

                if (((abs(current_x - neighbor_x) == 1) and\
                (abs(current_y - neighbor_y) == 0)) or\
                ((abs(current_y - neighbor_y) == 1) and\
                (abs(current_x - neighbor_x) == 0))) and\
                (output['type'][one] == 'H' and output['type'][two] == 'H'):
                    plot.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                    , 'r--', linewidth=0.5, zorder=-1)

        plot.plot(output['x-cor'],output['y-cor'], linewidth = 5.0, zorder = 0)

        for acids in range(lengthoutput):
            if output['type'][acids] == 'H':
                plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
                , color='r', s=2000, zorder=1)
            else:
                plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
                , color='b', s=2000, zorder=1)

        plot.title('Protein shizzle')
        plot.ylabel('Y axis')
        plot.xlabel('X axis')

        plot.show()

def main():
    protie = Protein("HHPHHHPHPHHHPH", 200)
    print (protie.bestProteinDict)
    print (protie.strength)

if __name__ == "__main__":
    main()
