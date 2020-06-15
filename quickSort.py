# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )          # index of smaller element 
    pivot = arr[high][0]   # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j][0] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i][0],arr[j][0] = arr[j][0],arr[i][0] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 
arr = [[0, 0], [7, 3], [8, 0], [9, 1], [1, 4], [8, 4]] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)
for i in range(n): 
    print (arr[i][0], " ", arr[i][1]), 
  
# This code is contributed by Mohit Kumra 