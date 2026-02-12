from IO_lessen import *

def gewicht_functie(lessen, les, j):
    """De functie die een gewicht berekent op basis van de andere lessen"""
    leraar_uren = []
    for leraar in les['leraren']:
        leraar_uren.append(0)
        for l in lessen:
            if leraar in l['leraren']: leraar_uren[-1] += l['uren']
    return les['uren'] + 30*len(les['klassen']) + max(leraar_uren)

def gewicht_functie2(lessen, les, j):
    """De functie die een gewicht berekent op basis van de andere lessen"""
    if les['uren'] == 0: return 0
    leraar_uren = []
    for leraar in les['leraren']:
        leraar_uren.append(0)
        for l in lessen:
            if leraar in l['leraren']: leraar_uren[-1] += l['uren']
    gewicht = les['uren']
    gewicht += 10*len(les['klassen'])
    gewicht += 20*len(les['leraren'])
    uren_over = 32-j-max(leraar_uren)
    if uren_over < 0: raise KeyError('te weinig lessen om nog te kunnen slagen')
    elif uren_over == 0: gewicht += 3_000
    elif uren_over == 1: gewicht += 2_000
    elif uren_over < 4: gewicht += 1_000
    return gewicht
        

def update_gewichten(lessen, j):
    """Voegt een 'gewicht'-parameter toe aan elke les of past die aan om te kunnen sorteren"""
    for les in lessen:
        les['gewicht'] = gewicht_functie(lessen, les, j)

def les_mogelijk(les, leraren_beschikbaar, klassen_beschikbaar):
    """Kijkt of alle leraren en klassen nog beschikbaar zijn en of die les nog uren heeft"""
    if not set(les['klassen']).issubset(klassen_beschikbaar): return False
    if not set(les['leraren']).issubset(leraren_beschikbaar): return False
    if les['uren']==0: return False
    return True

def maak_blok(lessen, j=0):
    """Maakt een lesblok door de lessen te rangschikken volgens gewicht en steeds de zwaarst mogelijke lessen in te plannen"""
    leraren_beschikbaar = set_van_lessen(lessen, 'leraren')
    klassen_beschikbaar = set_van_lessen(lessen, 'klassen')
    selectie = set()
    while len(klassen_beschikbaar)!=0:
        update_gewichten(lessen, j)
        lessen = sorted(lessen, key=lambda x:x['gewicht'], reverse=True)
        index = 0
        while not les_mogelijk(lessen[index], leraren_beschikbaar, klassen_beschikbaar):
            index += 1
            if index >= len(lessen): raise KeyError('lessenpoging mislukt')
        selectie.add(lessen[index]['id'])
        for leraar in lessen[index]['leraren']: leraren_beschikbaar.remove(leraar)
        for klas in lessen[index]['klassen']: klassen_beschikbaar.remove(klas)
        lessen[index]['uren'] -= 1
    return selectie

def maak_rooster(lessen):
    """Maakt 32 blokken"""
    rooster = []
    for i in range(32):
        rooster.append(maak_blok(lessen, i))
        print(f'Les {i}: {rooster[-1]}')
    return rooster

if __name__=='__main__':
    dummy = filter_jaren(input_file_naar_lessen('dummy_totaal.csv'), '123456')
    print_lessen(dummy)
    rooster = maak_rooster(dummy)
    print(rooster)
    lessen_naar_file(rooster)