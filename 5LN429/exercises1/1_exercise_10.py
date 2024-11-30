"""
    
    Write code so that you have a variable containing an empty list.
    Assign to a variable a tuple containing the strings "hello" and "there".
    Append the tuple to the list.
    
    Print the "r" in the second string, in the tuple, in the list.    

    The output should be:

r

"""
x = []
y = ("hello","there")
x.append(y)
print(x[0][1][3])

