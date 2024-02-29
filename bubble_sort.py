import time

def bubble_sort(data, plotData, timeTick):
    
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                plotData(data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    plotData(data, ['blue' for  x in range(len(data))])
