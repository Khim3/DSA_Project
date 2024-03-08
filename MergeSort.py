import time

class MergeSort:
    def __init__(self, plot_data, time_tick,num_of_steps):
        self.plot_data = plot_data
        self.time_tick = time_tick
        self.num_of_steps = num_of_steps

    def sort(self, data):
        self.merge_sort(data, 0, len(data) - 1)

    def merge_sort(self, data, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(data) - 1

        if left < right:
            middle = (left + right) // 2
            self.merge_sort(data, left, middle)
            self.merge_sort(data, middle + 1, right)
            self.merge(data, left, middle, right)

    def merge(self, data, left, middle, right):
        self.plot_data(data, self.color_array(len(data), left, middle, right))
        time.sleep(self.time_tick)

        left_part = data[left:middle + 1]
        right_part = data[middle + 1: right + 1]
        left_idx = right_idx = 0

        for data_idx in range(left, right + 1):
            if left_idx < len(left_part) and right_idx < len(right_part):
                if left_part[left_idx] <= right_part[right_idx]:
                    data[data_idx] = left_part[left_idx]
                    left_idx += 1
                else:
                    data[data_idx] = right_part[right_idx]
                    right_idx += 1
            elif left_idx < len(left_part):
                data[data_idx] = left_part[left_idx]
                left_idx += 1
            else:
                data[data_idx] = right_part[right_idx]
                right_idx += 1

        self.plot_data(data, ['green' if left <= x <=
                       right else 'white' for x in range(len(data))])
        time.sleep(self.time_tick)

    def color_array(self, length, left, middle, right):
        color_array = []
        for i in range(length):
            if left <= i <= right:
                color_array.append('yellow')
            else:
                color_array.append('blue')
        return color_array
