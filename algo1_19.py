def generate_partitions(n):
    if n == 0:
        return []

    result = []
    
    BLOCK = [0] * (n + 1)
    FORWARD = [False] * (n + 1)
    NEXT = [0] * (n + 1)
    PREV = [0] * (n + 1)

    for i in range(1, n + 1):
        BLOCK[i] = 1
        FORWARD[i] = True
    
    NEXT[1] = 0

    def format_partition():
        parts = []
        curr_block = 1
        while curr_block != 0:
            elements = [str(i) for i in range(1, n + 1) if BLOCK[i] == curr_block]
            if elements:
                parts.append(f"( {' '.join(elements)} )")
            curr_block = NEXT[curr_block]
        return " ".join(parts)

    result.append(format_partition())
    j = n
    
    while j > 1:
        k = BLOCK[j]
        
        if FORWARD[j]: 
            if NEXT[k] == 0:
                NEXT[k] = j
                PREV[j] = k
                NEXT[j] = 0
            elif NEXT[k] > j:
                PREV[j] = k
                NEXT[j] = NEXT[k]
                PREV[NEXT[j]] = j
                NEXT[k] = j
            
            BLOCK[j] = NEXT[k]
     
        else: 
            BLOCK[j] = PREV[k]
            
            if k == j:
                if NEXT[k] == 0:
                    NEXT[PREV[k]] = 0
                else:
                    NEXT[PREV[k]] = NEXT[k]
                    PREV[NEXT[k]] = PREV[k]

        result.append(format_partition())
        
        j = n
        while j > 1 and ((FORWARD[j] and BLOCK[j] == j) or (not FORWARD[j] and BLOCK[j] == 1)):
            FORWARD[j] = not FORWARD[j]
            j -= 1

    return result

if __name__ == "__main__":
    n = 4
    partitions = generate_partitions(n)
    
    print(f"Set of dividing arrays from 1 to {n}:")
    for p in partitions:
        print(p)