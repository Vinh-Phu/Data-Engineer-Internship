def mergeArray(array1,array2):
    return array1+array2 

def sortedArray(array): #Using Bubble sort
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

def findMedian(arr1,arr2):
    arr=mergeArray(arr1,arr2)
    arr=sortedArray(arr)
    n=len(arr)
    if ((n%2) != 0):
        midPos=int(n/2)
        Median = arr[midPos]
    else:
        leftMPos= int(n/2)-1
        rightMPos = leftMPos+1
        Median = (arr[leftMPos]+arr[rightMPos])/2
    print('Merge array:',arr,'and Median is', Median)
    return Median
def main():
     arr1 = [1,3,6]
     arr2 = [1,2,10]
     Median = findMedian(arr1,arr2)
main()

