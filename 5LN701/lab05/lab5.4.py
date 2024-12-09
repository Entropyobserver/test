import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
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


# 定义网格搜索的函数
def grid_search_tuning(datasets):
    # 定义参数范围
    param_grid = {
        'hidden_layer_sizes': [(50,), (100,), (150,), (50, 50), (100, 50)],
        'alpha': np.logspace(-2, -6, 5),
        'learning_rate_init': np.logspace(-1, -4, 4),
        'activation': ['relu', 'logistic', 'tanh'],
        'solver': ['adam', 'lbfgs']  # 注意： 'sgd' 通常比 'adam' 慢，所以这里只选择效率较高的优化器
    }

    # 记录每个数据集的最佳参数和分数
    best_scores = {}
    best_params = {}

    # 遍历每个数据集
    for dataset in datasets:
        X, y = dataset['data']
        title = dataset['title']
        
        print(f"\nPerforming Grid Search for dataset: {title}")
        
        # 创建 MLP 模型
        model = MLPClassifier(max_iter=500, random_state=42)
        
        # 创建 GridSearchCV 对象
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            scoring='accuracy',
            cv=3,  # 3 折交叉验证
            verbose=1,
            n_jobs=-1  # 并行加速
        )
        
        # 划分训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # 执行网格搜索
        grid_search.fit(X_train, y_train)
        
        # 最优参数和分数
        best_scores[title] = grid_search.best_score_
        best_params[title] = grid_search.best_params_
        
        # 输出结果
        print(f"Best score for dataset '{title}': {grid_search.best_score_:.4f}")
        print(f"Best parameters: {grid_search.best_params_}")
        
        # 测试集上的表现
        test_score = grid_search.best_estimator_.score(X_test, y_test)
        print(f"Test set accuracy: {test_score:.4f}\n{'-'*50}")
    
    return best_scores, best_params


# 主函数
def main():
    # 生成数据集
    datasets = make_datasets()
    
    # 使用网格搜索进行调参
    best_scores, best_params = grid_search_tuning(datasets)
    
    # 打印最终结果
    print("\nFinal Results:")
    for title in best_scores:
        print(f"Dataset: {title}")
        print(f"Best Score (CV): {best_scores[title]:.4f}")
        print(f"Best Parameters: {best_params[title]}\n")


if __name__ == '__main__':
    main()
