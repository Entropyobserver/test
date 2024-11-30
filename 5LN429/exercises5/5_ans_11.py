import re
result = re.match(r'(\d+)([a-zA-Z]+)', '123abc456')
print(result.group(1))  # Should print: '123'
print(result.group(2))  # Should print: 'abc'

# Create groups in the pattern to match digits and letters.

