# Create the initial list
fruits = ["apple", "banana", "orange", "mango"]
print("Initial list:", fruits)  
# We create a list called `fruits` with the elements "apple", "banana", "orange", and "mango", and then print the initial list.

# 1. append() Add an element to the end of the list
fruits.append("kiwi")
print("After using append() to add kiwi to the end of list:", fruits)  
# We use the `append()` method to add the element "kiwi" to the end of the `fruits` list, and then print the list after the append operation.

# 2. extend() Add multiple elements to the end of the list
more_fruits = ["pineapple", "grape"]
fruits.extend(more_fruits)
print("After using extend() to add more_fruits,pineapple and grape:", fruits)  
# We create a new list called `more_fruits` with the elements "pineapple" and "grape". We then use the `extend()` method to add all the elements 
# from `more_fruits` to the end of the `fruits` list, and print the list after the extend operation.

# 3. insert() Insert an element at a specified position
fruits.insert(2, "peach")
#fruits.insert( "peach")insert expected 2 arguments, got 1
print("After using insert() to insert peach at index 2:", fruits)  
# We use the `insert()` method to insert the element "peach" at index 2 (the third position) in the `fruits` list, and then print the list after the 
# insert operation.

# 4. remove() Remove the first occurrence of a specified element from the list
fruits.remove("banana")
print("After using remove() to remove the first occurrence of the element:", fruits)  
#fruits.remove() list.remove() takes exactly one argument (0 given)
# We use the `remove()` method to delete the first occurrence of the element "banana" from the `fruits` list, and then print the list after the remove 
# operation.

# 5. pop() Remove and return the element at a specified position, default is the last element
removed_fruit = fruits.pop(3)
print("Element removed by pop():", removed_fruit)
print("After pop():", fruits) 
# We use the `pop()` method to remove and return the element at index 3 (the fourth position) from the `fruits` list. 
# We store the removed element in the variable `removed_fruit` and print it. We then print the `fruits` list after the pop operation.

# 6. count() Count the number of occurrences of a specified element in the list
count = fruits.count("grape")
#count_all = count(fruits)
#print(count_all)int' object is not callable
print("using count() to count the number of a specified element ") 
print("Number of occurrences of 'grape':", count)  # We use the `count()` method to count the number of occurrences of the element "grape" in the `fruits` list, and print the count.

# 7. reverse() Reverse the order of elements in the list
fruits.reverse()
print("After using reverse() to reverse the order of elements:", fruits) 
 # We use the `reverse()` method to reverse the order of the elements in the `fruits` list, and then print the list after the reverse operation.

# 8. sort() Sort the elements in the list
fruits.sort()
print("After using sort() to sort the elements:", fruits)  
# We use the `sort()` method to sort the elements in the `fruits` list in ascending order, and then print the list after the sort operation.
#print(fruits.sort(reverse= True))None

# 9. copy() Create a shallow copy of the list
new_fruits = fruits.copy()
print("New list after copy():", new_fruits)  
# We use the `copy()` method to create a shallow copy of the `fruits` list, and store it in the variable `new_fruits`. We then print the `new_fruits` list.

# 10. index() Return the index of a specified element in the list
index = fruits.index("peach")

print("Index of 'peach':", index)  # We use the `index()` method to find the index of the element "peach" in the `fruits` list, and print the index.
for i in range(len(fruits)):
    print(i,fruits[i])
    print(f"index:{i} element:{fruits[i]}")
for index,ele in enumerate(fruits):
    print(index,ele)
    print(f"index:{i} element:{fruits[i]}")
