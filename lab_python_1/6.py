import os
import sys

plik_jpg = sys.argv[1]
plik_png = plik_jpg[:-3]+"png"
os.system("mv " +  plik_jpg + " " +  plik_png)
