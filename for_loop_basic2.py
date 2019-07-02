# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = "big"
    print(list)        
    return list

biggie_size([-1, 3, 5, -5])


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    count = 0
    for i in range(0, len(list), 1):
        if list[i] > 0:
            count += 1
    list[len(list) - 1] = count
    print(list)
    return list

count_positives([-1,1,1,1])


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    print(sum)
    return sum

sum_total([6,3,-2])


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    avg = sum / len(list)
    print(avg)
    return avg

average([1,2,3,4])


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    print(len(list))
    return len(list)

length([37,2,1,-9])


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(list):
    min = list[0]
    for i in range(1, len(list), 1):
        if len(list) < 1:
            return False
        elif list[i] < min:
            min = list[i]
    print(min)
    return min

minimum([37,2,1,-9])
minimum([-29,37,2,1,-9])


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list):
    max = list[0]
    for i in range(1, len(list), 1):
        if len(list) < 1:
            return False
        elif list[i] > max:
            max = list[i]
    print(max)
    return max

maximum([37,2,1,-9])


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    sumTotal = list[0]
    min = list[0]
    max = list[0]
    for i in range(1, len(list), 1):
        sumTotal += list[i]
        if min > list[i]:
            min = list[i]
        if max < list[i]:
            max = list[i]
    average = sumTotal / len(list)
    dict = {'sumTotal': sumTotal, 'average': average, 'minimum': min, 'maximum': max, 'length': len(list)}
    print(dict)
    return dict

ultimate_analysis([1,2,3,4,5,6,7,8])


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reversed(list):
    list = list[::-1]
    print(list)
    return list

reversed([1,2,4,5,6])


def reverse_list(list):
    for i in range(0, int(len(list)/2), 1):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    print(list)
    return list

reverse_list([37,2,1,-9])

