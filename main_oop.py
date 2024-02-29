import tkinter as tk
from tkinter import ttk
import random
from bubble_sort import bubble_sort

class SortingVisualizer(tk.Tk):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        super().__init__()

        self.title('Sorting Visualizer')
        self.geometry('1440x700')
        self.config(bg='gray')

        self.selected_algorithm = tk.StringVar()

        # Algorithm ComboBox
        algo_label = tk.Label(self, text='Algorithm: ', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=tk.GROOVE, bd=5)
        algo_label.place(x=0, y=0)

        algo_menu = ttk.Combobox(self, height=10, width=20, font=('Arial', 15, 'bold'), textvariable=self.selected_algorithm,
                                values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Heap Sort', 'Shell Sort'])
        algo_menu.place(x=130, y=0)
        algo_menu.current(0)

        # Random Data Button
        random_generate = tk.Button(self, text='Generate data', font=('Arial', 15, 'bold'),
                                    relief=tk.SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.generate_data)
        random_generate.place(x=1100, y=50)

        # Size ComboBox
        data_label = tk.Label(self, text='Size : ', font=(
            'Arial', 15, 'italic'), bg='green', width=15, fg='black', relief=tk.GROOVE, bd=5)
        data_label.place(x=0, y=50)

        self.data_menu = ttk.Combobox(self, height=10, width=15, font=('Arial', 15, 'bold'),
                                      values=[10, 15, 20, 25, 30])
        self.data_menu.current(0)
        self.data_menu.place(x=2, y=85)

        # Min Value Scale
        min_value_label = tk.Label(self, text='Min Value', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=tk.GROOVE, bd=5)
        min_value_label.place(x=250, y=50)

        self.min_scale = tk.Scale(self, from_=1, to=9, orient=tk.HORIZONTAL, length=200,
                                  label='Min Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
        self.min_scale.place(x=380, y=50)

        # Max Value Scale
        max_value_label = tk.Label(self, text='Max Value', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=tk.GROOVE, bd=5)
        max_value_label.place(x=600, y=50)

        self.max_scale = tk.Scale(self, from_=10, to=100, resolution=5, orient=tk.HORIZONTAL, length=200,
                                  label='Max Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
        self.max_scale.place(x=730, y=50)

        # Sort Button
        sort_button = tk.Button(self, text='Sort', font=('Arial', 15, 'bold'),
                                relief=tk.SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=self.start_algorithm)
        sort_button.place(x=1100, y=100)

        # Speed ComboBox
        speed_label = tk.Label(self, text='Speed: ', font=(
            'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=tk.GROOVE, bd=5)
        speed_label.place(x=600, y=00)

        self.speed_menu = ttk.Combobox(self, height=10, width=15, font=('Arial', 15, 'bold'),
                                        values=[.25, .5, .75])
        self.speed_menu.current(1)
        self.speed_menu.place(x=735, y=0)

        # Canvas
        self.canvas = tk.Canvas(self, width=950, height=500, bg='black')
        self.canvas.place(x=15, y=150)

    def generate_data(self):
        size = int(self.data_menu.get())
        min_val = self.min_scale.get()
        max_val = self.max_scale.get()
        data = [random.randint(min_val, max_val) for _ in range(size)]
        self.plot_data(data, ['red' for _ in range(len(data))])

    def plot_data(self, data, color_arr):
        self.canvas.delete('all')
        canvas_height = 500
        canvas_width = 950
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
            self.canvas.create_text(x0 + x_width / 2, y0 + (y1 - y0) / 2, anchor='center', text=str(data[i]),
                                    font=('Arial', 18, 'bold'), fill='red')
        self.update_idletasks()

    def start_algorithm(self):
        algorithm = self.selected_algorithm.get()
        data = [random.randint(self.min_scale.get(), self.max_scale.get()) for _ in range(int(self.data_menu.get()))]
        if algorithm == 'Bubble Sort':
            bubble_sort(data, self.plot_data, float(self.speed_menu.get()))


if __name__ == "__main__":
    app = SortingVisualizer()
    app.mainloop()
