import os

from classes import Protein
from Algorithms.fragmentRandomizer import fragmentRandomizer
from Algorithms.randomizer import randomizer

import matplotlib
import matplotlib.pyplot as plot

def main():

    allProteins = [['HHPHHHPH', 'A', 3], ['HHPHHHPHPHHHPH', 'B1', 5], ['HPHPPHHPHPPHPHHPPHPH', 'B2', 7], ['PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP', 'B3', 12],\
    ['HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH', 'B4', 17], ['PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP', 'C1', 12],\
    ['CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC','C2', 12], ['HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH','C3', 17],\
    ['HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH', 'C4', 17]]

    allAlgorithms = ['randomizer', 'fragment-randomizer']

    for algorithm in allAlgorithms:
        for current in allProteins:

            occurances = [0] * 100
            bestScore = 0
            worstScore = 100

            for tries in range(0, 100):

                proteinInstance = Protein(current[0])

                if algorithm == 'randomizer':
                    proteinSample = randomizer(proteinInstance, 100, '3D')
                elif algorithm == 'fragment-randomizer':
                    proteinSample = fragmentRandomizer(proteinInstance, current[2], '3D', 1)

                if proteinSample.strength > bestScore:
                    bestScore = int(proteinSample.strength)
                    bestPro = proteinSample
                elif proteinSample.strength < worstScore:
                    worstScore = int(proteinSample.strength)

                occurances[int(proteinSample.strength)] += 1

            scores = []
            for score in range(worstScore, bestScore + 1):
                scores.append(int(score))

            occurances = (occurances[worstScore:bestScore + 1])
            plot.bar(scores, occurances)
            plot.title(current[1] + ': ' + current[0])
            plot.xlabel('Scores')
            plot.ylabel('Occurances')

            myPath = os.path.dirname(os.path.abspath(__file__))
            myFile = '/Data/solution-quality/' + algorithm + '-' + current[1] + '.png'

            plot.savefig(myPath + myFile)
            plot.clf()

            print("The best folding of protein ", current[1], " had a strength of ", bestPro.strength, " and coordinates: ", bestPro.aminoCoordinates)

        print('Folded all the proteins using the', algorithm, 'algorithm.')

if __name__ == "__main__":
    main()
