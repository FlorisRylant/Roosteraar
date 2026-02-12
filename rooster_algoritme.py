from IO_lessen import *

def gewicht_functie(lessen, les):
    """De functie die een gewicht berekent op basis van de andere lessen"""
    leraar_uren = []
    for leraar in les['leraren']:
        leraar_uren.append(0)
        for l in lessen:
            if leraar in l['leraren']: leraar_uren[-1] += l['uren']
    return les['uren'] + 30*len(les['klassen']) + max(leraar_uren)

def update_gewichten(lessen):
    """Voegt een 'gewicht'-parameter toe aan elke les of past die aan om te kunnen sorteren"""
    for les in lessen:
        les['gewicht'] = gewicht_functie(lessen, les)

def les_mogelijk(les, leraren_beschikbaar, klassen_beschikbaar):
    """Kijkt of alle leraren en klassen nog beschikbaar zijn en of die les nog uren heeft"""
    if not set(les['klassen']).issubset(klassen_beschikbaar): return False
    if not set(les['leraren']).issubset(leraren_beschikbaar): return False
    if les['uren']==0: return False
    return True

def maak_blok(lessen):
    """Maakt een lesblok door de lessen te rangschikken volgens gewicht en steeds de zwaarst mogelijke lessen in te plannen"""
    leraren_beschikbaar = set_van_lessen(lessen, 'leraren')
    klassen_beschikbaar = set_van_lessen(lessen, 'klassen')
    selectie = set()
    while len(klassen_beschikbaar)!=0:
        update_gewichten(lessen)
        lessen = sorted(lessen, key=lambda x:x['gewicht'], reverse=True)
        index = 0
        while not les_mogelijk(lessen[index], leraren_beschikbaar, klassen_beschikbaar):
            index += 1
            if index >= len(lessen): raise KeyError('lessenpoging mislukt')
        selectie.add(lessen[index]['id'])
        for leraar in lessen[index]['leraren']: leraren_beschikbaar.remove(leraar)
        for klas in lessen[index]['klassen']: klassen_beschikbaar.remove(klas)
        lessen[index]['uren'] -= 1
        print(lessen[index])
    return selectie

def maak_rooster(lessen):
    """Maakt 32 blokken"""
    rooster = []
    for i in range(32):
        rooster.append(maak_blok(lessen))
        print(f'Les {i}: {rooster[-1]}')
    return rooster

if __name__=='__main__':
    dummy = input_file_naar_lessen()
    koppel_lessen(dummy, 33, 99)
    dummy = filter_lessen(dummy)
    print_lessen(dummy)
    update_gewichten(dummy)
    rooster = maak_rooster(dummy)
    print(rooster)
    lessen_naar_file(rooster)