import time


class SelectionSort:
    def __init__(self, plot_data, time_tick):
        self.plot_data = plot_data
        self.time_tick = time_tick

    def selection_sort(self, data):
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.plot_data(
                data, ['yellow' if x == min_idx or x == i else 'red' for x in range(len(data))])
            time.sleep(self.time_tick)
        self.plot_data(data, ['green' for _ in range(len(data))])
        return data
