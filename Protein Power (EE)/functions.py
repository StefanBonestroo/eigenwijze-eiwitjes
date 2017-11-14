from random import randint
import matplotlib
import matplotlib.pyplot as plot
import Classes.Protein as Protein

# This function takes a string ('proteinChain') and a set of coordinates ('output')
# and uses these to present the user with a visualization of the protein and its H-bonds
def visualizeFolding (self, proteinChain, output):

    # Iterates over all single amino acids in the protein
    for focus in range(len(proteinChain)):

        current_x = output['x-cor'][focus]
        current_y = output['y-cor'][focus]

        # Iterates over all the other amino acids in the chain
        for partner in range(len(proteinChain)):

            neighbor_x = output['x-cor'][partner]
            neighbor_y = output['y-cor'][partner]

            # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
            # and checks whether these can form an H-bond
            if (((abs(current_x - neighbor_x) == 1) and\
            (abs(current_y - neighbor_y) == 0)) or\
            ((abs(current_y - neighbor_y) == 1) and\
            (abs(current_x - neighbor_x) == 0))) and\
            (output['type'][focus] == 'H' and output['type'][partner] == 'H'):
                plot.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                , 'r--', linewidth=0.5, zorder=-1)

    # Plots the covalent bonds in the protein
    plot.plot(output['x-cor'],output['y-cor'], linewidth = 5.0, zorder = 0)

    # Plots the single amino acids as H's (red) or P's (blue)
    for acids in range(len(proteinChain)):
        if output['type'][acids] == 'H':
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='r', s=500, zorder=1)
        else:
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='b', s=500, zorder=1)

    # Graph info
    plot.title('Protein shizzle')
    plot.ylabel('Y axis')
    plot.xlabel('X axis')

    plot.show()

def calculateFolding (self, values, amount):
    strength = 0
    for amino in range(amount):
        location = self.exist[amino]
        surrounding = [(location[0] - 1, location[1]), (location[0] + 1, location[1]), (location[0], location[1] + 1), (location[0], location[1] - 1)]
        if values['type'][amino] == 'H':
            for checks in range(amount):
                if values['type'][checks] == "H" and self.exist[checks] in surrounding and (amino - checks) not in [-1, 0, 1]:
                    strength += 0.5
    self.bestFolding(strength, self.proteinDict, self.tries)
