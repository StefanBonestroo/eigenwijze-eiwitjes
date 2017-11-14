class Protein:

    def __init__(self, proteinChain):
        # string of amino acids chars
        self.proteinChain = proteinChain

        # location coordinates and amino acid type
        self.aminoCoordinates = [(0,0),(0,1)]
        self.strength = 0
