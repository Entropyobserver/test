"""

    Write a function f3() that returns None if the input argument is not a
    list. If it is a list, the function should loop over that list, 
    check if the element that the loop is currently on is a string,
    and if it is, add the last character of that string to a new list. 

    Finally, the function should return the new list.

    For example:
    
    print(f3(["wow", "3", 3, "drum"])) 

    should give this output:
    
    ['w', '3', 'm']

"""
def f3(lst):
    result = []
    for i in lst:
        if isinstance(i,str):
            result.append(i[-1])
    return result
print(f3(["wow","3",3,"drum"]))
