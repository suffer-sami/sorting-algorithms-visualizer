from tkinter import *
from tkinter import ttk

# Initialize main window
root = Tk()
root.title("Sorting Algorithms Visualizer")
root.geometry("800x500")
root.resizable(False, False)

# Configure the grid layout for the root window
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=0)

algoframe = LabelFrame(root, text="Algorithms", padx=10, pady=10)
algoframe.grid(row=0, column=0, padx=10, pady=10, sticky=(N, W, E, S))

ttk.Label(algoframe, text="Choose the sorting algorithm: ").grid(row=0, column=0, sticky=W)

selected_algorithm = StringVar(value='Bubble Sort')
algorithms = ['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort']

# Creating radio buttons for each algorithm
for row_count, algorithm in enumerate(algorithms, start=1):
    ttk.Radiobutton(algoframe, text=algorithm, variable=selected_algorithm, value=algorithm).grid(row=row_count, sticky=W)

selection_frame = LabelFrame(root, text="Selection", padx=10, pady=10)
selection_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(N, W, E, S))


no_of_elements = IntVar(value=10)
Scale(selection_frame, from_=0, to=200, label="No. of Elements: ", length=220, variable=no_of_elements, width=10, orient=HORIZONTAL).grid(row=0, column=0, sticky=(W, E))
speed = IntVar(value=1)
Scale(selection_frame, from_=0, to=3, label="Speed: ", length=220, variable=speed, width=10, orient=HORIZONTAL).grid(row=1, column=0, sticky=(W, E))



diagram_frame = LabelFrame(root, text="Diagram", padx=10, pady=10)
diagram_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=(N, W, E, S))

ttk.Label(diagram_frame, text="Visualization of the algorithm will appear here.").grid(row=0, column=0, sticky=(N, W, E, S))

def start_sorting():
    print(f"Starting {selected_algorithm.get()}... {no_of_elements.get()}") 

start_button = ttk.Button(root, text="Start Sorting", command=start_sorting)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
