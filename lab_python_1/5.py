import os
import sys
def rekurencja(katalog):
    items = os.listdir(katalog)
    for index in range(len(items)):
        if os.path.isdir(katalog + items[index]):
            rekurencja(katalog + items[index])
        else:
            print(katalog +"/"+ items[index]) 

def main():
    DIR = sys.argv[1]
    rekurencja(DIR)



main()
