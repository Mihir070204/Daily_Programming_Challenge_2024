'''def find_duplicate_number(arr):
    duplicate_number = 0
    for i in range (len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                duplicate_number = arr[i]
    print("Duplicate Number: ",duplicate_number)'''

def find_duplicate_number(nums):
    freq={}
    for num in nums:
        if num in freq:
            return num
        else:
            freq[num]=1

if __name__ == "__main__":
    arr1 = [1,3,4,2,2]
    print(find_duplicate_number(arr1))
        
    arr2 = [3,1,3,4,2]
    print(find_duplicate_number(arr2))
    
    arr3 = [1,1]
    print(find_duplicate_number(arr3))
    
    arr4 = [1,4,4,2,3]
    print(find_duplicate_number(arr4))
    
    arr5 = [i for i in range(1000000)]
    arr5.append(50000)
    print(find_duplicate_number(arr5))