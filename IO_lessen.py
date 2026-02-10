"""
Structuur van lessen-file:
leraar1/leraar2/...,vak1/vak2/...,klas1/klas2/...,aantal_uren
"""

def input_regel_naar_dict(line, id):
    line = line.split(',')
    return {'id':id,
            'leraren':line[0].split('/'),
            'vakken':line[1].split('/'),
            'klassen':line[2].split('/'),
            'uren':int(line[3]),}

def input_file_naar_lessen(src='dummy_lessen.csv'):
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
    leraren = set()
    for les in lessen:
        leraren = leraren.union(set(les[key]))
    return leraren

def koppel_lessen(lessen, *ids): # variabel aantal id's gegeven => die id's zijn niet meer nuttig maar dat moet ergens anders opgeslagen worden
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