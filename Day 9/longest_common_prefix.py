def longest_common_prefix(strs):
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first),len(last))
    
    i = 0
    
    while i < min_length and first[i] == last[i]:
        i +=1
        
    if i == 0:
        return "No common"
    
    return first[:i]

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs1))
    
    strs2 = ["dog", "racecar", "car"]
    print(longest_common_prefix(strs2))
    
    strs3 = ["apple", "ape", "april"]
    print(longest_common_prefix(strs3))
    
    strs4 = [""]
    print(longest_common_prefix(strs4))
    
    strs5 = ["alone"]
    print(longest_common_prefix(strs5))