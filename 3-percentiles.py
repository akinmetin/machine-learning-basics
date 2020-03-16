import numpy
'''
Percentiles are used in statistics to give you a number that describes
the value that a given percent of the values are lower than.
'''
# dataset
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# find the percentile of values below 75% of the dataset
x = numpy.percentile(ages, 75)

# 43 and below values are 75% of the dataset
print(x)
