class Protein:

    def __init__(self, proteinChain):
        # string of amino acids chars
        self.proteinChain = proteinChain

        # location coordinates and amino acid type
        self.aminoCoordinates = []
        self.strength = 0
