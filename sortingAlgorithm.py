import time     
from randomlist import generate_random_list   
from fire import print_fire       # Import av moduler och egna funktioner



def bubbleSort(random_list):

    n = len(random_list)    # ploppar in längden på random_list i en ny variabel
    
    for i in range(n-1):    # Kollar igenom alla element och byter plats om nästa element är större
                            # Om inget bytt plats är listan redan sorterad och loopen bryts
        swapped = False
        for j in range(0, n-i-1):   
            if random_list[j] > random_list[j + 1]:
                swapped = True
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]

        if not swapped: 
            break
        
    
    
def merge(arr1, arr2):
    """ 
    Tar två listor 'arr1' och 'arr2' som parametrar och slår ihop dem. Det skapas en tom lista: 'resultat'.
    Den första while-loopen fortsätter att jämföra elementen i de två listorna tills båda listorna är 
    tomma och fyller på 'resultat' med elementen i stigande ordning.
    De två sista while-looparna är till för att iterera över elementen i 'arr1' och 'arr2' och lägga till dem i 'resultat'
    x och y används som räknare for att hålla koll på positionerna i 'arr1' och 'arr2'.
    
    """
    i = 0                               
    j = 0
    result = []

    while (i < len(arr1)) and j < len(arr2):
        if arr2[j] > arr1[i]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while (i < len(arr1)):
        result.append(arr1[i])
        i += 1
    
    while (j < len(arr2)):
        result.append(arr2[j])
        j += 1
    
    return result
    

def mergeSort(random_list):
    """
    Delar upp listan i 'left' och 'right' och kallar på merge-funktionen för att sammanfoga de sorterade delarna i 'mid'.
    Den slutgiltiga sorterade listan returneras när alla rekursiva anrop gjort sitt.
    """
    if len(random_list) <= 1:
        return random_list
    mid = len(random_list) // 2
    left = mergeSort(random_list[:mid])
    right = mergeSort(random_list[mid:])

    return merge(left, right)


        
if __name__ == '__main__':  # Kod som kör hela programmet
    while True:
        try:
  
            length = int(input("Ange längden på listan: "))
            min_value = int(input("Ange det minsta värdet: "))
            max_value = int(input("Ange det största värdet: "))
            
      

            random_list = generate_random_list(length, min_value, max_value)     # längd, minsta värdet, största värdet
    
            print('\nOsorterad lista är:')
            print(*random_list)
    
            start_time_bubble = time.time()   # Startar tidtagning för bubblesort
            bubbleSort(random_list)
            end_time_bubble = time.time()   # Stoppar tidtagning för bubblesort
            print('\nBubblesorterad lista är:')
            print(*random_list)

            start_time_merge = time.time()  # Startar tidtagning för mergesort
            mergeSort(random_list)
            end_time_merge = time.time()  # Stoppar tidtagning för mergesort
            print('\nMergesorterad lista är:')
            print(*random_list)
    
            print(f"Bubblesort tog {end_time_bubble - start_time_bubble:.5f} sekunder")
            print(f"Mergesort tog {end_time_merge - start_time_merge:.5f} sekunder")
    
            if len(random_list) >= 10000:   # Om längdena på listan är 10 000 eller större börjar det brinna
                print_fire()
                print('Det blev för många element, din processor exploderade och alla proven brann upp. Sigge sends his regards. :-)')
            else:
                pass
         
        except ValueError:
            print('Felaktig Input, vänligen skriv in ett heltal.')

   
 #   for i in range(len(random_list)):    <---- till minne av den mest färglada for-loop jag någonsin skapat :(
 #        print('% d' % arr[i], end='')
        












  
