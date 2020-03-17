from pandas import read_csv
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# path for the dataset file
path = "datasets/shows.csv"

# read all data in .csv file into a data frame
df = read_csv(path)

print("Original data:\n", df)

# convert 'Nationality' values into 0, 1 and 2
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)

# convert 'GO' values into 0 and 1
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print("Converted data:\n", df)

# predict from
features = ['Age', 'Experience', 'Rank', 'Nationality']

# target values to predict
predict_features = ['Go']

X = df[features]
y = df[predict_features]

print(X)
print(y)

# create a decision tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
