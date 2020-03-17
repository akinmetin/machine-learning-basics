import numpy
import matplotlib.pyplot as plt

# x is car age, y is speed
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# draw simple x, y graph using above arrays
plt.scatter(x, y)
plt.xlabel("car age")
plt.ylabel("speed")
plt.show()

# mean is 5.0, standard deviation is 1.0 and total 1000 random values
a = numpy.random.normal(5.0, 1.0, 1000)

# mean is 10.0, standard deviation is 2.0 and total 1000 random values
b = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(a, b)
plt.show()
