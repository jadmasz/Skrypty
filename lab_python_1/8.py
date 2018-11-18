import copy
import random
# generowanie losowych liczb
y = []
for x in range(0,50):
    liczba = random.randint(0,1000)
    y.append(liczba)
lista=copy.copy(y)
print(lista)

#Quicksort
def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]     
 
    for j in range(low , high):
        if   arr[j] >= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#sortowanie za pomoca stworzonej funkcji
print("Sortowanie za pomoca stworzonej funkcji:")
n=len(lista)
quickSort(lista,0,n-1)
print(lista)

#sortowanie za pomoca gotowej funkcji
print("Sortowanie za pomoca gotowej funkcji:")
y.sort(reverse=True)
print(y)
