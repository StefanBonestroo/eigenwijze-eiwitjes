from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding

from Algorithms.randomizer import randomizer #niet nodig als af.

# Maak een eiwit in de structuur --> [[x,y,z,strength,position],[x,y,z,strength,position]]

# Pak van de proteinChain fragements elke |strength > 0| tot de volgende |strength > 0| als de length
# van de fragment groter is als 4 continue naar de if loops. (ook position 0 tot tot eerste position met |strength >0|(selfde voor het einde))

        # alles hieronder opslaan in de eiwitstructuur boven aangegeven.
        # de fragmets die worden doorgegeven in de ifstatements zetten als: [position, position]

# Maak 3 if statements:
#if start position == 0
    # maak een functie die vanaf het einde van het fragment naar 0 toe fouwt (omgekeerde van randomizer (die werkt van begin tot einde))

#elif start position != 0 and end position != len(chain)
    # gebruik de door Yente gemaakte functie om een nieuw path te creeren

#elif end position == len(chain)
    # maak fucntie zoals randomizer die doorfouwt

# Beste resultaat opslaan

# Afhankelijk van de hitte x aantal strength naar 0 zetten (hoe meer strength naar 0 word gezet destemeer het eiwit word veranderd).
