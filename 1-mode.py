from scipy import stats

# dataset
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# the value that appears the most number of times
x = stats.mode(speed)

print(x)
