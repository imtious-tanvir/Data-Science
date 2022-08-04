import numpy
import statistics
import scipy.stats
dataset = [24, 16, 30, 10, 24, 28, 38, 2, 4, 36, 15]
mean = numpy.mean(dataset)
median = numpy.median(dataset)
mode1 = statistics.mode(dataset)
mode2 = scipy.stats.mode(dataset)
print("Average is ",mean)
print("Middle value is",median)
print("Mode is ",mode1)
print("Mode is ",mode2)
