import re
words = ["bike", "bikes", "biking", "biker"]
pattern = r"bike$"
matches = []
for word in words:
    if re.match(pattern, word):
        matches.append(word)
print(matches)

import re
words = ["bike", "bikes", "biking", "biker"]
pattern = r"bik(e(er|s)?|ing)"
matches = []
for word in words:
    if re.match(pattern, word):
        matches.append(word)
print(matches)

