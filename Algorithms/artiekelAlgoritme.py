from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding

# DONE # Maak een eiwit in de structuur --> [[x,y,z,strength,position],[x,y,z,strength,position]]

def fragmentFinal(Protein, tries, dimension):
    length = len(Protein.proteinChain)
    lengthPc = (length - 1)
    dataStructure = []
    for amount in range(length):
        dataStructure.append([0,0,0,0,amount])

# Soort van DONE
    # Pak van de proteinChain fragements elke |strength > 0| tot de volgende |strength > 0| als de length
    # van de fragment groter is als 4 continue naar de if loops. (ook position 0 tot tot eerste position met |strength >0|(selfde voor het einde))

    fragements = []
    start = [0]
    for aminozuur in dataStructure:
        if aminozuur[3] > 0:
            start.append(aminozuur[3])
            fragments.append(start)
            start = [aminozuur[3]]
    if dataStructure[lengthPc] == 0:
        start.append(lengthPc)
        fragments.append(start)

            # alles hieronder opslaan in de eiwitstructuur boven aangegeven.
            # de fragmets die worden doorgegeven in de ifstatements zetten als: [position, position]
    for fragment in fragments:
        fragmentLength = (fragment[1] - fragment[0])
# Maak 3 if statements:
#if start position == 0
    # maak een functie die vanaf het einde van het fragment naar 0 toe fouwt (omgekeerde van randomizer (die werkt van begin tot einde))
        if fragment[0] == 0:
            for nieuweFouwing in range(fragmentLength):
                currentCoor = dataStructure[fragmentLength - nieuweFouwing][0:3]
                existingCoors = dataStructure[(fragmentlength - nieuweFouwing):length][0:3]

                possibilities = possibilityCheck(1, currentCoor)

                direction = validityCheck(possibilities, existingCoors)

                dataStructure[fragmentlength - nieuweFouwing - 1][0] = direction[0]
                dataStructure[fragmentlength - nieuweFouwing - 1][1] = direction[1]
                dataStructure[fragmentlength - nieuweFouwing - 1][2] = direction[2]
#elif start position != 0 and end position != len(chain)
    # gebruik de door Yente gemaakte functie om een nieuw path te creeren
        elif fragment[0] != 0 and fragmet[1] != lengthPc and fragmentLength > 2:
            shifts = []
            for amino in range(fragment[0] + 1, fragmet[1]):
                # Append the shift in coordinates
                shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
                origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1],
                origPro.aminoCoordinates[amino + 1][2] - origPro.aminoCoordinates[amino][2]))
#elif end position == len(chain)
    # maak fucntie zoals randomizer die doorfouwt
        elif fragment[1] == lengthPc:
            for nieuweFouwing in range(fragment[0],lengthPc):
                currentCoor = dataStructure[nieuweFouwing][0:3]
                existingCoors = dataStructure[0:nieuweFouwing][0:3]

                possibilities = possibilityCheck(1, currentCoor)

                direction = validityCheck(possibilities, existingCoors)

                dataStructure[nieuweFouwing + 1][0] = direction[0]
                dataStructure[nieuweFouwing + 1][1] = direction[1]
                dataStructure[nieuweFouwing + 1][2] = direction[2]

# Beste resultaat opslaan

# Afhankelijk van de hitte x aantal strength naar 0 zetten (hoe meer strength naar 0 word gezet destemeer het eiwit word veranderd).
