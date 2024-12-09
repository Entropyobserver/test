import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

# Load the data with a different encoding
try:
    data = pd.read_csv(r'D:\J\Desktop\language technology\course\combined_sentences.csv', encoding='latin1')
except UnicodeDecodeError:
    data = pd.read_csv(r'D:\J\Desktop\language technology\course\combined_sentences.csv', encoding='cp1252')

# Create a DataFrame
df = pd.DataFrame(data)

# Select only the 'Duration' and 'Average Surprisal' columns for linear regression
df = df[['Duration', 'Average Surprisal']]

# Remove rows where 'Duration' or 'Average Surprisal' is 0 
df = df[(df['Duration'] != 0) & (df['Average Surprisal'] != 0)]



# Define x and y
x = df['Duration'].values.reshape(-1, 1)
y = df['Average Surprisal'].values

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
plt.xlabel('Duration (ms)')
plt.ylabel('Surprisal')
plt.legend()
#plt.savefig('word-level_lin.png')
plt.show()


