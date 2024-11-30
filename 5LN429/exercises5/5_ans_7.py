import re

result = re.match(r'\d+', '123abc456')

print(result.group())  # Output: '123'

