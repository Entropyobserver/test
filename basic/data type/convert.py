"""
text = "hello, world!"

print(list(text))

print(text.split())

lst = []
for i in text:
    lst.append(i)
print(lst)

print([i for i  in text])

word_lst = []
for word in text.split():
    word_lst.append(word)
print(word_lst)

word_lst2 = [word for word in text.split()]
print(word_lst2)
"""
my_list = ['Hello', 'world']
result = ' '.join(my_list)
print(result)


result2 = str(my_list)
print(result2)  

result3 = ''
for s in my_list:
    result3 += str(s) + ' '
result3 = result3.strip()
print(result3)

result4 = ''
for s in my_list:
    result4 = ''.join(s)
result4 = result4.strip()
print(result4)