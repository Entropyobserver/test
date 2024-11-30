import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成模拟数据
np.random.seed(42)
x = np.linspace(1, 100, 100)
y = 10 * np.exp(0.05 * x) + np.random.normal(0, 100, size=x.shape)

# 创建DataFrame
df = pd.DataFrame({'x': x, 'y': y})

# 过滤掉 y <= 0 的数据点
df_filtered = df[df['y'] > 0]

# 线性回归（不进行对数转换）
model1 = LinearRegression()
model1.fit(df[['x']], df['y'])
y_pred1 = model1.predict(df[['x']])

# 线性回归（对因变量进行对数转换）
model2 = LinearRegression()
log_y = np.log(df_filtered['y'])
model2.fit(df_filtered[['x']], log_y)
y_pred2 = np.exp(model2.predict(df[['x']]))

# 绘制拟合曲线
plt.figure(figsize=(14, 6))

# 不进行对数转换的拟合
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', s=10, label='Original Data')
plt.plot(x, y_pred1, color='red', linewidth=2, label='Linear Fit (No Log)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression without Log Transformation')
plt.legend()

# 进行对数转换的拟合
plt.subplot(1, 2, 2)
plt.scatter(df_filtered['x'], df_filtered['y'], color='blue', s=10, label='Filtered Data')
plt.plot(x, y_pred2, color='green', linewidth=2, label='Linear Fit (Log Transformed)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Log Transformation')
plt.legend()

plt.tight_layout()
plt.show()

# 打印 R² 和残差分析
print("====== Linear Regression without Log Transformation ======")
r_squared1 = model1.score(df[['x']], df['y'])
print(f"R-squared: {r_squared1:.4f}")

print("\n====== Linear Regression with Log Transformation ======")
r_squared2 = model2.score(df_filtered[['x']], log_y)
print(f"R-squared: {r_squared2:.4f}")