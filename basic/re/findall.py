import re
furniture = ["chair", "table", "stool", "couch"]
pattern = r"c"
matches = []
for word in furniture:
    test = re.findall(pattern, word)
    matches.append(test)
print(matches)

import re
words = "chair table stool couch"
pattern = r"c\w+"
matches = re.findall(pattern, words)
print(matches)

