from IO_lessen import *

def gewicht_functie(lessen, les):
    """De functie die een gewicht berekent op basis van de andere lessen"""
    return les['uren'] + 3*len(les['klassen']) - 100_000_000*int(les['uren']==0)

def gewichten(lessen):
    """Voegt een 'gewicht'-parameter toe aan elke les of past die aan om te kunnen sorteren"""
    for les in lessen:
        les['gewicht'] = gewicht_functie(lessen, les)

def maak_blok(lessen):
    pass

if __name__=='__main__':
    dummy = input_file_naar_lessen()
    koppel_lessen(dummy, 33, 99)
    dummy = filter_lessen(dummy)
    print_lessen(dummy)
    gewichten(dummy)
    print_lessen(dummy)