import re
english_pron = ["cheat", "cheese", "chain", "chart"]
pattern = r"ch"
replacement = "sh"
swedish_pron = []
for word in english_pron:
    swedish = re.sub(pattern, replacement, word)
    swedish_pron.append(swedish)
print(swedish_pron)