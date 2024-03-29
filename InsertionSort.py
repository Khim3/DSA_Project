import time

class InsertionSort:
    def __init__(self, plot_data, time_tick, num_of_swap):
        self.plot_data = plot_data
        self.time_tick = time_tick
        self.num_of_swap = num_of_swap

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                self.plot_data(data, [
                               'yellow' if x == j + 1 else 'red' if x == i else 'blue' for x in range(len(data))])
                time.sleep(self.time_tick)
            if j != i - 1:
                self.num_of_swap.set(str(int(self.num_of_swap.get()) + 1))
            data[j + 1] = key
            self.plot_data(data, ['green' if x == j +
                           1 else 'blue' for x in range(len(data))])
            time.sleep(self.time_tick)
        return data
