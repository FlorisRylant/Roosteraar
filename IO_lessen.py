"""
Structuur van lessen-file:

"""

def input_regel_naar_dict(line, id):
    """
    Maakt van een regel van de structuur
        leraar1/leraar2/...,vak1/vak2/...,klas1/klas2/...,aantal_uren
    een dictionary met daarin de id (nutteloos?) en alle andere logische info
    """
    line = line.split(',')
    return {'id':id,
            'leraren':line[0].split('/'),
            'vakken':line[1].split('/'),
            'klassen':line[2].split('/'),
            'uren':int(line[3]),}

def input_file_naar_lessen(src='dummy_lessen.csv'):
    """Maakt van het bestand met inputlessen een lijst met dictionaries"""
    out = []
    with open(src) as file:
        for i, line in enumerate(file.readlines()):
            if line.count(',') != 3: continue
            out.append(input_regel_naar_dict(line.strip(), i))
    return out

def print_lessen(lessen):
    for les in lessen:
        print(les)

def set_van_lessen(lessen, key):
    """Vraagt een set op met alles dat voorkomt in een categorie (alle leraren / vakken / klassen)"""
    leraren = set()
    for les in lessen:
        leraren = leraren.union(set(les[key]))
    return leraren

def koppel_lessen(lessen, *ids): # variabel aantal id's gegeven => die id's zijn niet meer nuttig maar dat moet ergens anders opgeslagen worden
    """
    Koppelt twee of meer lessen aan elkaar:
    -> nieuwe les: combinatie van de leraren, klassen en vakken
    -> bron: id's die samengevoegd zijn
    geeft een ValueError als de lessen niet evenveel uren zijn
    
    Gebruik: heel multi-inzetbaar:
    - twee lessen samenvoegen: bv dezelfde les maar in twee talen, die tellen dan als één blok
    - meerdere lessen samen: keuzevak (alle leerkrachten, groepen en vakken zitten samen dan)
    -> als er een discrepantie is in het aantal uren (bv 2uGrieks => 1uAV + 1uMEAV) de les grieks opsplitsen in 2 en zo combineren
        * nog een extra functie maken om lessen te splitsen, en dan een overkoepelend systeem *
    - vakken die om de zoveel tijd wisselen (bv MEAV of stage-inhaallessen) samenvoegen
        * als het permuteerbare vakken zijn moeten alle klassen samen (zoals MEAV) voor efficiëntie *
    """
    nieuw = {'id':len(lessen), 'leraren':[], 'vakken':[], 'klassen':[], 'bron':ids}
    for id in ids:
        les = lessen[id]
        for leraar in les['leraren']:
            if leraar not in nieuw['leraren']: nieuw['leraren'].append(leraar)
        for vak in les['vakken']:
            if vak not in nieuw['vakken']: nieuw['vakken'].append(vak)
        for klas in les['klassen']:
            if klas not in nieuw['klassen']: nieuw['klassen'].append(klas)
        if nieuw.get('uren', les['uren']) != les['uren']: raise ValueError('Niet evenveel uren in elke les')
        nieuw['uren'] = les['uren']
    lessen.append(nieuw)

def ontkoppel_rooster(rooster_file, lessen):
    """
    Zorgt dat in een rooster de samengesmolten lessen terug in hun componenten gesplitst worden (optioneel) in het bestand
    """
    with open(rooster_file) as file:
        blokken = file.readlines()
    with open(rooster_file, 'w') as file:
        for blok in blokken:
            regel = ''
            for les in blok.strip().split(','):
                if 'bron' in lessen[int(les)].keys(): regel += ','.join(lessen[int[les]])
                else: regel += les
                regel += ','
            file.write(regel[:-1]+'\n')


if __name__=='__main__':
    testlessen = input_file_naar_lessen()
    print_lessen(testlessen)
    print(set_van_lessen(testlessen, 'leraren'))
    koppel_lessen(testlessen, 33, 99)
    print_lessen(testlessen)