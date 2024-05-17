arr = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort(arr):
    
    n = len(arr)     # ploppar in längden på arr i en ny variabel
   
    
    for i in range(n-1):    # Kollar värdet på n, om det är 1 räknas den redan som sorterad.

        swapped = False
        for j in range(0, n-i-1):    # Kollar igenom alla element och byter plats om nästa element är större
           
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:     
            return
        
        
    
bubbleSort(arr)
if __name__ == '__main__':
    print('Bubblesorterad lista är:')
    for i in range(len(arr)):
         print('% d' % arr[i], end='')
    
    

    
def merge(arr1,arr2):  
    """ 
    Tar två listor 'arr1' och 'arr2' som parametrar och slår ihop dem. Det skapas en tom lista: 'resultat'.
    Den första while-loopen fortsätter att jämföra elementen i de två listorna tills båda listorna är 
    tomma och fyller på 'resultat' med elementen i stigande ordning.
    De två sista while-looparna är till för att iterera över elementen i 'arr1' och 'arr2' och lägga till dem i 'resultat'
    x och y används som räknare for att hålla koll på positionerna i 'arr1' och 'arr2'
    
    """
    x = 0                               
    y = 0
    resultat = []
    
    while (x < len(arr1)) and y < len(arr2):
        if arr2[y] > arr1[x]:
            resultat.append(arr1[x])
            x += 1
        else:
            resultat.append(arr2[y])
            y += 1

    while (x < len(arr1)):
        resultat.append(arr1[x])
        x += 1
    
    while (y < len(arr2)):
        resultat.append(arr2[y])
        y += 1
    
 
    return resultat



def mergeSort(arr):
    """
    Delar upp listan i 'left' och 'right' och kallar på merge-funktionen för att sammanfoga de sorterade delarna.
    Den slutgiltiga sorterade listan returneras när alla rekursiva anrop gjort sitt.
    """
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left,right)


  
if __name__ == '__main__':
  # arr = [64, 34, 25, 12, 22, 11, 90]
    arr = mergeSort(arr)
    print('\nMergesorterad lista är:')
    print(*arr)