
class Protein:

    def __init__(self, proteinChain, loops):

        # slaat de waardes op die belangrijk zijn voor het programma
        self.proteinChain = proteinChain
        self.proteinDict = {'x-cor': [], 'y-cor': [], 'type': []}
        self.tries = loops
        self.exist = [(0, 0), (0, 1)]

        # de waardes die aan het einde van het programma belangrijk zijn
        self.bestProteinDict = None
        self.strength = 0

        # maakt de dictionary aan met de benodigde lengte
        for round in range(len(proteinChain)):
            if round == 1:
                self.proteinDict["y-cor"].append(1)
            else:
                self.proteinDict["y-cor"].append(0)
            self.proteinDict["x-cor"].append(0)
            self.proteinDict["type"].append(proteinChain[round])

        self.makeChainStructure(self.proteinDict, len(proteinChain))
