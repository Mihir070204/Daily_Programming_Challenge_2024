def sorting_into_two_arrays(arr1,arr2):
    while(arr1[-1]>arr2[0]):
        arr1[-1],arr2[0] = arr2[0],arr1[-1]
        arr1.sort()
        arr2.sort()
    return arr1,arr2

if __name__ == "__main__":
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    print(sorting_into_two_arrays(arr1,arr2))
    
    arr3 = [10, 12, 14]
    arr4 = [1, 3, 5]
    print(sorting_into_two_arrays(arr3,arr4))
    
    arr5 = [2, 3, 8]
    arr6 = [4, 6, 10]
    print(sorting_into_two_arrays(arr5,arr6))
    
    arr7 = [1]
    arr8 = [2]
    print(sorting_into_two_arrays(arr7,arr8))
    
    arr9 = [i for i in range(1,100001)]
    arr10 = [i for i in range(50001,100001)]
    print(sorting_into_two_arrays(arr9,arr10))