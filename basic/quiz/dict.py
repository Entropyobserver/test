#What is output?

car = {'make': 'Toyota', 'model': 'Camry', 'year': 2020}
print(car.get('Model', 'Volvo'))
'''
Volvo
None
KeyError
Camry
The car dictionary contains the keys 'make', 'model', and 'year'.
The get method is used to retrieve the value associated with the key 'Model'.
Dictionary keys are case-sensitive, so 'Model' (with an uppercase ‘M’) is different from 'model' (with a lowercase ‘m’).
Since 'Model' does not exist in the dictionary, the get method returns the default value provided, which is 'Volvo'.
'''