def smaller_than_100(x):
    print(f"Function smaller_than_100 called with argument x = {x}")
    print(f"Checking if {x} is less than 100")
    if x < 100:
        print(f"{x} is less than 100")
        print("Returning True")
        return True
    else:
        print(f"{x} is not less than 100")
        print("Returning False")
        return False

print("Calling smaller_than_100(110)")
result = smaller_than_100(110)
print(f"Result of smaller_than_100(110): {result}")

print("\nCalling smaller_than_100(90)")
result = smaller_than_100(90)
print(f"Result of smaller_than_100(90): {result}")