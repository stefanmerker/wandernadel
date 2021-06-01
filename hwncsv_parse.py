import csv
import math

with open ('HWN_2020_05_01.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    anzahl = 222;
    koordinaten = [[0 for x in range(2)] for y in range(anzahl)]

    i=0
    for line in csv_reader:
        hwn = {"stempel":line['Stempel'], "ort":line['Ort'], "e":line['GPS'][11:19], "n":line['GPS'][1:9]}
        #print(hwn)
        koordinaten[i][0]=line['GPS'][11:19]
        koordinaten[i][1]=line['GPS'][1:9]
        i += 1
    #print(koordinaten)

    anzahl = 222;
    distanzen = [[0 for x in range(anzahl)] for y in range(anzahl)]

    file = open('distanzen.txt', 'w')

    i=0
    while i < anzahl:
        j=0
        while j < anzahl:
            distanzen[i][j] = math.sqrt((float(koordinaten[i][0])-float(koordinaten[j][0]))**2+(float(koordinaten[i][1])-float(koordinaten[j][1]))**2)
            file.write(str(distanzen[i][j]))
            file.write(',')
            j += 1
        file.write('\n')
        i += 1
