import time


class BubbleSort:
    def __init__(self, plot_data, time_tick):
        self.plot_data = plot_data
        self.time_tick = time_tick

    def bubble_sort(self, data):
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.plot_data(
                        data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                    time.sleep(self.time_tick)
        self.plot_data(data, ['blue' for x in range(len(data))])
