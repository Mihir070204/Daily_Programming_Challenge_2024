def reverse_string(s: str) -> str:
    words = s.strip().split()
    words = words[::-1]
    reverse = " ".join(words)
    return reverse

if __name__ == "__main__":
    str1 = "the sky is blue"
    print(reverse_string(str1))
    
    str2 = "  hello world  "
    print(reverse_string(str2))
    
    str3 = "a good   example"
    print(reverse_string(str3))
    
    str4 = "    "
    print(reverse_string(str4))
    
    str5 = "word"
    print(reverse_string(str5))