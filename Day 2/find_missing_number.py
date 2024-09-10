def find_missing_number(arr):
    count = 1
    missing_number = 0
    for i in range(len(arr)):
        if arr[i] ==  count:
            count+=1
        else:
            missing_number = count
            break
        
    if missing_number==0:
        missing_number = count
    print(missing_number)

if __name__ == "__main__":
    arr1 = [1,2,4,5]
    find_missing_number(arr1)
    

    arr2 = [2,3,4,5]
    find_missing_number(arr2)
    
    arr3 = [1,2,3,4]
    find_missing_number(arr3)
    
    arr4 = [1]
    find_missing_number(arr4)
    
    arr5 = [i for i in range(1, 1000000)]
    find_missing_number(arr5)