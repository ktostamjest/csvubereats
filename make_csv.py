# /usr/bin/python

import csv

import sqlite3

file = open("b828d4bc-282c-4d0c-e5a7-bb1d03753199.csv")
sql_file = open("zapytaniesql")
dupa = sql_file.read()
print(type(dupa))
filereader = csv.reader(file)
exampleData = list(filereader)
kierowcy = {"Adam Pasierowski": "500842221", "Ahmet Uzan": "880004263",
            "Piotr Dobrasiak": "536723523", "jakub lotycz": "795803514"}
dupa = dupa.replace("nazwa_kierowcy", kierowcy["jakub lotycz"])

conn = sqlite3.connect('kierowcy.db')
c = conn.cursor()
conn.execute(dupa)

print (dupa)
ilosc_elementow = len(exampleData)
i = 0
print (exampleData[4])
suma_zarobkow = 0
dochod = 0
brutto = 0

print (ilosc_elementow)

while (i < ilosc_elementow):
    if (exampleData[i][1] == kierowcy["jakub lotycz"]):
        j = i
        j = str(j)
        print ("DUPA " + j)
        if exampleData[i][14]:  # sprawdza pusty string
            suma_zarobkow = suma_zarobkow + float(exampleData[i][14])
        if exampleData[i][16]:  # sprawdza pusty string
            dochod = dochod + float(exampleData[i][16])
        if exampleData[i][7]:  # sprawdza pusty string
            brutto = brutto + float(exampleData[i][7])
    i = i+1
zarobek = brutto - suma_zarobkow
print (suma_zarobkow, dochod, brutto, zarobek)

# Tworzenie arkusza kalkulacyjnego #

#from openpyxl import load_workbook
#wb = load_workbook(filename = 'rozliczenia.xlsx')
#sheet_ranges = wb['Arkusz1']
#print(sheet_ranges['E2'].value)

print ("Tak, udalos sie!")


'''
class Kierowca:    
    """Documentation for Kierowca

    """
    numer_telefonu = ""
    def __init__(self, args):
        self.numer_telefonu = args
'''
