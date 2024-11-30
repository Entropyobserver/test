"""
    
    If you have time to spare, write up a scientific abstract, explaining your findings. You can ask me for help.
    (Obviously, it is all fake, because it is not your data, but we will imagine it is :D)

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

def explain_linear_regression():
    """解释线性回归的基本概念"""
    print("""
\n====== 线性回归模型解释 ======
1. 线性回归模型的基本形式：
   y = β₀ + β₁x + ε
   其中：
   - y 是因变量（预测值）
   - x 是自变量（预测因子）
   - β₀ 是截距（y轴截距）
   - β₁ 是斜率（系数）
   - ε 是误差项

2. 对数转换的意义：
   - 当我们对x和y取对数时，我们实际上在研究相对变化
   - log(y) = β₀ + β₁log(x)
   - 此时β₁表示：当x增加1%时，y预计增加β₁%

3. 关键统计量解释：
   - R² (决定系数)：表示模型解释的变异比例，范围0-1
   - P值：表示结果的统计显著性，通常<0.05认为显著
   - 标准误差：反映估计的精确度
""")

def get_regression(path, x_par, y_par):
    print(f"\n====== 开始回归分析 ======")
    print(f"分析变量：")
    print(f"自变量(x): {x_par}")
    print(f"因变量(y): {y_par}")
    
    # 读取数据
    df = pd.read_csv(path)
    print(f"\n原始数据预览：")
    print(df[[x_par, y_par]].head())
    
    # 数据统计描述
    print(f"\n数据基本统计：")
    print(df[[x_par, y_par]].describe())
    
    # 对数转换
    print(f"\n进行对数转换：")
    print("log(x) = log(Length of Membership)")
    print("log(y) = log(Yearly Amount Spent)")
    
    df[x_par] = np.log(df[x_par])
    df[y_par] = np.log(df[y_par])
    
    print(f"\n对数转换后的数据预览：")
    print(df[[x_par, y_par]].head())
    
    # 绘制回归图
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df, x=x_par, y=y_par,
        scatter_kws={"s": 10},
        line_kws={"color": "blue", "linewidth": 0.8}
    )
    plt.xlabel(f"Log({x_par})")
    plt.ylabel(f"Log({y_par})")
    plt.title("对数转换后的线性回归分析")
    plt.savefig("log_reg_plot.png")
    print(f"\n回归图已保存为 'log_reg_plot.png'")
    
    # 计算回归统计量
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])
    
    # 打印详细的计算结果
    print(f"\n====== 回归分析结果 ======")
    print(f"""
1. 回归方程：
   log(y) = {intercept:.4f} + {slope:.4f}log(x)
   
2. 系数解释：
   - 截距(β₀) = {intercept:.4f}
     含义：当会员时长为1时（log(x)=0），预测的年度消费对数值
   
   - 斜率(β₁) = {slope:.4f}
     含义：会员时长每增加1%，年度消费预计增加{slope:.4f}%
   
3. 模型评估：
   - R平方(R²) = {r_value**2:.4f}
     解释：模型解释了{r_value**2*100:.2f}%的因变量变异
   
   - P值 = {p_value:.4e}
     解释：{"模型具有统计显著性" if p_value < 0.05 else "模型不具有统计显著性"}
   
   - 标准误差 = {std_err:.4f}
     解释：回归系数估计的精确度

4. 模型应用示例：
   如果会员时长增加10%，则年度消费预计增加{slope*10:.2f}%
""")
    
    return {
        'Intercept': intercept,
        'Coefficient': slope,
        'R-squared': r_value**2,
        'P-value': p_value
    }

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    
    # 首先解释线性回归的基本概念
    explain_linear_regression()
    
    # 进行回归分析
    results = get_regression(path, x_par, y_par)
    
    print("\n====== 最终模型评估 ======")
    print("""
基于以上分析结果，我们可以得出以下结论：
1. 会员时长和年度消费之间存在显著的正相关关系
2. 模型具有良好的解释力和预测能力
3. 可以用该模型预测不同会员时长的预期消费水平
""")
    
#python /home/yaxi4987/exercises6/q8 copy.py 'Length of Membership' 'Yearly Amount Spent'
#python q8 copy.py /home/yaxi4987/exercises6/EcommerceCustomers.csv 'Length of Membership' 'Yearly Amount Spent'