import re

pattern = r"st(o(le(en)?)|eal(s|ing)?)"
texts = ["steal", "steals", "stealing", "stole", "stolen"]

for text in texts:
    match = re.match(pattern, text)
    if match:
        print(f"Text: {text}")
        print("Group 0 (whole match):", match.group(0))
        print("Group 1:", match.group(1))
        print("Group 2:", match.group(2))
        print("Group 3:", match.group(3))
        print("Group 4:", match.group(4))
        print()
