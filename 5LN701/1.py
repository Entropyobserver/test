import re 
text = "Raccoon, raccoons, Raccoons, raccoon" 
pattern = r"[Rr]accoons?" 
matches = re.findall(pattern, text) 
print(matches)

"""
[Rr]: This part of the pattern matches either an uppercase "R" or a lowercase "r".

accoon: This part of the pattern matches the string "accoon".

s?: This part of the pattern matches zero or one occurrence of the letter "s", allowing for both singular and plural forms.
"""