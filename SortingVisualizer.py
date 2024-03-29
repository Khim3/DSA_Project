import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
import random
import time
from BubbleSort import BubbleSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from ShellSort import ShellSort
import textwrap


class SortingVisualizer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        self.root = root
        self.root.title('Sorting Visualizer')
        self.root.geometry('1400x720')
        self.root.config(bg='gray')
        self.data = []
        self.create_widgets()

    @staticmethod
    def get_instance(root=None):
        if not SortingVisualizer._instance:
            SortingVisualizer._instance = SortingVisualizer(root)
        return SortingVisualizer._instance

    def create_widgets(self):
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Segoe UI', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Select one', 'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Shell Sort', 'Merge Sort'])
        self.algoMenu.place(x=125, y=8)
        self.algoMenu.current(0)
       # self.algoMenu.current(randint(0, 5))

        # Data generation
        self.random_generate = Button(self.root, text='Generate data', font=('Segoe UI', 15, 'bold'),
                                      relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.generator)
        self.random_generate.place(x=975, y=25)

        # Data size selection
        self.dataLabel = Label(self.root, text='Size ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.dataLabel.place(x=2, y=50)

        self.dataMenu = ttk.Combobox(self.root, height=10, width=8, font=('Segoe UI', 15, 'bold'),
                                     values=[10, 15, 20, 25, 30])
        dataList = [10, 15, 20, 25, 30]
        random_value = random.choice(dataList)
        self.dataMenu.current(dataList.index(random_value))
        self.dataMenu.place(x=2, y=90)

        # Min value scale
        self.minValueLabel = Label(self.root, text='Min Value', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.minValueLabel.place(x=150, y=50)

        self.minScale = Scale(self.root, from_=1, to=9, orient=HORIZONTAL, length=150,
                              label='Min Value', font=('Segoe UI', 15, 'bold'), bg='green', fg='black')
        self.minScale.place(x=274, y=50)

        # Max value scale
        self.maxValueLabel = Label(self.root, text='Max Value', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.maxValueLabel.place(x=470, y=50)

        self.maxScale = Scale(self.root, from_=10, to=100, resolution=10, orient=HORIZONTAL, length=150,
                              label='Max Value', font=('Segoe UI', 15, 'bold'), bg='green', fg='black')
        self.maxScale.place(x=595, y=50)

        # Sort button
        self.sortButton = Button(self.root, text='Sort', font=('Segoe UI', 15, 'bold'),
                                 relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.start_algorithm)
        self.sortButton.place(x=975, y=75)

        # Speed selection
        self.speedLabel = Label(self.root, text='Speed: ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.speedLabel.place(x=350, y=5)

        self.speedMenu = ttk.Combobox(self.root, height=10, width=10, font=('Segoe UI', 15, 'bold'),
                                      values=[.1, .25, .5, .75, 1])
        self.speedMenu.current(0)
        self.speedMenu.place(x=475, y=8)

        # no. of swaps
        self.swapsLabel = Label(self.root, text='No. of Swaps: ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.swapsLabel.place(x=620, y=5)
        self.numOfSwap = StringVar()
        self.numOfSwap.set('0')
        self.text = Label(self.root, bg='gray', textvariable=self.numOfSwap, font=(
            'Segoe UI', 15, 'bold'))
        self.text.place(x=780, y=8)
        # time
        self.timeLabel = Label(self.root, text='Time', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.timeLabel.place(x=760, y=50)
        self.time = StringVar()
        self.time.set('0')
        self.timeDisplay = Label(self.root, bg='gray', textvariable=self.time, font=(
            'Segoe UI', 15, 'bold'))
        self.timeDisplay.place(x=770, y=90)

        # Canvas for visualization
        self.canvas = Canvas(self.root, width=920, height=540, bg='black')
        self.canvas.place(x=15, y=145)
        # Canvas for description
        self.canvas_desc = Canvas(self.root, width=450, height=540, bg='black')
        self.canvas_desc.place(x=930, y=145)

    def generator(self):
        self.data = [random.randint(self.minScale.get(), self.maxScale.get())
                     for _ in range(int(self.dataMenu.get()))]

        self.plot_data(self.data, ['red' for _ in range(len(self.data))])
        algorithm = self.algoMenu.get()
        if algorithm == 'Merge Sort':
            self.numOfSwap.set('NA')
        else:
            self.numOfSwap.set('0')
        self.canvas_desc.delete('all')
        description = ''
        if algorithm == 'Bubble Sort':
            description = "Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted."
        elif algorithm == 'Merge Sort':
            description = "Merge Sort is a divide-and-conquer algorithm that splits an array into two halves, recursively sorts them, and then merges them. This method results in a stable, efficient sort"
        elif algorithm == 'Quick Sort':
            description = "Quick Sort is an efficient sorting algorithm that uses divide-and-conquer principles. It partitions an array and recursively sorts the sub-arrays, achieving high performance"
        elif algorithm == 'Selection Sort':
            description = "This is a simple comparison-based algorithm. It divides the input into a sorted and an unsorted region, and repeatedly picks the smallest element from the unsorted region and moves it to the sorted region."
        elif algorithm == 'Insertion Sort':
            description = "Insertion Sort is a simple, comparison-based algorithm. It builds a sorted array one item at a time, making it efficient for small data sets and substantially sorted lists."
        elif algorithm == 'Shell Sort':
            description = "This is a generalized version of insertion sort. It sorts elements at specific intervals, and gradually reduces the interval to perform a final insertion sort. It’s more efficient than simple insertion sort."
        elif algorithm == 'Quick Sort':
            description = "This is a highly efficient sorting algorithm that employs divide-and-conquer principles. It selects a ‘pivot’ element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted."
        # wrap the description
        wrapper = textwrap.TextWrapper(width=50)
        wrapped_description = wrapper.fill(description)
        self.canvas_desc.create_text(10, 10, anchor=NW, text=wrapped_description, font=(
            'Segoe UI', 14, 'bold'), fill='orange')

    def plot_data(self, data, color_arr):
        self.canvas.delete('all')
        canvas_height = 540
        canvas_width = 920

        spacing_bet_rect = 10
        total_spacing = (len(data) + 1) * spacing_bet_rect
        x_width = (canvas_width - total_spacing) / len(data)

        offset = (canvas_width - (x_width * len(data) + total_spacing)) / 2

        max_data_height = canvas_height - 40

        for i, height in enumerate(data):
            x0 = i * x_width + (i + 1) * spacing_bet_rect + offset
            y0 = canvas_height - (height / max(data)) * max_data_height
            x1 = x0 + x_width
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_arr[i])
            self.canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('Segoe UI', 15, 'bold'),
                                    fill='blue')
        self.root.update_idletasks()

    def start_algorithm(self):
        global start_time
        start_time = time.time()
        if (self.algoMenu.get() == 'Bubble Sort'):
            bubble_sorter = BubbleSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            bubble_sorter.bubble_sort(self.data)
        elif (self.algoMenu.get() == 'Selection Sort'):
            selection_sorter = SelectionSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            selection_sorter.selection_sort(self.data)
        elif (self.algoMenu.get() == 'Insertion Sort'):
            insertion_sorter = InsertionSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            insertion_sorter.insertion_sort(self.data)
        elif (self.algoMenu.get() == 'Merge Sort'):
            merge_sorter = MergeSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            merge_sorter.merge_sort(self.data)
        elif (self.algoMenu.get() == 'Shell Sort'):
            shell_sorter = ShellSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            shell_sorter.shell_sort(self.data)
        elif (self.algoMenu.get() == 'Quick Sort'):
            quick_sorter = QuickSort(
                self.plot_data, float(self.speedMenu.get()), self.numOfSwap)
            quick_sorter.quick_sort(self.data, 0, len(self.data)-1)
        self.plot_data(self.data, ['green' for _ in range(len(self.data))])
        self.end_time = time.time()
        global end_time
        end_time = time.time()
        total_time = end_time - start_time
        self.time.set(f"{total_time:.2f} seconds")


if __name__ == "__main__":
    root = Tk()
    app = SortingVisualizer.get_instance(root)
    root.mainloop()
