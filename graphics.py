from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self):
        self._root = None
        self._no_of_elements = None
        self._speed = None
        self._is_sorting_active = None
        self._selected_algorithm = None
        self.start_button = None
        self.stop_button = None
        self._canvas = None        

    def setup_ui(self):
        self._setup_root()
        self._setup_algorithm_frame()
        self._setup_control_frame()
        self._setup_diagram_frame()
        self._root.mainloop()

    def _setup_root(self):
        # Initialize main window
        root = Tk()
        root.title("Sorting Algorithms Visualizer")
        root.geometry("800x600")
        root.resizable(False, False) # Disable Resizing

        # Configure the grid layout for the root window
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(1, weight=2)
        self._root = root

    def _setup_algorithm_frame(self):
        algorithm_frame = LabelFrame(self._root, text="Algorithms", padx=10, pady=10)
        algorithm_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(N, W, E, S))
        
        algorithm_frame.grid_columnconfigure(0, weight=1)

        algorithm_label = ttk.Label(algorithm_frame, text="Choose the sorting algorithm: ")
        algorithm_label.grid(row=0, column=0, padx=5, pady=5, sticky=(N, W))

        algorithms = ['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort']

        self._selected_algorithm = StringVar(value='Bubble Sort')
        
        # Creating radio buttons for each algorithm
        for row_count, algorithm in enumerate(algorithms, start=1):
            radio_button = ttk.Radiobutton(algorithm_frame, text=algorithm, variable=self._selected_algorithm, value=algorithm)
            radio_button.grid(row=row_count, padx=5, sticky=(N, W))

    def _setup_control_frame(self):
        control_frame = LabelFrame(self._root, text="Controls", padx=10, pady=10)
        control_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(N, W, E, S))
        
        # Configure the grid layout for algorithm frame

        control_frame.grid_columnconfigure(0, weight=1)
        control_frame.grid_columnconfigure(1, weight=1)
        control_frame.grid_columnconfigure(2, weight=1)
        
        self._no_of_elements = IntVar(value=10)
        self._speed = IntVar(value=1)

        no_of_elements_scale = Scale(control_frame, from_=0, to=50, label="No. of Elements: ", length=220, variable=self._no_of_elements, width=10, orient=HORIZONTAL, tickinterval=10)
        no_of_elements_scale.grid(row=0, column=0, sticky=(W, E))
        speed_scale = Scale(control_frame, from_=0, to=2, label="Speed: ", length=220, variable=self._speed, width=10, orient=HORIZONTAL, tickinterval=1)
        speed_scale.grid(row=1, column=0, sticky=(W, E))

        self._is_sorting_active = BooleanVar(value=False)

        self.start_button = ttk.Button(control_frame, text="Start Sorting", command=self.start_sorting)
        self.start_button.grid(row=0, column=2, padx=10, pady=10, sticky=(N, W, E, S))

        self.stop_button = ttk.Button(control_frame, text="Stop Sorting", command=self.stop_sorting, state=DISABLED)
        self.stop_button.grid(row=1, column=2, padx=10, pady=10, sticky=(N, W, E, S))

    def start_sorting(self):
        print(f"Starting {self._selected_algorithm.get()}... {self._no_of_elements.get()}") 
        self._is_sorting_active.set(True)
        self.stop_button.config(state=NORMAL)

    def stop_sorting(self):
        print("Sorting stopped.")
        self._is_sorting_active.set(False)
        self.stop_button.config(state=DISABLED)

    def _setup_diagram_frame(self):
        diagram_frame = LabelFrame(self._root, text="Diagram", padx=10, pady=10)
        diagram_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=(N, W, E, S))
        
        # Configure the grid layout for diagram frame
        diagram_frame.grid_columnconfigure(0, weight=1) 
        diagram_frame.grid_rowconfigure(0, weight=1)

        self._canvas = Canvas(diagram_frame, background="black", width=730, height=170)
        self._canvas.grid(row=0, column=0, sticky=(N, W, E, S))
