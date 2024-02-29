import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
# create the app frame
root = Tk()
root.title('Sorting Visualizer')
root.geometry('1440x700')
root.config(bg='gray')

# Function
# Generate data
def Generator():
    global data
    data = [random.randint(minScale.get(), maxScale.get())
            for _ in range(int(dataMenu.get()))]

    plotData(data, ['red' for x in range(len(data))])

# plot the data
def plotData(data, colorArr):
    canvas.delete('all')
    canvas_height = 500
    canvas_width = 950

    # Calculate width of each rectangle and spacing
    spacing_bet_rect = 10
    total_spacing = (len(data) + 1) * spacing_bet_rect
    x_width = (canvas_width - total_spacing) / len(data)

    # Adjusted offset to center the rectangles horizontally
    offset = (canvas_width - (x_width * len(data) + total_spacing)) / 2

    # Adjusted height calculation to fit within canvas
    max_data_height = canvas_height - 40  # Adjusted to fit within canvas vertically

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(data):
        x0 = i * x_width + (i + 1) * spacing_bet_rect + offset
        y0 = canvas_height - (height / max(data)) * max_data_height
        x1 = x0 + x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArr[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('Arial', 18, 'bold'),
                           fill='red')
    root.update_idletasks()
# sort algorithm
def StartAlgorithm():
    global data
    bubble_sort(data, plotData, float(speedMenu.get()))


# Create algorithm combobox
selected_algorithm = StringVar()
algoLabel = Label(root, text='Algorithm: ', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
algoLabel.place(x=0, y=0)

algoMenu = ttk.Combobox(root, height=10, width=20, font=('Arial', 15, 'bold'), textvariable=selected_algorithm,
                        values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Heap Sort', 'Shell Sort'])


algoMenu.place(x=130, y=0)
algoMenu.current(0)
# Generate random data
random_generate = Button(root, text='Generate data', font=('Arial', 15, 'bold'),
                         relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=Generator)
random_generate.place(x=1100, y=50)
# create a combobox for choose number of data
dataLabel = Label(root, text='Size : ', font=(
    'Arial', 15, 'italic'), bg='green', width=15, fg='black', relief=GROOVE, bd=5)
dataLabel.place(x=0, y=50)

dataMenu = ttk.Combobox(root, height=10, width=15, font=('Arial', 15, 'bold'),
                        values=[10, 15, 20, 25, 30])
dataMenu.current(0)
dataMenu.place(x=2, y=85)

# create scale for choosing max and min values
# min value
minValueLabel = Label(root, text='Min Value', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
minValueLabel.place(x=250, y=50)
minScale = Scale(root, from_=1, to=9, orient=HORIZONTAL, length=200,
                 label='Min Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
minScale.place(x=380, y=50)

# max value
maxValueLabel = Label(root, text='Max Value', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
maxValueLabel.place(x=600, y=50)
maxScale = Scale(root, from_=10, to=100, resolution=5, orient=HORIZONTAL, length=200,
                 label='Max Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
maxScale.place(x=730, y=50)
# sort button
sortButton = Button(root, text='Sort', font=('Arial', 15, 'bold'),
                    relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13, command=StartAlgorithm)
sortButton.place(x=1100, y=100)
# scale combobox
speedLabel = Label(root, text='Speed: ', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)

speedLabel.place(x=600, y=00)
speedMenu = ttk.Combobox(root, height=10, width=15, font=('Arial', 15, 'bold'),
                         values=[.25, .5, .75])
speedMenu.current(1)
speedMenu.place(x=735, y=0)

# canvas for visualizing
canvas = Canvas(root, width=950, height=500, bg='black')
canvas.place(x=15, y=150)
print(type(speedMenu.get()))
root.mainloop()
