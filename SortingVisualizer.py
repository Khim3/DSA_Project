import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
import random
from BubbleSort import BubbleSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from ShellSort import ShellSort


class SortingVisualizer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if not hasattr(self, 'initialized'):
            self.root = root
            self.root.title('Sorting Visualizer')
            self.root.geometry('1400x720')
            self.root.config(bg='gray')
            self.data = []
            self.create_widgets()
            self.initialized = True

    @staticmethod
    def get_instance(root=None):
        if not SortingVisualizer._instance:
            SortingVisualizer._instance = SortingVisualizer(root)
        return SortingVisualizer._instance

    def create_widgets(self):
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Arial', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Shell Sort', 'Merge Sort'])
        self.algoMenu.place(x=132, y=8)
       # self.algoMenu.current(0)
        self.algoMenu.current(randint(0, 5))

        # Data generation
        self.random_generate = Button(self.root, text='Generate data', font=('Arial', 15, 'bold'),
                                      relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.generator)
        self.random_generate.place(x=975, y=25)

        # Data size selection
        self.dataLabel = Label(self.root, text='Size ', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.dataLabel.place(x=2, y=50)

        self.dataMenu = ttk.Combobox(self.root, height=10, width=10, font=('Arial', 15, 'bold'),
                                     values=[10, 15, 20, 25, 30])
        dataList = [10, 15, 20, 25, 30]
        random_value = random.choice(dataList)
        self.dataMenu.current(dataList.index(random_value))
        self.dataMenu.place(x=2, y=85)

        # Min value scale
        self.minValueLabel = Label(self.root, text='Min Value', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.minValueLabel.place(x=150, y=50)

        self.minScale = Scale(self.root, from_=1, to=9, orient=HORIZONTAL, length=150,
                              label='Min Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
        self.minScale.place(x=280, y=50)

        # Max value scale
        self.maxValueLabel = Label(self.root, text='Max Value', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.maxValueLabel.place(x=470, y=50)

        self.maxScale = Scale(self.root, from_=10, to=100, resolution=5, orient=HORIZONTAL, length=150,
                              label='Max Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
        self.maxScale.place(x=600, y=50)

        # Sort button
        self.sortButton = Button(self.root, text='Sort', font=('Arial', 15, 'bold'),
                                 relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.start_algorithm)
        self.sortButton.place(x=975, y=75)

        # Speed selection
        self.speedLabel = Label(self.root, text='Speed: ', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.speedLabel.place(x=350, y=5)

        self.speedMenu = ttk.Combobox(self.root, height=10, width=10, font=('Arial', 15, 'bold'),
                                      values=[.25, .5, .75, 1])
        self.speedMenu.current(1)
        self.speedMenu.place(x=482, y=8)

        # no. of swaps
        self.swapsLabel = Label(self.root, text='No. of Swaps: ', font=(
            'Arial', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.swapsLabel.place(x=620, y=5)
        self.numOfSwap = StringVar()
        self.numOfSwap.set('0')
        self.text = Label(self.root, bg='gray', textvariable=self.numOfSwap, font=(
            'Arial', 15, 'bold'))
        self.text.place(x=780, y=8)

        # time
        self.timeLabel = Label(self.root, text='Time', font=(
            'Arial', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.timeLabel.place(x=760, y=50)

        # Canvas for visualization
        self.canvas = Canvas(self.root, width=920, height=540, bg='black')
        self.canvas.place(x=15, y=145)

    def generator(self):
        self.data = [random.randint(self.minScale.get(), self.maxScale.get())
                     for _ in range(int(self.dataMenu.get()))]

        self.plot_data(self.data, ['red' for _ in range(len(self.data))])
        if (self.algoMenu.get() == 'Merge Sort'):
            self.numOfSwap.set('NA')
        else:   
            self.numOfSwap.set('0')

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
            self.canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('Arial', 15, 'bold'),
                                    fill='blue')
        self.root.update_idletasks()

    def start_algorithm(self):
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


if __name__ == "__main__":
    root = Tk()
    app = SortingVisualizer.get_instance(root)
    root.mainloop()
