import re
pattern = r'\d+'
text = '235hel678lohej'
result = re.search(pattern, text)
print( result.group())
#The re.search() function in Python’s re module only finds the 
# first match of the pattern in the text.
#The re.findall() function returns a list of all matches of the 
# pattern in the text, so you get both 235 and 678

#What is the output of the code below?
import re
text = "I love berry, for example, blackberry, blueberry, raspberry, and boysenberry." 
pattern = r'\b\w+berry\b'
matches = re.findall(pattern, text)
print(len(matches),type(matches))

import re
pattern = r"\\\az"
print(pattern)