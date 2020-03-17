import numpy
import matplotlib.pyplot as plt

# create an array that contains 250 random floats between 0.0 and 5.0
x = numpy.random.uniform(0.0, 5.0, 25000)

print(x)

# draw histogram with 100 bars using x array
plt.hist(x, 100)
plt.show()
