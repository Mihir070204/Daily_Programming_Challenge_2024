def sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    if len(arr)<=1:
        return arr
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high],arr[mid]
            mid+=1
            high-=1
    
    return arr

if __name__ == "__main__":
    arr1 = [0,1,2,1,0,2,1,0]
    print("Test Case 1: ",sort(arr1))
    
    arr2 = [2,2,2,2]
    print("Test Case 2: ",sort(arr2))
    
    arr3 = [0,0,0,0]
    print("Test Case 3: ",sort(arr3))
    
    arr4 = [1,1,1,1]
    print("Test Case 4: ",sort(arr4))
    
    arr5 = [2,0,1]
    print("Test Case 5: ",sort(arr5))
    
    arr6 = []
    print("Test Case 6: ",sort(arr6))
    