import matplotlib
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches

# This function takes a string ('proteinChain') and a set of coordinates ('output')
# and uses these to present the user with a visualization of the protein and its H-bonds
def visualizeFolding (Protein):

    proteinChain = Protein.proteinChain
    x = 0
    y = 1

    plotX = []
    plotY = []

    # Iterates over all single amino acids in the protein
    for focus in range(len(proteinChain)):

        current_x = Protein.aminoCoordinates[focus][x]
        current_y = Protein.aminoCoordinates[focus][y]
        plotX.append(current_x)
        plotY.append(current_y)

        if proteinChain[focus] == 'H':
            plot.scatter(current_x, current_y,color='r',s=500,zorder=1)
        else:
            plot.scatter(current_x, current_y,color='b',s=500,zorder=1)

        # Iterates over all the other amino acids in the chain
        for partner in range(len(proteinChain)):

            neighbor_x = Protein.aminoCoordinates[partner][x]
            neighbor_y = Protein.aminoCoordinates[partner][y]

            # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
            # , checks whether these can form an H-bond, and plots those
            if (((abs(current_x - neighbor_x) == 1) and\
            (abs(current_y - neighbor_y) == 0)) or\
            ((abs(current_y - neighbor_y) == 1) and\
            (abs(current_x - neighbor_x) == 0))) and\
            (proteinChain[focus] == 'H' and proteinChain[partner] == 'H'):
                plot.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                , 'r--', linewidth=0.5, zorder=-1)

    # Plots the covalent bonds in the protein
    plot.plot(plotX, plotY, linewidth = 5.0, zorder = 0)

    # Graph info
    plot.title('Strength: ' + str(Protein.strength))
    plot.ylabel('Y axis')
    plot.xlabel('X axis')

    plot.show()

# Calculates the protein stability/strength
def calculateFolding (aminoCoordinates, proteinChain):

    x = 0
    y = 1
    strength = 0

    # Iterates over all single amino acids in the protein
    for focus in range(len(proteinChain)):

        current_x = aminoCoordinates[focus][x]
        current_y = aminoCoordinates[focus][y]

        # Iterates over all the other amino acids in the chain
        for partner in range(len(proteinChain)):

            neighbor_x = aminoCoordinates[partner][x]
            neighbor_y = aminoCoordinates[partner][y]

            # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
            # , checks whether these can form an H-bond, and plots those
            if (((abs(current_x - neighbor_x) == 1) and\
            (abs(current_y - neighbor_y) == 0)) or\
            ((abs(current_y - neighbor_y) == 1) and\
            (abs(current_x - neighbor_x) == 0))) and\
            (proteinChain[focus] == 'H' and proteinChain[partner] == 'H'):
                strength += 0.5

    return strength
