for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            print("B", end=" ")
        else:
            print("W", end=" ")
    print()