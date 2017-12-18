# This protein class is build to contain all the basic information a protein object
# must have in order to be folded by its visualizeFolding function.

import os

import matplotlib
import matplotlib.pyplot as plot
import matplotlib.axes as axis
from mpl_toolkits.mplot3d import Axes3D as plot3D

class Protein:

    def __init__(self, proteinChain):
        # string of amino acids chars
        self.proteinChain = proteinChain

        # location coordinates and amino acid type
        self.aminoCoordinates = []
        self.strength = 0

    # This function takes a string ('self.proteinChain') and a set of coordinates ('output')
    # and uses these to present the user with a visualization of the protein and its H-bonds
    def visualizeFolding (self, save):
        """ Visualizes a 2D or 3D protein (this includes 'H-bonds') """

        x = 0
        y = 1
        z = 2

        plotX = []
        plotY = []
        plotZ = []

        if len(self.aminoCoordinates[0]) == 2:
            Is2D = True
            Is3D = False
        else:
            Is2D = False
            Is3D = True

        # Initiate figure
        if Is3D:
            figure3D = plot.figure()
            plot3D = figure3D.add_subplot(111, projection = '3d')

        # Iterates over all single amino acids in the protein
        for focus in range(len(self.proteinChain)):

            currentX = self.aminoCoordinates[focus][x]
            currentY = self.aminoCoordinates[focus][y]
            plotX.append(currentX)
            plotY.append(currentY)

            if Is3D:
                currentZ = self.aminoCoordinates[focus][z]
                plotZ.append(currentZ)

            # Plots all the amino acids
            if Is2D:
                if self.proteinChain[focus] == 'H':
                    plot.scatter(currentX,currentY,color='r',s=100,zorder=1)
                elif self.proteinChain[focus] == 'C':
                    plot.scatter(currentX,currentY,color='y',s=100,zorder=1)
                else:
                    plot.scatter(currentX,currentY,color='b',s=100,zorder=1)

            if Is3D:
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
                if Is3D:
                    neighborZ = self.aminoCoordinates[partner][z]

                # Checks whether 'partner' amino acid neighbors 'focus' amino acid
                # , checks whether these can form an H-bond, and plots those
                if Is2D and any([(abs(currentX - neighborX) == 1) and\
                     (abs(currentY - neighborY) == 0),\
                     (abs(currentX - neighborX) == 0) and\
                     (abs(currentY - neighborY) == 1)]) and\
                     (focus - partner) not in [-1, 0, 1]:

                     # H-H, C-H, and H-C show connections
                    if any([(self.proteinChain[focus] == 'H' and\
                            self.proteinChain[partner] == 'H'),
                            (self.proteinChain[focus] == 'C' and\
                            self.proteinChain[partner] == 'H'),
                            (self.proteinChain[focus] == 'H' and\
                            self.proteinChain[partner] == 'C')]):

                        plot.plot([currentX, neighborX],[currentY,neighborY]\
                        , 'r--', linewidth=1, zorder=-1)

                    # C-C connections are yellow (more points)
                    elif self.proteinChain[focus] == 'C' and\
                         self.proteinChain[partner] == 'C':

                        plot.plot([currentX, neighborX],[currentY,neighborY]\
                        , 'y--', linewidth=1, zorder=-1)

                elif Is3D and any([(abs(currentX - neighborX) == 1) and\
                    (abs(currentY - neighborY) == 0) and\
                    (abs(currentZ - neighborZ) == 0),
                    (abs(currentX - neighborX) == 0) and\
                    (abs(currentY - neighborY) == 1) and\
                    (abs(currentZ - neighborZ) == 0),
                    (abs(currentX - neighborX) == 0) and\
                    (abs(currentY - neighborY) == 0) and\
                    (abs(currentZ - neighborZ) == 1)]) and\
                    (focus - partner) not in [-1, 0, 1]:

                        # H-H, C-H, and H-C show connections
                        if any([(self.proteinChain[focus] == 'H' and\
                               self.proteinChain[partner] == 'H'),
                               (self.proteinChain[focus] == 'C' and\
                               self.proteinChain[partner] == 'H'),
                               (self.proteinChain[focus] == 'H' and\
                               self.proteinChain[partner] == 'C')]):

                               plot3D.plot([currentX,neighborX],[currentY,neighborY],\
                               [currentZ,neighborZ], 'r--', linewidth=1, zorder=-1)

                        # C-C connections are yellow (more points)
                        elif self.proteinChain[focus] == 'C' and\
                             self.proteinChain[partner] == 'C':

                               plot3D.plot([currentX,neighborX],[currentY,neighborY],\
                               [currentZ,neighborZ], 'y--', linewidth=1, zorder=-1)

        # Plots the covalent bonds in the protein
        if Is2D:

            plot.plot(plotX, plotY, linewidth = 0.5, zorder = 0)

            # Graph info
            plot.title('Strength: ' + str(self.strength))
            plot.axis('off')

        else:
            plot3D.plot(plotX, plotY, plotZ, linewidth = 0.5, zorder = 0)

            # Graph info
            plot3D.text2D(0.5, 0.95,'Strength: ' + str(self.strength),\
            transform = plot3D.transAxes)
            plot3D.axis('off')

        # Provides save possibilities
        if save and Is2D:

            myPath = os.path.dirname(os.path.abspath(__file__))
            myFile = '/Experimentation/Safe-Space/'+ self.proteinChain + '.png'
            plot.savefig(myPath + myFile)
            plot.show()
            plot.clf()

        else:
            plot.show()
