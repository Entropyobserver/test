import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# 使用你的 make_datasets() 函数
def make_datasets():
    from sklearn.datasets import make_circles, make_classification, make_moons

    n_samples = 200
    data = list()
    data.append({'title': "2 classes", 
                 'data': make_classification(n_samples=n_samples, n_classes=2, 
                                             n_features=2, n_redundant=0, n_informative=2, 
                                             random_state=3, n_clusters_per_class=1)})
    data.append({'title': "3 classes", 
                 'data': make_classification(n_samples=n_samples, n_classes=3, 
                                             n_features=2, n_redundant=0, n_informative=2, 
                                             random_state=3, n_clusters_per_class=1)})
    data.append({'title': "Moons", 
                 'data': make_moons(n_samples=n_samples, noise=0.1, random_state=0)})
    data.append({'title': "Circles", 
                 'data': make_circles(n_samples=n_samples, noise=0.05, factor=0.5, random_state=0)})
    theta = np.linspace(np.pi/2, np.pi*3/2, num=n_samples//2)
    X = np.concatenate([np.zeros((n_samples//2, 2)), np.column_stack([np.cos(theta), np.sin(theta)])])
    y = np.concatenate([np.zeros(n_samples//2), np.ones(n_samples//2)])
    X += np.random.normal(scale=0.1, size=X.shape)
    data.append({'title': "Moon and blob", 
                 'data': (X, y)})
    X = np.random.uniform(-1, 1, size=(n_samples, 2))
    y = np.asarray([1 if (X[i, 0]>0 or X[i, 1]>0) and not (X[i, 0]>0 and X[i, 1]>0) else 0 for i in range(n_samples)])
    data.append({'title': "XOR", 
                 'data': (X, y)})
    return data


# 定义手动调参的函数
def manual_tuning(datasets):
    # 定义参数搜索范围
    hidden_layer_sizes = [(50,), (100,), (150,), (50, 50), (100, 50)]
    alphas = np.logspace(-2, -6, 5)
    learning_rates = np.logspace(-1, -4, 4)
    activations = ['relu', 'logistic', 'tanh']
    solvers = ['adam', 'sgd', 'lbfgs']
    
    # 记录最佳参数和分数
    best_params = {}
    best_scores = {}
    
    # 遍历每个数据集
    for dataset in datasets:
        X, y = dataset['data']
        title = dataset['title']
        
        best_score = 0
        best_param = None
        
        print(f"\nTuning parameters for dataset: {title}")
        
        # 遍历所有参数组合
        for hidden_layer in hidden_layer_sizes:
            for alpha in alphas:
                for lr in learning_rates:
                    for activation in activations:
                        for solver in solvers:
                            try:
                                # 初始化模型
                                model = MLPClassifier(hidden_layer_sizes=hidden_layer, 
                                                      alpha=alpha, 
                                                      learning_rate_init=lr, 
                                                      activation=activation, 
                                                      solver=solver, 
                                                      max_iter=500, 
                                                      random_state=42)
                                # 训练模型
                                model.fit(X, y)
                                
                                # 计算准确率
                                score = model.score(X, y)
                                print(f"Params: {hidden_layer}, {alpha}, {lr}, {activation}, {solver} | Score: {score:.4f}")
                                
                                # 更新最佳参数
                                if score > best_score:
                                    best_score = score
                                    best_param = (hidden_layer, alpha, lr, activation, solver)
                            except Exception as e:
                                # 捕获可能的训练错误
                                print(f"Error with params: {hidden_layer}, {alpha}, {lr}, {activation}, {solver}")
                                continue
        
        # 保存最佳结果
        best_scores[title] = best_score
        best_params[title] = best_param
        
        print(f"\nBest score for dataset '{title}': {best_score:.4f}")
        print(f"Best parameters: {best_param}\n{'-'*50}")
    
    return best_scores, best_params


# 主函数
def main():
    # 生成数据集
    datasets = make_datasets()
    
    # 调参
    best_scores, best_params = manual_tuning(datasets)
    
    # 打印最终结果
    print("\nFinal Results:")
    for title in best_scores:
        print(f"Dataset: {title}")
        print(f"Best Score: {best_scores[title]:.4f}")
        print(f"Best Parameters: {best_params[title]}\n")


if __name__ == '__main__':
    main()
