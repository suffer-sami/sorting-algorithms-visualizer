import random
import time
from tkinter import *
from tkinter import ttk, messagebox
from bars import State, Bar
from sorter import Sorter

class Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Sorting Algorithms Visualizer")
        self.__root.resizable(False, False)
        self.__root.geometry("800x600")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.bind("<Configure>", self.draw_bars)
        self.__algorithm_list =  ['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort']
        self.__selected_algorithm = StringVar(value='Bubble Sort')
        self.__no_of_elements = IntVar(value=30)
        self._speed = IntVar(value=1)
        self.is_sorting_active = BooleanVar(value=False)
        self.__start_button = None
        self.__stop_button = None
        self.__no_of_elements_scale = None
        self.__canvas = None
        self.__bars = []
        self.__running = False
        self.__fill_colors = {
            State.UNSORTED: "white",
            State.BEING_SORTED: "SkyBlue3",
            State.SORTED: "spring green",
            State.PIVOT: "dark violet"
        }
        self.sorter = Sorter(self)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def __setup_root_grid(self):
        # Configure the grid layout for the root window
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_rowconfigure(1, weight=2)

    def __setup_algorithm_frame(self):
        algorithm_frame = LabelFrame(self.__root, text="Algorithms", padx=10, pady=10)
        algorithm_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(N, W, E, S))
        
        algorithm_frame.grid_columnconfigure(0, weight=1)

        algorithm_label = ttk.Label(algorithm_frame, text="Choose the sorting algorithm: ")
        algorithm_label.grid(row=0, column=0, padx=5, pady=5, sticky=(N, W))
        
        # Creating radio buttons for each algorithm
        for row_count, algorithm in enumerate(self.__algorithm_list, start=1):
            radio_button = ttk.Radiobutton(algorithm_frame, text=algorithm, variable=self.__selected_algorithm, value=algorithm)
            radio_button.grid(row=row_count, padx=5, pady=1, sticky=(N, W))

    def __setup_control_frame(self):
        control_frame = LabelFrame(self.__root, text="Controls", padx=10, pady=10)
        control_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(N, W, E, S))
        
        # Configure the grid layout for algorithm frame
        control_frame.grid_columnconfigure(0, weight=1)
        control_frame.grid_columnconfigure(1, weight=1)
        control_frame.grid_columnconfigure(2, weight=1)

        self.__no_of_elements_scale = Scale(control_frame, from_=10, to=50, label="No. of Elements: ", length=220, variable=self.__no_of_elements, width=10, orient=HORIZONTAL, tickinterval=10)
        self.__no_of_elements_scale.grid(row=0, column=0, sticky=(W, E))
        speed_scale = Scale(control_frame, from_=1, to=5, label="Speed: ", length=220, variable=self._speed, width=10, orient=HORIZONTAL, tickinterval=1)
        speed_scale.grid(row=1, column=0, sticky=(W, E))

        self.__start_button = Button(control_frame, text="Start Sorting", command=self.__start_sorting)
        self.__start_button.grid(row=0, column=2, padx=10, pady=10, sticky=(N, W, E, S))

        self.__stop_button = Button(control_frame, text="Stop Sorting", command=self.__stop_sorting, state=DISABLED)
        self.__stop_button.grid(row=1, column=2, padx=10, pady=10, sticky=(N, W, E, S))

    def draw_bars(self, event=None):
        if not self.__bars:
            return
        self.__canvas.delete("all")
        margin = 50
        canvas_width = self.__canvas.winfo_width()
        canvas_height = self.__canvas.winfo_height()
        bar_width = (canvas_width - 2 * margin) // len(self.__bars)
        current_x = margin
        height_with_margin = canvas_height - 2 * margin
        for bar in self.__bars:
            x1 = current_x
            y1 = height_with_margin - height_with_margin * (bar.val / 100) + margin
            x2 = x1 + bar_width
            y2 = canvas_height - margin
            self.__canvas.create_rectangle(current_x, y1, x2, y2, fill=self.__fill_colors[bar.state])
            current_x = x2

    def __start_sorting(self):
        self.is_sorting_active.set(True)
        self.__bars = [Bar(i) for i in range(1, 100, 100 // self.__no_of_elements.get())]
        random.shuffle(self.__bars)
        self.draw_bars()
        self.__start_button.config(state=DISABLED)
        self.__stop_button.config(state=NORMAL)
        self.__no_of_elements_scale.config(state=DISABLED)
        self.__sort_bars()

    def __sort_bars(self):
        selected_algorithm = self.__selected_algorithm.get()

        if selected_algorithm in self.__algorithm_list:
            if selected_algorithm == "Bubble Sort":
                self.sorter.bubble_sort(self.__bars)
            elif selected_algorithm == "Selection Sort":
                self.sorter.selection_sort(self.__bars)
            elif selected_algorithm == "Quick Sort":
                self.sorter.quick_sort(self.__bars)
            elif selected_algorithm == "Merge Sort":
                self.sorter.merge_sort(self.__bars)
            elif selected_algorithm == "Insertion Sort":
                self.sorter.insertion_sort(self.__bars)
        else:
            self.__show_message("Please select valid sorting algorithm")

        self.__stop_sorting()

    def __show_message(self, message):
        messagebox.showinfo("Message",  message)

    def __stop_sorting(self):
        self.is_sorting_active.set(False)
        self.__start_button.config(state=NORMAL)
        self.__stop_button.config(state=DISABLED)
        self.__no_of_elements_scale.config(state=NORMAL)

    def __setup_diagram_frame(self):
        diagram_frame = LabelFrame(self.__root, text="Diagram", padx=10, pady=10)
        diagram_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=(N, W, E, S))
        
        # Configure the grid layout for diagram frame
        diagram_frame.grid_columnconfigure(0, weight=1) 
        diagram_frame.grid_rowconfigure(0, weight=1)

        self.__canvas = Canvas(diagram_frame, background="black")
        self.__canvas.grid(row=0, column=0, sticky=(N, W, E, S))

    def setup_ui(self):
        self.__setup_root_grid()
        self.__setup_algorithm_frame()
        self.__setup_control_frame()
        self.__setup_diagram_frame()

    def close(self):
        self.__running = False
