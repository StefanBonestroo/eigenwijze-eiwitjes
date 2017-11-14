
class Protein:

    def __init__(self, proteinChain):
        # string of amino acids chars
        self.proteinChain = proteinChain

        # location coordinates and amino acid type
        self.proteinDict = {'x-cor': [], 'y-cor': [], 'type': []}
        self.strength = 0

        # initialize dictionary
        for aminoAcid in range(len(proteinChain)):
            self.proteinDict["y-cor"].append(aminoAcid)
            self.proteinDict["x-cor"].append(0)
            self.proteinDict["type"].append(proteinChain[aminoAcid])
