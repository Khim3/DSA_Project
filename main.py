import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title('Sorting Visualizer')
root.geometry('1440x700')
root.config(bg='gray')




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
dataLabel = Label(root, text='No. of data: ', font=(
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
minScale = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=200,
                 label='Min Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
minScale.place(x=380, y=50)

# max value
maxValue = Label(root, text='Max Value', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
maxValue.place(x=600, y=50)
maxScale = Scale(root, from_=10, to=100, resolution=5, orient=HORIZONTAL, length=200,
                 label='Max Value', font=('Arial', 15, 'bold'), bg='green', fg='black')
maxScale.place(x=730, y=50)
# sort button
sortButton = Button(root, text='Sort', font=('Arial', 15, 'bold'),
                    relief=SUNKEN, activebackground='green', activeforeground='white', bd=5, width=13,)
sortButton.place(x=1100, y=100)
# scale combobox
speedLabel = Label(root, text='Speed: ', font=(
    'Arial', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)

speedLabel.place(x=600, y=00)
speedMenu = ttk.Combobox(root, height=10, width=15, font=('Arial', 15, 'bold'),
                         values=['Fast', 'Medium', 'Slow'])
speedMenu.current(1)
speedMenu.place(x=735, y=0)

# canvas for visualizing

canvas = Canvas(root, width=950, height=500, bg='black')
canvas.place(x=15, y=150)

root.mainloop()
