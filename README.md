# Protein Power

![alt-text](https://github.com/StefanBonestroo/eigenwijze-eiwitjes/blob/master/Miscellaneous/Logo.png)

Dit, in python geschreven, programma probeert een oplossing te vinden voor het zogenaamde 'Hydrophobic-polar Protein Folding'-probleem. Dit probleem kan als volgt beschreven worden: We hebben een eiwit hebben bestaande uit H en P aminozuren - weer te geven als bijv. "HHHPHHPHP" - en wij moeten deze vouwen, enkel gebruikmakende van hoeken van 90 graden, zonder aminozuren te doen laten overlappen of breken. Een vouwing wordt beter naarmate er H'tjes naast elkaar liggen, waar de covalente verbindingen tussen H'tjes niet meetellen. Een H-bond tussen 2 H'tjes zorgt namelijk voor een meer stabiele energietoestand. Wat is de beste manier om een eiwit te vouwen?

## Voorbereidingen

Na het volgen van deze instructies zou het programma goed 'runnable' moeten zijn in de terminal van je computer.


### Randvoorwaarden

Er zijn wat tools nodig om dit programma effectief te kunnen runnen.

#### Matplotlib
Dit package verzorgd het visualisatie onderdeel van 'Protein Power'. Deze kan op de volgende manier geinstalleerd worden:
```
python3 -mpip install matplotlib
```
Maar, er zijn ook andere manieren om deze package te installeren. De details voor deze installaties vind je [hier](https://matplotlib.org/faq/installing_faq.html).

Na installatie run je deze python code om te kijken of de installatie gelukt is:
```
>>> import matplotlib
>>> matplotlib.__version__
'2.1.0'
```
Mocht de installatie niet succesvol zijn geweest, dan kan de [Matplotlib documentatie](https://matplotlib.org/faq/troubleshooting_faq.html) je vaak verder helpen.

### Het programma zelf

Het programma kan in de terminal gerund worden en vereist verder geen installaties.

## Vouw je eiwit

Nadat alle bestanden op je computer aanwezig zijn, kun je beginnen met het vouwen van je eerste eiwit.

### Gebruik

Wanneer enkel ``` python3 Main.py ``` gerund wordt, zal het programma je vertellen hoe je het programma moet gebruiken en welke argumenten je daarmee kan (en mag) meegeven:
```
Usage: 

 Argument 1: protein string to be folded, e.a. "HHPHPHP"
 Argument 2: desired algorithm -> 'randomizer', 'depth-first', 'fragment-randomizer'
 Argument 3: desired folding dimensions -> '2D' or '3D'
 Argument 4: *optional argument 'tries' for 'randomizer' and 'fragment-randomizer'
 Argument 5: *optional argument 'fragmentLength' for 'fragment-randomizer'
```

### De resultaten

Nadat het door jou gekozen algoritme gerund heeft, zal het programma je een visualisatie van de gevonden resultaten geven. Aangezien de resultaten opgeslagen worden in je 'Protein' klasse, kun je elke gewenst stuk code voor verdere bewerking aan het einde van Main.py toevoegen, om daarin deze aan te roepen.

## Gebruikte software

* [Atom](https://atom.io/), hier is alle code in geschreven

## Auteurs

* **Yente Stor** - [YenteStor](https://github.com/YenteStor)
* **Jesse Groot** - [JesseGroot](https://github.com/jessegroot)
* **Stefan Bonestroo** - [StefanBonestroo](https://github.com/StefanBonestroo)

## Erkenningen

* Wietze Slagman - *Voor de inzichten, tips, en begeleiding* - [Wietze](https://github.com/WietzeSlagman)
* Het README.md template van [Purplebooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
