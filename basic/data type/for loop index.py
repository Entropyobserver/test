


# Create a longer example list
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", 
        "Henry", "Ivy", "Jack", "Kelly", "Leo", "Mike", "Nancy", "Oliver"]
print("Original list:", names)
print("\n" + "="*50 + "\n")

# 1. Using enumerate()
print("1. Using enumerate():")
print("1.1 enumerate traversal result:")
enum_result = []
for index, name in enumerate(names):
   enum_result.append(f"{index}: {name}")
   print(f"Processing: Index {index}, Value {name}")
print("\nFinal result:")
for result in enum_result:
   print(result)
print("\n" + "="*50 + "\n")

# 2. Using range() and len()
print("2. Using range() and len():")
range_result = []
print(f"List length: {len(names)}")
print("Traversal process:")
for i in range(len(names)):
   range_result.append(f"{i}: {names[i]}")
   print(f"Processing: Index {i}, Value {names[i]}")
print("\nFinal result:")
for result in range_result:
   print(result)
print("\n" + "="*50 + "\n")

# 3. Using a manual counter
print("3. Using a manual counter:")
counter_result = []
index = 0
print("Traversal process:")
for name in names:
   counter_result.append(f"{index}: {name}")
   print(f"Processing: Counter {index}, Value {name}")
   index += 1
print("\nFinal result:")
for result in counter_result:
   print(result)
print("\n" + "="*50 + "\n")

# 4. Using zip() and range()
print("4. Using zip() and range():")
zip_result = []
print("Traversal process:")
for i, name in zip(range(len(names)), names):
   zip_result.append(f"{i}: {name}")
   print(f"Processing: Index {i}, Value {name}")
print("\nFinal result:")
for result in zip_result:
   print(result)

# Comparison of results
print("\n" + "="*50)
print("\n5. Comparison of results:")
print("\nComparison between methods:")
for i in range(len(names)):
   print(f"Index {i}:")
   print(f"enumerate: {enum_result[i]}")
   print(f"range+len: {range_result[i]}")
   print(f"counter:    {counter_result[i]}")
   print(f"zip+range: {zip_result[i]}")
   print("-" * 30)

# Performance tips
print("\nUsage suggestions:")
print("""
1. enumerate() - Recommended for:
  - Standard index+value traversal
  - Clear and readable code
  
2. range()+len() - Recommended for:
  - Controlling step size
  - Reverse traversal
  - Modifying the index within the loop
  
3. Manual counter - Recommended for:
  - Custom counting logic
  - Non-numeric indices
  - Conditional counter increments
  
4. zip()+range() - Recommended for:
  - Simultaneously traversing multiple lists
  - Parallel processing of multiple sequences
  - Explicitly pairing indices with values
""")
