import time

class QuickSort:
    def __init__(self, plot_data, time_tick):
        self.plot_data = plot_data
        self.time_tick = time_tick

    def partition(self, data, head, tail):
        border = head
        pivot = data[tail]
        self.plot_data(data, self.color_array(len(data), head, tail, border, border))
        time.sleep(self.time_tick)
        
        for i in range(head, tail):
            if data[i] < pivot:
                self.plot_data(data, self.color_array(len(data), head, tail, border, i, True))
                time.sleep(self.time_tick)
                data[border], data[i] = data[i], data[border]
                border += 1
            self.plot_data(data, self.color_array(len(data), head, tail, border, i))
            time.sleep(self.time_tick)
        
        self.plot_data(data, self.color_array(len(data), head, tail, border, tail, True))
        time.sleep(self.time_tick)
        data[border], data[tail] = data[tail], data[border]
        return border

    def quick_sort(self, data, head, tail):
        if head < tail:
            partition_idx = self.partition(data, head, tail)
            self.quick_sort(data, head, partition_idx - 1)
            self.quick_sort(data, partition_idx + 1, tail)

    def color_array(self, data_length, head, tail, border, current_idx, is_swapping=False):
        color_array = []
        for i in range(data_length):
            if head <= i <= tail:
                color_array.append('blue')
            else:
                color_array.append('white')
            if i == tail:
                color_array.append('red')
            elif i == border:
                color_array.append('orange')
            elif i == current_idx:
                color_array.append('yellow')

            if is_swapping:
                if i == border or i == current_idx:
                    color_array[i] = 'green'

        return color_array
