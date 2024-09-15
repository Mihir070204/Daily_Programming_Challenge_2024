def trapping_rain_water(arr):
    n = len(arr)
    left = 0
    right = 0
    res = 0
    
    if n<3:
        return 0
    
    for i in range(1,n-1):
        
        left = arr[i]
        for j in range(i):
            left = max(left,arr[j])
            
        right = arr[i]
        for j in range(i+1,n):
            right = max(right,arr[j])
            
        res = res + (min(left,right) - arr[i])
    
    return res

if __name__ == "__main__":
    arr1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapping_rain_water(arr1))
    
    arr2 = [4, 2, 0, 3, 2, 5]
    print(trapping_rain_water(arr2))
    
    arr3 = [1, 1, 1]
    print(trapping_rain_water(arr3))
    
    arr4 = [5]
    print(trapping_rain_water(arr4))
    
    arr5 = [2, 0, 2]
    print(trapping_rain_water(arr5))