import os

from classes import Protein
from Algorithms.fragmentRandomizer import fragmentRandomizer
from Algorithms.randomizer import randomizer

import matplotlib
import matplotlib.pyplot as plot

def main():

    allProteins = ['HHPHHHPHPHHHPH','HPHPPHHPHPPHPHHPPHPH','PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP',\
    'HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH','PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP',\
    'CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC','HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH',\
    'HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH']

    allAlgorithms = ['randomizer', 'fragment-randomizer']

    for algorithm in allAlgorithms:
        for current in allProteins:

            occurances = [0] * 100
            bestScore = 0
            worstScore = 100


            for tries in range(0,100):

                proteinInstance = Protein(current)

                if algorithm == 'randomizer':
                    proteinSample = randomizer(proteinInstance, 50, '3D')
                elif algorithm == 'fragment-randomizer':
                    proteinSample = fragmentRandomizer(proteinInstance, 6, '3D', 1)

                if proteinSample.strength > bestScore:
                    bestScore = int(proteinSample.strength)
                elif proteinSample.strength < worstScore:
                    worstScore = int(proteinSample.strength)

                occurances[int(proteinSample.strength)] += 1

            scores = []
            for score in range(worstScore, bestScore):
                scores.append(int(score))

            occurances = (occurances[worstScore:bestScore])
            plot.bar(scores, occurances)
            plot.title(current)
            plot.xlabel('Scores')
            plot.ylabel('Occurances')

            myPath = os.path.dirname(os.path.abspath(__file__))
            myFile = '/Data/solution-quality/' + algorithm + '-' + current + '.png'

            plot.savefig(myPath + myFile)
            plot.clf()

        print('Folded all the proteins using the', algorithm, 'algorithm.')

if __name__ == "__main__":
    main()
