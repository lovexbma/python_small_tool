import csv

csvfile = 'e:/FlowerDoc/Public/master/master_character_skills.csv'

with open(csvfile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:

        strRow = ', '.join(row)
        arrRow = strRow.split(',')
        print arrRow[0]
