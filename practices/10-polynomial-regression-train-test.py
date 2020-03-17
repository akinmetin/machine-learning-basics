import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

# create datasets
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# train dataset will be 80% of the data
train_x = x[:80]
train_y = y[:80]

# test dataset will be remaining 20% of the data
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.title("Polynomial regression")
plt.xlabel("Minutes")
plt.ylabel("Spent money")
plt.plot(myline, mymodel(myline))
plt.show()

# test train dataset using R2
r2 = r2_score(train_y, mymodel(train_x))

# the value ranges from 0 to 1, where 0 means no relationship,
# and 1 means totally related.
print(r2)

# test test dataset using R2
r2_test = r2_score(test_y, mymodel(test_x))

# the value ranges from 0 to 1, where 0 means no relationship,
# and 1 means totally related.
print(r2_test)

# predict spent money in 5 minutes
print(mymodel(5))
