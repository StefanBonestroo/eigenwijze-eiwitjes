class Protein:

    def __init__(self, proteinChain):

        self.proteinChain = proteinChain

    def makeChainStructure(self, amino_zuur, counter):

        if counter >= len(self.proteinChain):
            return

        amino_zuur.left = Amino(counter)
        counter +=1
        makeChainStructure(amino_zuur.left, counter)

    def calculateFolding (self):
        print 'function is empty'

    def visualizeFolding (self):
        print 'function is empty'

class Amino:
    def __init__(self, position):
        self.position = position
        upper = None
        right = None
        lower = None
        left = None

def main():

    protie = Protein("PPHHHPHHHPH")

    counter = 0
    first_amino = Amino(counter)
    counter = 1

    protie.makeChainStructure(first_amino, counter)
    #protie.culculateFolding
if __name__=='__main__':
    main()
