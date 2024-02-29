import time

def partition(data, head, tail, plotData, timeTick):
    border = head
    pivot = data[tail]
    
    for i in range(head, tail):
        if data[i] < pivot:
            data[border], data[i] = data[i], data[border]
            border += 1
    data[border] , data[tail] = data[tail], data[border]
   
    return border
def quick_sort(data, head, tail, plotData, timeTick):
    if head < tail:
        partitionIdx = partition(data,head, tail, plotData, timeTick) 
        ## left partition
        quick_sort(data, head, partitionIdx - 1, plotData, timeTick)
        ## right partition
        quick_sort(data, partitionIdx + 1, tail, plotData, timeTick)
 
   
data = [1,4,6,1,2,3,9,5,3,7,5,8]
quick_sort(data, 0, len(data) -1,0,0)

print(data)