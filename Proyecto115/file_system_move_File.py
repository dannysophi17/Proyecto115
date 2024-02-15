import os

source = 'main.txt'

dest = 'newfile.txt'

os.rename(source, dest)

print("La ruta de origen fue renombrada a la ruta de destino exitosamente.")