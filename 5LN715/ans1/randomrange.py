#生成一个随机整数：


import random

random_number = random.randrange(1000)
print(f"随机生成的整数是: {random_number}")
#生成多个随机整数：

print("........................")
for _ in range(5):
    print(random.randrange(1000))
#生成特定范围内的随机整数：

print("........................")

# 生成一个从 10 到 99 之间的随机整数
random_number = random.randrange(10, 100)
print(f"随机生成的整数是: {random_number}")