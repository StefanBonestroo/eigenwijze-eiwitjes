import matplotlib
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import plot3D

# Calculates the protein stability/strength
def calculateFolding (aminoCoordinates, proteinChain, dimension):

    # X & Y's for increased readability
    x = 0
    y = 1
    z = 2

    strength = 0

    if dimension == '2D':

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

                (proteinChain[focus] == 'H' and proteinChain[partner] == 'H') and\
                (focus-partner) not in [-1, 0, 1]:
                    strength += 0.5

        return strength


    elif dimension == '3D':

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
def visualizeFolding (Protein, dimension):

    proteinChain = Protein.proteinChain
    x = 0
    y = 1

    plotX = []
    plotY = []
    plotZ = []

    if dimension == '2D':

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
                    plot3D.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                    , 'r--', linewidth=0.5, zorder=-1)

        # Plots the covalent bonds in the protein
        plot.plot(plotX, plotY, linewidth = 5.0, zorder = 0)

        # Graph info
        plot.title('Strength: ' + str(Protein.strength))
        plot.ylabel('Y axis')
        plot.xlabel('X axis')

        plot.show()


    elif dimension == '3D':

        # Iterates over all single amino acids in the protein
        for focus in range(len(proteinChain)):

            current_x = Protein.aminoCoordinates[focus][x]
            current_y = Protein.aminoCoordinates[focus][y]
            current_z = Protein.aminoCoordinates[focus][z]
            plotX.append(current_x)
            plotY.append(current_y)
            plotX.append(current_z)

            if proteinChain[focus] == 'H':
                plot3D.scatter(current_x, current_y, current_z, color='r',s=200,zorder=1)
            else:
                plot3D.scatter(current_x, current_y, current_z, color='b',s=200,zorder=1)

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
        plot3D.title('Strength: ' + str(Protein.strength))
        plot3D.ylabel('Y axis')
        plot3D.xlabel('X axis')
        plot3D.zlabel('Z axis')

        plot3D.show()
        
