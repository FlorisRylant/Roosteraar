# Roosteraar
Doel van de software: betere lessenroosters kunnen maken dan Untis (geen rekening houdend met lokalen, eventueel later)

# Methode
Deel 1: een werkend lessenrooster maken (moeilijkste deel)

Preprocessor:
- alle lessen worden eringezet vanuit de "opdrachten" van de leerkrachten
- zo veel mogelijk systemen om lessen te koppelen tot één "les" in het programma:
  - keuzevakken: wordt één les met alle keuzeleerkrachten en alle groepen die kunnen kiezen
  - vakken over meerdere jaren: klasgroepen in de les samenvoegen tot één les
  - vakken met meerdere leraren: zoals keuzevakken maar dan gewoon één lokaal
  - vakken die om de zoveel tijd afwisselen van leraar / les (bv MEAV of uren om stage in te halen): zoals vak met meerdere leraren aangezien die allemaal vrij moeten zijn
  - > als meerdere klassen dit type les hebben en een permutatie is mogelijk: samenvoegen tot één "keuzevak" (waar de leerlingen dan geen keuze hebben)
  - CLIL: keuzevak tussen "normaal" en "andere taal"
  - ...

Algoritmes mogelijk (voorlopig onbekend of ze werken):
- alle lessen een "gewicht" toekennen en dan steeds de lessen met het hoogste gewicht eerst inplannen -> heel snel aanpasbaar en heel algemeen maar moeilijk om te perfectioneren
- gewoon proberen tot het lukt -> kleine slaagkans maar extreem simpel
- heilige graal moet nog gevonden worden

Deel 2: lessen rangschikken voor pretmaximalisatie
- elk lesblok een "pretscore" geven en dan rangschikken voor maximale pret
- > zoveel mogelijk QOL-toevoegingen implementeren:
  - voor elk vak moet je kunnen bepalen hoe leuk het is om elke les te hebben, algemener: per dag (lessen gelijk) of uur (dagen gelijk) of voor elk vak met die naam (vak gelijk)
  - lescombinaties van twee uur punten geven (- of +), algemener: kunnen instellen of lessen in een blok van twee uur moeten (zoals LO)
  - voor leerkrachten apart een lessenrooster kunnen inkleuren met hoe graag ze uren willen van graag tot onmogelijk
  - kunnen instellen hoe leuk een aantal keer één vak op een dag is (om te voorkomen dat maandag 5u wiskunde is bv)
  - eventueel: systeem om aan elk vak een "gewicht" te geven (mentale moeite) en dan een grafiek tekenen door de week van de ideale mentale moeite op een dag / uur / ...
