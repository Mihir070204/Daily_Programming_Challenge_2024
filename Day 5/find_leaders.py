def find_leaders(arr):
    n = len(arr)
    leaders = []
    m = arr[-1]
    leaders.append(m)
    
    for i in range(n-2,-1,-1):
        if arr[i] > m:
            leaders.append(arr[i])
            m = arr[i]
    
    return leaders[::-1]

if __name__ == "__main__":
    arr1 = [1,2,3,4,0]
    print(find_leaders(arr1))
    
    arr2 = [7,10,4,10,6,5,2]
    print(find_leaders(arr2))
    
    arr3 = [5]
    print(find_leaders(arr3))
    
    arr4 = [100,50,20,10]
    print(find_leaders(arr4))
    
    arr5 = [i for i in range(1,1000001)]
    print(find_leaders(arr5))