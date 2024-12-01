import matplotlib.pyplot as plt
import numpy as np

# 定义惊奇值函数
def get_surprisal(p):
    return -np.log2(p)

# 生成概率值
probabilities = np.linspace(0.01, 1, 100)  # 避免log(0)的情况

# 计算惊奇值
surprisals = get_surprisal(probabilities)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(probabilities, surprisals, label='Surprisal')
plt.xlabel('Probability (P)')
plt.ylabel('Surprisal (I)')
plt.title('Surprisal vs Probability')
plt.legend()
plt.grid(True)
plt.savefig("sur.png")
plt.show()
