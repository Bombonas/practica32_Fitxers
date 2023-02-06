import os
path1 = os.path.join(".", "exercicis", "Data", "operacions", "pacients.txt")
pacient= {'nom': 'Pep', 'edat': 42, 'Diabetic': True}

txt = pacient["nom"] + "\t" + str(pacient["edat"]) + "\t"
if pacient["Diabetic"]:
    txt += "Si"
else:
    txt += "No"

f = open("pacients.txt", "w")
f.write(txt)
f.close()
