import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

# Load the data
data = pd.read_csv(r'D:\J\Desktop\language technology\course\5LN715\ans2\output.csv')

# Create a DataFrame
df = pd.DataFrame(data)

# Define x and y
x = df['Duration'].values.reshape(-1, 1)
y = df['Surprisal'].values

# Create a linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict y values
y_pred = model.predict(x)

# Calculate R² value
r2 = r2_score(y, y_pred)

# Using statsmodels to get p-value and intercept
x_with_const = sm.add_constant(x)
model_sm = sm.OLS(y, x_with_const).fit()
p_value = model_sm.pvalues[1]
intercept = model_sm.params[0]
coefficient = model_sm.params[1]

# Print the results
print(f"Intercept: {intercept}")
print(f"Coefficient: {coefficient}")
print(f"R² value: {r2}")
print(f"P-value: {p_value}")

# Plot the linear regression
plt.scatter(x, y, alpha=0.5, label='Data points')
plt.plot(x, y_pred, color='red', label='Linear regression line')
plt.title('Linear Regression of Duration and Surprisal')
plt.xlabel('Duration')
plt.ylabel('Surprisal')
plt.legend()
plt.show()

