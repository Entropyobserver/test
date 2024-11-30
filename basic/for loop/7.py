nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
for key, sub_dict in nested_dict.items():
    for sub_key, value in sub_dict.items():
        print(f"{key} -> {sub_key}: {value}")