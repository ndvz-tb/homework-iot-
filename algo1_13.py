def generate_subsets_gray_code(n: int):
    B = [0] * n
    i = 0 
    
    while True:
        print(" ".join(map(str, B)))
        
        i += 1
        p = 1
        j = i
        
        while j % 2 == 0:
            j //= 2  
            p += 1
            
        if p <= n:
            B[p - 1] = 1 - B[p - 1]
        else:
            break

if __name__ == "__main__":
    n = 4
    print(f"Послідовність множин для n = {n}:")
    generate_subsets_gray_code(n)