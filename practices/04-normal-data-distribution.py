import numpy
import matplotlib.pyplot as plt

# mean value is 5.0 and standard deviation is 1.0
x = numpy.random.normal(5.0, 1.0, 100000)

# draw histogram with 100 bars using x array
plt.hist(x, 100)
plt.show()
