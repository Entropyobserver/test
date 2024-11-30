def print_lcs_matrix(gtokens, stokens):
    # Create and fill LCS matrix
    lcs = {}
    
    print("\nBuilding LCS matrix process:")
    
    # Initialize
    for i in range(len(gtokens) + 1):
        lcs[(i, 0)] = 0
    for j in range(len(stokens) + 1):
        lcs[(0, j)] = 0
        
    # Fill matrix and print each step
    for i in range(1, len(gtokens) + 1):
        for j in range(1, len(stokens) + 1):
            if gtokens[i-1] == stokens[j-1]:
                lcs[(i, j)] = lcs[(i-1, j-1)] + 1
                print(f"Position({i},{j}): {gtokens[i-1]} == {stokens[j-1]}, take diagonal value + 1 = {lcs[(i,j)]}")
            else:
                lcs[(i, j)] = max(lcs[(i-1, j)], lcs[(i, j-1)])
                print(f"Position({i},{j}): {gtokens[i-1]} != {stokens[j-1]}, take max of up {lcs[(i-1,j)]} and left {lcs[(i,j-1)]} = {lcs[(i,j)]}")
    
    # Print final matrix
    print("\nFinal LCS Matrix:")
    print("    ", end="")
    print("ε   ", end="")
    for s in stokens:
        print(f"{s}   ", end="")
    print()
    
    for i in range(len(gtokens) + 1):
        if i == 0:
            print("ε   ", end="")
        else:
            print(f"{gtokens[i-1]}   ", end="")
        for j in range(len(stokens) + 1):
            print(f"{lcs[(i,j)]}   ", end="")
        print()
    
    return lcs[(len(gtokens), len(stokens))]

# Test
gtokens = ["A", "B", "C"]
stokens = ["A", "C"]
length = print_lcs_matrix(gtokens, stokens)
print(f"\nThe length of the longest common subsequence is: {length}")