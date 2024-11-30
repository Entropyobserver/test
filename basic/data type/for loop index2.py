names = ["Alice", "Bob", "Charlie"]
#lst = []
for index, name in enumerate(names):
    print(f"{index}: {name}")
    #lst.append((index,name))
#print(lst)

names = ["Alice", "Bob", "Charlie"]
#lst = []
for index, name in enumerate(names):
    print(f"{index}: {name}")
    #lst.extend([index,name])
#print(lst)

names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(f"{i}: {names[i]}")

names = ["Alice", "Bob", "Charlie"]
index = 0
for name in names:
    print(f"{index}: {name}")
    index += 1
names = ["Alice", "Bob", "Charlie"]
index = 0
for name in names:
    print(f"{index}: {name}")
    index += 1

names = ["Alice", "Bob", "Charlie"]
for i, name in zip(range(len(names)), names):
    print(f"{i}: {name}")

