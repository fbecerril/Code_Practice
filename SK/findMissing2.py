def findMissing(arr):
    #set indexes
    start = 0
    end = len(arr)-1
    while(start < end):
        middle = (start + end) / 2
        if(arr[middle] != middle and arr[middle-1] == middle-1):
            return middle
        elif(arr[middle] == middle):
            start = middle
        else:
            end = middle
