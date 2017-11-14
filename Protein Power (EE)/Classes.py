# A class to store a proteinchain in with types of amino acids, coordinates of
# folded protein chain and the strength of this folding
class Protein:

    def __init__(self, proteinChain):
        # string of amino acids chars
        self.proteinChain = proteinChain

        # location coordinates and amino acid type
        self.proteinDict = {'x-cor': [], 'y-cor': []}
        self.strength = 0

        # initialize dictionary
        for aminoAcid in range(len(proteinChain)):
            self.proteinDict["y-cor"].append(aminoAcid)
            self.proteinDict["x-cor"].append(0)
            self.proteinDict["type"].append(proteinChain[aminoAcid])
