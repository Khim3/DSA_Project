import time

class BubbleSort:
    def __init__(self, plot_data, time_tick, num_of_swap):
        self.plot_data = plot_data
        self.time_tick = time_tick
        self.num_of_swap = num_of_swap
        self.swap_count = 0

    def bubble_sort(self, data):
        self.swap_count = 0
        for i in range(len(data) - 1):
            swapped = False
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.swap_count += 1
                    self.plot_data(
                        data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                    self.num_of_swap.set(str(self.swap_count))
                    time.sleep(self.time_tick)
                    swapped = True
            if not swapped:
                break
        self.plot_data(data, ['blue' for x in range(len(data))])
