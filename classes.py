import matplotlib
import matplotlib.pyplot as plot
import matplotlib.axes as axis
from mpl_toolkits.mplot3d import Axes3D as plot3D

class Protein:

    def __init__(self, self.proteinChain):
        # string of amino acids chars
        self.self.proteinChain = self.proteinChain

        # location coordinates and amino acid type
        self.self.aminoCoordinates = []
        self.strength = 0

    # This function takes a string ('self.proteinChain') and a set of coordinates ('output')
    # and uses these to present the user with a visualization of the protein and its H-bonds
    def visualizeFolding ():

        x = 0
        y = 1
        z = 2

        plotX = []
        plotY = []
        plotZ = []

        if len(self.aminoCoordinates[0]) == 2:

            # Initiate figure
            plot2D = plot.figure()

            # Iterates over all single amino acids in the protein
            for focus in range(len(self.proteinChain)):

                currentX = self.aminoCoordinates[focus][x]
                currentY = self.aminoCoordinates[focus][y]
                plotX.append(currentX)
                plotY.append(currentY)

                if self.proteinChain[focus] == 'H':
                    plot.scatter(currentX,currentY,color='r',s=100,zorder=1)
                elif self.proteinChain[focus] == 'C':
                    plot.scatter(currentX,currentY,color='y',s=100,zorder=1)
                else:
                    plot.scatter(currentX,currentY,color='b',s=100,zorder=1)

                # Iterates over all the other amino acids in the chain
                for partner in range(len(self.proteinChain)):

                    neighborX = self.aminoCoordinates[partner][x]
                    neighborY = self.aminoCoordinates[partner][y]

                    # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                    # , checks whether these can form an H-bond, and plots those
                    if (((abs(currentX - neighborX) == 1) and\
                    (abs(currentY - neighborY) == 0)) or\
                    ((abs(currentX - neighborX) == 0) and\
                    (abs(currentY - neighborY) == 1))) and\
                    (focus - partner) not in [-1, 0, 1]:
                        if (self.proteinChain[focus] == 'H' and self.proteinChain[partner] == 'H') or\
                        (self.proteinChain[focus] == 'C' and self.proteinChain[partner] == 'H') or\
                        (self.proteinChain[focus] == 'H' and self.proteinChain[partner] == 'C'):
                            plot.plot([currentX, neighborX],[currentY,neighborY]\
                            , 'r--', linewidth=1, zorder=-1)
                        elif self.proteinChain[focus] == 'C' and self.proteinChain[partner] == 'C':
                            plot.plot([currentX, neighborX],[currentY,neighborY]\
                            , 'y--', linewidth=1, zorder=-1)

            # Plots the covalent bonds in the protein
            plot.plot(plotX, plotY, linewidth = 0.5, zorder = 0)

            # Graph info
            plot.title('Strength: ' + str(self.strength))
            plot.axis('off')

            plot.show()


        elif len(self.aminoCoordinates[0]) == 3:

            # Initiate 3D plot
            figure3D = plot.figure()
            plot3D = figure3D.add_subplot(111, projection = '3d')

            # Iterates over all single amino acids in the protein
            for focus in range(len(self.proteinChain)):

                currentX = self.aminoCoordinates[focus][x]
                currentY = self.aminoCoordinates[focus][y]
                currentZ = self.aminoCoordinates[focus][z]
                plotX.append(currentX)
                plotY.append(currentY)
                plotZ.append(currentZ)

                if self.proteinChain[focus] == 'H':
                    plot3D.scatter(currentX,currentY,currentZ,c='r',s=100,zorder=1)
                elif self.proteinChain[focus] == 'C':
                    plot3D.scatter(currentX,currentY,currentZ,c='y',s=100,zorder=1)
                else:
                    plot3D.scatter(currentX,currentY,currentZ,c='b',s=100,zorder=1)

                # Iterates over all the other amino acids in the chain
                for partner in range(len(self.proteinChain)):

                    neighborX = self.aminoCoordinates[partner][x]
                    neighborY = self.aminoCoordinates[partner][y]
                    neighborZ = self.aminoCoordinates[partner][z]

                    # Checks whether the 'partner' amino acid neighbors the 'focus' amino acids
                    # , checks whether these can form an H-bond, and plots those
                    if (((abs(currentX - neighborX) == 1) and\
                    (abs(currentY - neighborY) == 0) and\
                    (abs(currentZ - neighborZ) == 0)) or\
                    ((abs(currentX - neighborX) == 0) and\
                    (abs(currentY - neighborY) == 1) and\
                    (abs(currentZ - neighborZ) == 0)) or\
                    ((abs(currentX - neighborX) == 0) and\
                    (abs(currentY - neighborY) == 0) and\
                    (abs(currentZ - neighborZ) == 1))) and\
                    (focus - partner) not in [-1, 0, 1]:
                        if (self.proteinChain[focus] == 'H' and self.proteinChain[partner] == 'H') or\
                        (self.proteinChain[focus] == 'C' and self.proteinChain[partner] == 'H') or\
                        (self.proteinChain[focus] == 'H' and self.proteinChain[partner] == 'C'):
                            plot3D.plot([currentX,neighborX],[currentY,neighborY],\
                            [currentZ,neighborZ], 'r--', linewidth=1, zorder=-1)
                        elif self.proteinChain[focus] == 'C' and self.proteinChain[partner] == 'C':
                            plot3D.plot([currentX,neighborX],[currentY,neighborY],\
                            [currentZ,neighborZ], 'y--', linewidth=1, zorder=-1)

            # Plots the covalent bonds in the protein
            plot3D.plot(plotX, plotY, plotZ, linewidth = 0.5, zorder = 0)

            # Graph info
            plot3D.text2D(0.5, 0.95,'Strength: ' + str(self.strength), transform = plot3D.transAxes)
            plot3D.axis('off')

            plot.show()
