from scipy import stats
import matplotlib.pyplot as plt

'''Linear regression uses the relationship between
the data-points to draw a straight line through all them.
'''

# x is car age, y is speed
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

# draw simple x, y graph using above arrays
plt.scatter(x, y)
plt.xlabel("car age")
plt.ylabel("speed")
plt.plot(x, mymodel)
plt.show()

# R-squared
'''
The r-squared value ranges from 0 to 1, where 0 means no relationship,
and 1 means 100% related.
'''
print(r)

'''
The result -076 shows that there is a relationship, not perfect,
but it indicates that we could use linear regression in future predictions.
If the result is like 0.01, it indicates a very bad relationship,
and tells us that this data set is not suitable for linear regression.
'''

# predicting future values
speed = myfunc(10)

print(speed)
