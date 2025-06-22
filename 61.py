# return multiple values from a function
import statistics


def mean_median_mode(list1):
    # returning multiple values ,this will return values in the form of tuples
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)


print(mean_median_mode([1, 2, 3, 4, 5, 6, 7, 8]))  # passing list as argument
# storing mean,median,mode in diff variables
a, b, c = mean_median_mode([1, 2, 3, 4, 5, 6, 7, 8])
print(f"mean is {a}, median is {b}, mode is {c}")


def mean_median_mode2(list1):
    # returning multiple values in the form of list,just put square braces
    return [statistics.mean(list1), statistics.median(list1), statistics.mode(list1)]


print(mean_median_mode2([1, 2, 3, 4, 5, 6, 7, 8]))


def add(a, b):  # multiple return statements ina function,we can return multiple values from multiple return statements
    if a == 0 and b == 0:
        return
    else:
        return a+b


print(add(0, 0))
