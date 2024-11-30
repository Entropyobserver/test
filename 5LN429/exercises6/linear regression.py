import numpy as np
import matplotlib.pyplot as plt

def print_formula(name, formula):
    print(f"\n{'-'*20} {name} 公式 {'-'*20}")
    print(formula)

def print_calculation(name, calculation):
    print(f"\n>>> {name} 计算过程:")
    print(calculation)

def linear_regression_analysis(X, y):
    # 显示输入数据
    print("\n====== 输入数据 ======")
    print("自变量 X:")
    for i, x in enumerate(X):
        print(f"X[{i}] = {x}")
    
    print("\n因变量 y:")
    for i, yi in enumerate(y):
        print(f"y[{i}] = {yi}")
        
    print("\n数据对应关系:")
    for i in range(len(X)):
        print(f"(X[{i}], y[{i}]) = ({X[i]}, {y[i]})")
    
    print("\n====== 开始一元线性回归分析 ======")
    
    # 1. 计算基本统计量
    n = len(X)
    print(f"\n样本数量 n = {n}")
    
    # 1.1 计算平均值
    print_formula("平均值", "μ = (Σx) / n")
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    print_calculation("X平均值", f"X_mean = ({' + '.join(map(str, X))}) / {n} = {X_mean:.4f}")
    print_calculation("y平均值", f"y_mean = ({' + '.join(map(str, y))}) / {n} = {y_mean:.4f}")
    
    # 1.2 计算方差
    print_formula("方差", "σ² = Σ(x - μ)² / n")
    X_var = np.var(X)
    y_var = np.var(y)
    
    print_calculation("X方差计算过程", "X的偏差平方:")
    for i, x in enumerate(X):
        deviation = x - X_mean
        print(f"  (X[{i}] - X_mean)² = ({x} - {X_mean:.4f})² = {deviation**2:.4f}")
    print(f"X_var = ({' + '.join([f'({x} - {X_mean:.4f})²' for x in X])}) / {n} = {X_var:.4f}")
    
    print_calculation("y方差计算过程", "y的偏差平方:")
    for i, yi in enumerate(y):
        deviation = yi - y_mean
        print(f"  (y[{i}] - y_mean)² = ({yi} - {y_mean:.4f})² = {deviation**2:.4f}")
    print(f"y_var = ({' + '.join([f'({yi} - {y_mean:.4f})²' for yi in y])}) / {n} = {y_var:.4f}")
    
    # 1.3 计算标准差
    print_formula("标准差", "σ = √(σ²)")
    X_std = np.std(X)
    y_std = np.std(y)
    print_calculation("X标准差", f"X_std = √{X_var:.4f} = {X_std:.4f}")
    print_calculation("y标准差", f"y_std = √{y_var:.4f} = {y_std:.4f}")
    
    # 2. 计算协方差
    print_formula("协方差", "cov(X,y) = Σ((x - μx)(y - μy)) / n")
    print_calculation("协方差计算过程", "偏差乘积:")
    covariance = 0
    for i in range(n):
        x_dev = X[i] - X_mean
        y_dev = y[i] - y_mean
        prod = x_dev * y_dev
        covariance += prod
        print(f"  (X[{i}] - X_mean)(y[{i}] - y_mean) = ({X[i]} - {X_mean:.4f})({y[i]} - {y_mean:.4f}) = {prod:.4f}")
    covariance /= n
    print(f"covariance = {covariance:.4f}")
    
    # 3. 计算相关系数
    print_formula("相关系数", "r = cov(X,y) / (σx * σy)")
    correlation = covariance / (X_std * y_std)
    print_calculation("相关系数", f"r = {covariance:.4f} / ({X_std:.4f} * {y_std:.4f}) = {correlation:.4f}")
    
    # 4. 计算回归系数
    print_formula("回归系数 β1", "β1 = cov(X,y) / var(X)")
    beta1 = covariance / X_var
    print_calculation("β1", f"beta1 = {covariance:.4f} / {X_var:.4f} = {beta1:.4f}")
    
    print_formula("回归系数 β0", "β0 = μy - β1 * μx")
    beta0 = y_mean - beta1 * X_mean
    print_calculation("β0", f"beta0 = {y_mean:.4f} - {beta1:.4f} * {X_mean:.4f} = {beta0:.4f}")
    
    # 5. 计算拟合值和残差
    y_pred = beta0 + beta1 * X
    residuals = y - y_pred
    
    print("\n====== 拟合值和残差 ======")
    for i in range(n):
        print(f"观测点 {i+1}:")
        print(f"  X = {X[i]}")
        print(f"  实际y值 = {y[i]:.4f}")
        print(f"  预测y值 = {beta0:.4f} + {beta1:.4f} * {X[i]} = {y_pred[i]:.4f}")
        print(f"  残差 = {residuals[i]:.4f}")
    
    # 6. 计算决定系数 R²
    print_formula("决定系数 R²", "R² = 1 - (Σ(y - ŷ)²) / (Σ(y - μy)²)")
    SSR = np.sum(residuals**2)  # 残差平方和
    SST = np.sum((y - y_mean)**2)  # 总平方和
    r_squared = 1 - SSR/SST
    print_calculation("R²", f"""
残差平方和 SSR = {' + '.join([f'({y[i]:.4f} - {y_pred[i]:.4f})²' for i in range(n)])} = {SSR:.4f}
总平方和 SST = {' + '.join([f'({y[i]:.4f} - {y_mean:.4f})²' for i in range(n)])} = {SST:.4f}
R² = 1 - {SSR:.4f}/{SST:.4f} = {r_squared:.4f}
""")
    
    # 7. 输出回归方程
    print(f"\n====== 回归分析结果 ======")
    print(f"回归方程: y = {beta0:.4f} + {beta1:.4f}x")
    print(f"相关系数 r = {correlation:.4f}")
    print(f"决定系数 R² = {r_squared:.4f}")
    
    # 8. 绘制散点图和回归直线
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='观测点')
    plt.plot(X, y_pred, color='red', label='回归直线')
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {y[i]:.2f})', 
                    (X[i], y[i]), 
                    xytext=(5, 5), 
                    textcoords='offset points')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('一元线性回归分析')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return {
        'beta0': beta0,
        'beta1': beta1,
        'r': correlation,
        'r_squared': r_squared,
        'y_pred': y_pred,
        'residuals': residuals
    }

# 示例数据
X = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.8, 5.2, 6.9, 8.3])

# 执行回归分析
print("\n==================== 一元线性回归分析 ====================")
print("使用示例数据进行分析:")
print("X (自变量):", X)
print("y (因变量):", y)
results = linear_regression_analysis(X, y)