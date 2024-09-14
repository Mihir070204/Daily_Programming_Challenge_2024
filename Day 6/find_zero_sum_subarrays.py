def find_zero_sum_subarrays(arr):
    n = len(arr)
    result = []
       
    for i in range(n):
        current_sum = 0
        
        for j in range(i,n):
            current_sum += arr[j]                        
            
            if current_sum == 0:
                result.append((i,j))
    
    return result   
    
if __name__ == "__main__":
    print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))
    print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))
    print(find_zero_sum_subarrays([1, 2, 3, 4]))
    print(find_zero_sum_subarrays([0, 0, 0]))
    print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))
    