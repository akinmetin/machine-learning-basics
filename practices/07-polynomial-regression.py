import numpy
import matplotlib.pyplot as plt

# dataset for hours of the day
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]

# dataset for speed
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]


mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# line between 1 and 22
line = numpy.linspace(1, 22, 100)

# draw the value pairs into graph
plt.scatter(x, y)

# draw line of polynomial regression
plt.plot(line, mymodel(line))
plt.show()

# predict speed for 17 o'clock
speed = mymodel(17)

print(speed)
