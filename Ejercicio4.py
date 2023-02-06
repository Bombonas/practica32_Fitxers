import shutil
import os
path1 = os.path.join("exercicis", "Data", "operacions", "pacients.txt")
path2 = os.path.join("exercicis", "Data", "pacients_copy.txt")
shutil.copy(path1, path2)