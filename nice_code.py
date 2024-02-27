## code for plotting
def plotData(data):
    canvas_height = 500
    canvas_width = 950
    
    # Calculate width of each rectangle and spacing
    spacing_bet_rect = 10
    total_spacing = (len(data) + 1) * spacing_bet_rect
    x_width = (canvas_width - total_spacing) / len(data)

    # Adjusted offset to center the rectangles horizontally
    offset = (canvas_width - (x_width * len(data) + total_spacing)) / 2

    # Adjusted height calculation to fit within canvas
    max_data_height = canvas_height - 20  # Adjusted to fit within canvas vertically

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(data):
        x0 = i * x_width + (i + 1) * spacing_bet_rect + offset
        y0 = canvas_height - (height / max(data)) * max_data_height
        x1 = x0 + x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('Arial', 15, 'italic'),
                           fill='red')

  # You can replace the list with any data you want to plot
