def merge_sort(data, plotData, timeTick):
    merge_sort_algo(data, 0, len(data) - 1, plotData, timeTick)

def merge_sort_algo(data, left, right, plotData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, plotData, timeTick)
        merge_sort_algo(data, middle + 1, right, plotData, timeTick)
        merge(data, left, middle, right, plotData, timeTick)

def merge(data, left, middle, right, plotData, timeTick):
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

data = [1, 4, 5, 2, 3, 1, 6, 5, 7, 12, 4, 8]
merge_sort(data, 0, 0)
print(data)
