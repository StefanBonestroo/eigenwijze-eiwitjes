# Protein Power

Dit, in python geschreven, programma probeert een oplossing te vinden voor het zogenaamde 'Hydrophobic-polar Protein Folding'-probleem. Dit probleem kan als volgt beschreven worden: We hebben een eiwit hebben bestaande uit H en P aminozuren - weer te geven als bijv. "HHHPHHPHP" - en wij moeten deze vouwen, enkel gebruikmakende van hoeken van 90 graden, zonder aminozuren te doen laten overlappen of breken. Een vouwing wordt beter naarmate er H'tjes naast elkaar liggen, waar de covalente verbindingen tussen H'tjes niet meetellen. Een H-bond tussen 2 H'tjes zorgt namelijk voor een meer stabiele energietoestand. Wat is de beste manier om een eiwit te vouwen?

## Main.py

Deze main functie vereist een string met H'tjes en P'tjes en returned een object met de classe 'Protein', welk bevat: de input string, een gevouwen eiwit in de vorm van een lijst met coordinaten (2D of 3D), en de score die deze vouwing produceert. 
Daarnaast wordt de gebruiker gepresenteerd met een grafiek die deze vouwing visualiseert. Tenslotte wordt de gebruiker gepresenteerd met een grafiek die de gevonden scores plot tegen de tijd van het runnen van Main.py, en visualiseert hiermee de snelheid waarmee de vouwing verbeterd werd.

## functions.py

Dit bestand bevat 2 veelgebruikte functies:

### calculateFolding
Deze functie berekent de sterkte van een gevouwen eiwit. Als input moet een lijst coordinaten en een string H'tjes en P'tjes (van dezelfde lengte) mee worden gegeven. Als output geeft deze functie de sterkte in 'aantal H-bonds'.

### visualizeFolding
Deze functie maakt voor zowel 2D als 3D structuren een overzichtelijke figuur waar de vouwing en sterkte uit kan worden afgeleid. Als input moet een 'Protein' object worden meegegeven. De functie geeft geen output, maar laat wel een figuur zien aan de gebruiker.

## classes

Dit bestand defineert de klasse 'Protein'.

## mainProgress & fragmentMain

Deze varianten op Main.py zijn een 'work in progress'.

