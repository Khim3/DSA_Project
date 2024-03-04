# import the needed libraries
import time

def merge_sort(data, plot_data, timeTick):
    merge_sort_algo(data, 0, len(data) - 1, plot_data, timeTick)

def merge_sort_algo(data, left, right, plot_data, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, plot_data, timeTick)
        merge_sort_algo(data, middle + 1, right, plot_data, timeTick)
        merge(data, left, middle, right, plot_data, timeTick)

def merge(data, left, middle, right, plot_data, timeTick):
    plot_data (data, colorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    
    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]
    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
            
    plot_data (data, ['green' if x >= left and x<= right else 'white' for x in range(len(data))])
    time.sleep(timeTick)


def colorArray(length, left, middle, right):
    colorArray = []
    for i in range(length):
        if i >= left and i <= right:
            if i>= left and i <= right: 
                colorArray.append('yellow')
                
            else:
                colorArray.append('orange')
        else:
            colorArray.append('blue')
    return colorArray
            

