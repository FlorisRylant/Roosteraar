def convert(src_lessen, src_rooster, dest):
    l_oud = open(src_lessen)
    r_oud = open(src_rooster)
    nieuw = open(dest, 'w')

    oud_rooster = ','+r_oud.read().replace('\n', ',')+','
    for les in l_oud.readlines():
        les = les.strip().split(',', 4)
        nieuw.write(f"{les[1]},{les[2]},{les[4].replace(',', '/')},{oud_rooster.count(f',{les[0]},')}\n")

    l_oud.close()
    r_oud.close()
    nieuw.close()

convert('dummy_lessen_oud.csv', 'dummy_uren.csv', 'dummy_derde.csv')