arr = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort(arr):
    
    n = len(arr)     
   
    
    for i in range(n-1):    # Kollar om den redan är sorterad (behöver inte genomgå sorterings processen)

        swapped = False
        for j in range(0, n-i-1):    # Kollar igenom alla element och byter plats om nästa element är större
           
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:     # Om inget bytt plats lämnar man bara main loopen
            return



bubbleSort(arr)

print("Sorterad lista är:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
    
    
def mergesort(arr):
    
    n = len(arr)
    
    


