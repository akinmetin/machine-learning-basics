import numpy

# standard deviation
# dataset
speed = [32, 111, 138, 28, 59, 77, 97]

x = numpy.std(speed)

print("\nMean(average) is:", numpy.mean(speed))
print("\nStandard deviation is:", x)
'''
Standard deviation is most of the values are within
the range of 0.9 from the mean(average) value.
Standard deviation is also equals to square root of
the variance
'''

# variance
'''
variance is the average number of squared differences
between the values and mean(average)
'''
y = numpy.var(speed)
print("\nVariance is:", y)
