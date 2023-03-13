from itertools import permutations

filos = ["Arthropoda", "Chordata", "Mollusca", "Echinodermata", "Vermea", "Cnidaria",
         "Porifera", "Machina", "Angiospermas", "Gimnospermas", "Briofitas", "Basidiomycota",
         "Hidrea"]
lis = []

for loop in permutations(filos, 2):
    names = list(loop)
    names.sort()
    text = "_".join(names)
    if text not in lis:
        lis.append(text)

valids = ["Arthropoda", "Chordata", "Mollusca", "Echinodermata", "Vermea", "Cnidaria",
          "Porifera", "Machina", "Hidrea", "Quimera"]
valids.sort()
lis.sort()

print(valids)
print(lis)

animals = ['Arthropoda', 'Chordata', 'Cnidaria', 'Echinodermata', 'Hidrea', 'Machina', 'Mollusca', 'Porifera',
           'Quimera',
           'Vermea', 'Angiospermas_Arthropoda', 'Angiospermas_Basidiomycota', 'Angiospermas_Briofitas',
           'Angiospermas_Chordata',
           'Angiospermas_Cnidaria', 'Angiospermas_Echinodermata', 'Angiospermas_Gimnospermas', 'Angiospermas_Hidrea',
           'Angiospermas_Machina', 'Angiospermas_Mollusca', 'Angiospermas_Porifera', 'Angiospermas_Vermea',
           'Arthropoda_Basidiomycota',
           'Arthropoda_Briofitas', 'Arthropoda_Chordata', 'Arthropoda_Cnidaria', 'Arthropoda_Echinodermata',
           'Arthropoda_Gimnospermas',
           'Arthropoda_Hidrea', 'Arthropoda_Machina', 'Arthropoda_Mollusca', 'Arthropoda_Porifera', 'Arthropoda_Vermea',
           'Basidiomycota_Briofitas', 'Basidiomycota_Chordata', 'Basidiomycota_Cnidaria', 'Basidiomycota_Echinodermata',
           'Basidiomycota_Gimnospermas', 'Basidiomycota_Hidrea', 'Basidiomycota_Machina', 'Basidiomycota_Mollusca',
           'Basidiomycota_Porifera', 'Basidiomycota_Vermea', 'Briofitas_Chordata', 'Briofitas_Cnidaria',
           'Briofitas_Echinodermata',
           'Briofitas_Gimnospermas', 'Briofitas_Hidrea', 'Briofitas_Machina', 'Briofitas_Mollusca',
           'Briofitas_Porifera',
           'Briofitas_Vermea', 'Chordata_Cnidaria', 'Chordata_Echinodermata', 'Chordata_Gimnospermas',
           'Chordata_Hidrea',
           'Chordachona', 'Chordalluscona', 'Chordifera', 'Chordata_Vermea', 'Cnidaria_Echinodermata',
           'Cnidaria_Gimnospermas', 'Cnidaria_Hidrea', 'Cnidaria_Machina', 'Cnidaria_Mollusca', 'Cnidaria_Porifera',
           'Cnidaria_Vermea', 'Echinodermata_Gimnospermas', 'Echinodermata_Hidrea', 'Echinodermata_Machina',
           'Echinodermata_Mollusca',
           'Echinodermata_Porifera', 'Echinodermata_Vermea', 'Gimnospermas_Hidrea', 'Gimnospermas_Machina',
           'Gimnospermas_Mollusca',
           'Gimnospermas_Porifera', 'Gimnospermas_Vermea', 'Hidrachena', 'Hidrolusca', 'Hidrea_Poridrea',
           'Hidrea_Vermea',
           'Molluschona', 'Porichena', 'Vermachena', 'Molluspora', 'Mollusermea',
           'Porifermea']
