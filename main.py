import statistics


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def get_min(array):
    minimum = array[0]
    for i in array:
        if i < minimum:
            minimum = i
    return minimum


def get_max(array):
    maximum = array[0]
    for i in array:
        if i > maximum:
            maximum = i
    return maximum


def get_average(array):
    average = sum(array) / len(array)
    return average


def get_median(array):
    if len(array) % 2 == 1:
        median = array[len(array) // 2]
        return median
    else:
        median = (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
        return median

