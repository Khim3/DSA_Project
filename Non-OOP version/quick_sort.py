import time

def partition(data, head, tail, plot_data, timeTick):
    border = head
    pivot = data[tail]
    
    plot_data(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for i in range(head, tail):
        if data[i] < pivot:
            plot_data(data, colorArray(len(data), head, tail, border,i,True))
            time.sleep(timeTick)
            data[border], data[i] = data[i], data[border]
            border += 1
        plot_data(data, colorArray(len(data), head, tail, border, i))
        time.sleep(timeTick)
    ## swapping data
    plot_data(data, colorArray(len(data), head, tail, border,tail, True))
    time.sleep(timeTick)
    data[border] , data[tail] = data[tail], data[border]
    return border
def quick_sort(data, head, tail, plot_data, timeTick):
    if head < tail:
        partitionIdx = partition(data,head, tail, plot_data, timeTick) 
        ## left partition
        quick_sort(data, head, partitionIdx - 1, plot_data, timeTick)
        ## right partition
        quick_sort(data, partitionIdx + 1, tail, plot_data, timeTick)
 
def colorArray(dataLenth, head, tail, border, currentIdx, isSwapping = False):
    colorArray =[]
    for i in range(dataLenth):
        if i >= head and i <= tail:
            colorArray.append('blue')
        else:
            colorArray.append('white')
        if i == tail:
            colorArray.append('red')
        elif i == border:
            colorArray.append('orange')
        elif i == currentIdx:
            colorArray.append('yellow')
        
        if isSwapping:
            if i == border or i == currentIdx:
                colorArray[i] ='green'
                
    return colorArray