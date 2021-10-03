import csv

with open('materials.csv') as fm:
    myreader=csv.DictReader(fm)
    print(myreader.fieldnames)
    for row in myreader:
        print('Das Material {} hat das E-Modul E={} N/mm2.'.format(row['Name'],row['E-Modul (N/mm2)']))