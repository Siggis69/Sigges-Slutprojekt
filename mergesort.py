import time
from randomlist import generate_random_list

random_list = generate_random_list(10000, 1, 10000)

def merge(arr1, arr2):
    x = 0
    y = 0
    result = []

    while (x < len(arr1)) and (y < len(arr2)):
        if arr2[y] > arr1[x]:
            result.append(arr1[x])
            x += 1
        else:
            result.append(arr2[y])
            y += 1

    while (x < len(arr1)):
        result.append(arr1[x])
        x += 1

    while (y < len(arr2)):
        result.append(arr2[y])
        y += 1

    return result

def mergeSort(random_list):
    if len(random_list) <= 1:
        return random_list

    mid = len(random_list) // 2
    left = mergeSort(random_list[:mid])
    right = mergeSort(random_list[mid:])

    return merge(left, right)

if __name__ == '__main__':
    start_time = time.time()  # Starta tidtagning för mergesort
    random_list_sorted = mergeSort(random_list)
    end_time = time.time()  # Stoppa tidtagning för mergesort
    print(f"Mergesort tog {end_time - start_time:.5f} sekunder")
