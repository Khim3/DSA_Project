import time

class QuickSort:
    def __init__(self, plot_data, time_tick, num_of_swap):
        self.plot_data = plot_data
        self.time_tick = time_tick
        self.num_of_swap = num_of_swap

    def partition(self, data, head, tail):
        border = head
        pivot = data[tail]
        self.plot_data(data, self.color_array(
            len(data), head, tail, border, border))
        time.sleep(self.time_tick)

        for i in range(head, tail):
            if data[i] < pivot:
                self.plot_data(data, self.color_array(
                    len(data), head, tail, border, i, True))
                time.sleep(self.time_tick)
                data[border], data[i] = data[i], data[border]
                border += 1
                self.num_of_swap.set(str(int(self.num_of_swap.get()) + 1))  # Increment swap count
            self.plot_data(data, self.color_array(
                len(data), head, tail, border, i))
            time.sleep(self.time_tick)

        self.plot_data(data, self.color_array(
            len(data), head, tail, border, tail, True))
        time.sleep(self.time_tick)
        data[border], data[tail] = data[tail], data[border]
        return border

    def quick_sort(self, data, head, tail):
        if head < tail:
            partition_idx = self.partition(data, head, tail)
            self.quick_sort(data, head, partition_idx - 1)
            self.quick_sort(data, partition_idx + 1, tail)

    def color_array(self, data_length, head, tail, border, current_idx, is_swapping=False):
        color_array = ['blue' for _ in range(data_length)]
        color_array[head:tail + 1] = ['blue' for _ in range(tail - head + 1)]
        color_array[border] = 'orange'
        color_array[current_idx] = 'yellow'
        if is_swapping:
            color_array[border] = 'green'
            color_array[current_idx] = 'green'
        color_array[tail] = 'red'
        return color_array
