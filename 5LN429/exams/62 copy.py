def f12(c):
    print("\n1. Input string:")
    print(c)
    
    b = c.split()
    print("\n2. List of words after splitting:")
    print(b)
    
    a = [x.strip('.') for x in b]
    print("\n3. List of words after removing periods:")
    print(a)
    
    _2 = {}
    print("\n4. Create an empty dictionary _2:")
    print(_2)
    
    for i in range(len(a)):
        print(f"\n5. Loop #{i+1}")
        print(f"Current index i = {i}")
        try:
            _1 = (a[i], a[i + 2])
            print(f"Attempt to create tuple _1 = {_1}")
            
            if _1 in _2:
                print(f"Tuple {_1} is already in the dictionary, increment value by 1")
                _2[_1] += 1
            else:
                print(f"Tuple {_1} is not in the dictionary, add it and set value to 1")
                _2[_1] = 1
                
            print(f"Current dictionary content: {_2}")
            
        except:
            print('Little darling')
    
    print("\n6. Final returned dictionary:")
    return _2

h = "sun sun sun here it comes. sun sun sun here it comes."
print("Final result:", f12(h))
