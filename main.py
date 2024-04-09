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


# string functions
def text_contains_word(text, word):
    for letter in word:
        if letter in text:
            return True
    return False

if __name__ == '__main__':
    print(text_contains_word("Hello world", "world"))
    print(subtract(10, 20))
    print(add(0, 20))
    print(get_min([10, 11, 13, 15, 0, -20]))
    print(get_max([10, 11, 13, 15, 0, -20]))
    print(get_median([10, 11, 13, 15, 0, -20]))
