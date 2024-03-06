import time


class ShellSort:
    def __init__(self, plot_data, time_tick):
        self.plot_data = plot_data
        self.time_tick = time_tick

    def shell_sort(self, data):
        n = len(data)
        gap = n // 2
        while (gap > 0):
            for i in range(gap, n):
                temp = data[i]
                j = i
                while (j >= gap and data[j - gap] > temp):
                    data[j] = data[j-gap]
                    j -= gap
                data[j] = temp
                self.plot_data(data, [
                               'yellow' if x == j else 'red' if x == i else 'blue' for x in range(len(data))])
                time.sleep(self.time_tick)
            gap //= 2
        self.plot_data(data, ['green' for _ in range(len(data))])
        return data
