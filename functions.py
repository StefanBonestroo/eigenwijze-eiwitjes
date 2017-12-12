import matplotlib
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D as plot3D

# Prints the correct usage (in a pretty way)
def printUsage():
        print('\nUsage: \n')
        print(' Argument 1: protein string to be folded, e.a. \"HHPHPHP\"')
        print(' Argument 2: desired algorithm -> \'randomizer\', \'depth-first\', \'fragment-randomizer\'')
        print(' Argument 3: desired folding dimensions -> \'2D\' or \'3D\'')
        print(' Argument 4: *optional argument \'tries\' for \'randomizer\' and \'fragment-randomizer\'')
        print(' Argument 5: *optional argument \'fragmentLength\' for \'fragment-randomizer\'\n')


# Calculates the protein stability/strength
def calculateFolding (aminoCoordinates, proteinChain):

    # X & Y's for increased readability
    x = 0
    y = 1
    z = 2

    strength = 0

    if len(aminoCoordinates[0]) == 2:

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            current_x = aminoCoordinates[focus][x]
            current_y = aminoCoordinates[focus][y]

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):
                # print(aminoCoordinates)
                neighbor_x = aminoCoordinates[partner][x]
                neighbor_y = aminoCoordinates[partner][y]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(current_x - neighbor_x) == 1) and\
                (abs(current_y - neighbor_y) == 0)) or\
                ((abs(current_y - neighbor_y) == 1) and\
                (abs(current_x - neighbor_x) == 0))) and\
                (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') and\
                (focus-partner) not in [-1, 0, 1]:
                    strength += 0.5

        return strength


    elif len(aminoCoordinates[0]) == 3:

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            current_x = aminoCoordinates[focus][x]
            current_y = aminoCoordinates[focus][y]
            current_z = aminoCoordinates[focus][z]

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):

                neighbor_x = aminoCoordinates[partner][x]
                neighbor_y = aminoCoordinates[partner][y]
                neighbor_z = aminoCoordinates[partner][z]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(current_x - neighbor_x) == 1) and\
                (abs(current_y - neighbor_y) == 0) and\
                (abs(current_z - neighbor_z) == 0)) or\
                ((abs(current_x - neighbor_x) == 0) and\
                (abs(current_y - neighbor_y) == 1) and\
                (abs(current_z - neighbor_z) == 0)) or\
                ((abs(current_x - neighbor_x) == 0) and\
                (abs(current_y - neighbor_y) == 0) and\
                (abs(current_z - neighbor_z) == 1))) and\
                (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') and\
                (focus - partner) not in [-1, 0, 1]:
                    strength += 0.5

        return strength


# This function takes a string ('proteinChain') and a set of coordinates ('output')
# and uses these to present the user with a visualization of the protein and its H-bonds
def visualizeFolding (Protein):

    proteinChain = Protein.proteinChain
    x = 0
    y = 1
    z = 2

    plotX = []
    plotY = []
    plotZ = []

    if len(Protein.aminoCoordinates[0]) == 2:

        # Initiate figure
        plot2D = plot.figure()

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            current_x = Protein.aminoCoordinates[focus][x]
            current_y = Protein.aminoCoordinates[focus][y]
            plotX.append(current_x)
            plotY.append(current_y)

            if proteinChain[focus] == 'H':
                plot.scatter(current_x,current_y,color='r',s=200,zorder=1)
            else:
                plot.scatter(current_x,current_y,color='b',s=200,zorder=1)

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):

                neighbor_x = Protein.aminoCoordinates[partner][x]
                neighbor_y = Protein.aminoCoordinates[partner][y]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(current_x - neighbor_x) == 1) and\
                (abs(current_y - neighbor_y) == 0)) or\
                ((abs(current_x - neighbor_x) == 0) and\
                (abs(current_y - neighbor_y) == 1))) and\
                (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') and\
                (focus - partner) not in [-1, 0, 1]:
                    plot.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                    , 'r--', linewidth=0.5, zorder=-1)

        # Plots the covalent bonds in the protein
        plot.plot(plotX, plotY, linewidth = 5.0, zorder = 0)

        # Graph info
        plot.title('Strength: ' + str(Protein.strength))
        plot.ylabel('Y axis')
        plot.xlabel('X axis')

        plot.show()


    elif len(Protein.aminoCoordinates[0]) == 3:

        # Initiate 3D plot
        figure3D = plot.figure()
        plot3D = figure3D.add_subplot(111, projection = '3d')

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            current_x = Protein.aminoCoordinates[focus][x]
            current_y = Protein.aminoCoordinates[focus][y]
            current_z = Protein.aminoCoordinates[focus][z]
            plotX.append(current_x)
            plotY.append(current_y)
            plotZ.append(current_z)

            if proteinChain[focus] == 'H':
                plot3D.scatter(current_x, current_y, current_z, c='r', depthshade = 1\
                ,s=200,zorder=1)
            else:
                plot3D.scatter(current_x, current_y, current_z, c='b',depthshade = 1\
                ,s=200,zorder=1)

            # Iterates over all the other amino acids in the chain
            for partner in range(len(proteinChain)):

                neighbor_x = Protein.aminoCoordinates[partner][x]
                neighbor_y = Protein.aminoCoordinates[partner][y]
                neighbor_z = Protein.aminoCoordinates[partner][z]

                # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                # , checks whether these can form an H-bond, and plots those
                if (((abs(current_x - neighbor_x) == 1) and\
                (abs(current_y - neighbor_y) == 0) and\
                (abs(current_z - neighbor_z) == 0)) or\
                ((abs(current_x - neighbor_x) == 0) and\
                (abs(current_y - neighbor_y) == 1) and\
                (abs(current_z - neighbor_z) == 0)) or\
                ((abs(current_x - neighbor_x) == 0) and\
                (abs(current_y - neighbor_y) == 0) and\
                (abs(current_z - neighbor_z) == 1))) and\
                (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') and\
                (focus - partner) not in [-1, 0, 1]:
                    plot3D.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                    , [current_z, neighbor_z],'r--', linewidth=0.5, zorder=-1)

        # Plots the covalent bonds in the protein
        plot3D.plot(plotX, plotY, plotZ, linewidth = 5.0, zorder = 0)

        # Graph info
        plot3D.text2D(0.5, 0.95,'Strength: ' + str(Protein.strength), transform = plot3D.transAxes)
        plot3D.set_ylabel('Y axis')
        plot3D.set_xlabel('X axis')
        plot3D.set_zlabel('Z axis')

        plot.show()
