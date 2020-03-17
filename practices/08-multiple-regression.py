from pandas import read_csv
from sklearn import linear_model

# path for the dataset file
path = "datasets/cars.csv"

# read all data in .csv file into a data frame
df = read_csv(path)

# array of data
array = df.values
print("Original data:\n", array)

# X is independent, y is dependent
X = df[['Weight', 'Volume']]
y = df['CO2']

regression = linear_model.LinearRegression()
regression.fit(X, y)

# predict the CO2 emission of a car where the weight is 2300g,
# and the volume is 1300ccm:
predictedCO2 = regression.predict([[2300, 1300]])
print("Predicted CO2\n", predictedCO2)
