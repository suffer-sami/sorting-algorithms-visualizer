from time import sleep
from bars import State
from sys import exit

class Sorter:
    def __init__(self, win=None) -> None:
        self._win = win

    def _animate(self):
        if self._win is not None:
            if not self._win.is_sorting_active.get():
                exit(0)
            self._win.draw_bars()
            self._win.redraw()
            sleep(0.01/self._win._speed.get())

    def bubble_sort(self, bars):
        for i in range(len(bars)):
            for j in range(0, len(bars) - i - 1):
                bars[j].state = State.BEING_SORTED
                bars[j + 1].state = State.BEING_SORTED
                self._animate()
                if bars[j] > bars[j + 1]:
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                bars[j].state = State.UNSORTED

            bars[len(bars) - i - 1].state = State.SORTED
            self._animate()

        bars[0].state = State.SORTED
        self._animate()

    def selection_sort(self, bars):
        for step in range(len(bars)):
            min_idx = step
            bars[min_idx].state = State.BEING_SORTED
            self._animate()

            for i in range(step + 1, len(bars)):
                bars[i].state = State.BEING_SORTED
                self._animate()

                if bars[i] < bars[min_idx]:
                    bars[min_idx].state = State.UNSORTED
                    min_idx = i
                    bars[min_idx].state = State.BEING_SORTED

                bars[i].state = State.UNSORTED
                self._animate()

            bars[step], bars[min_idx] = bars[min_idx], bars[step]
            bars[min_idx].state = State.UNSORTED
            bars[step].state = State.SORTED

            self._animate()

    def quick_sort(self, bars, low, high):
        if low < high:
            pivot = self.__partition(bars, low, high)
            self.quick_sort(bars, low, pivot - 1)
            self.quick_sort(bars, pivot + 1, high)

            if low == 0 and high == len(bars) - 1:
                for bar in bars:
                    bar.state = State.SORTED
                self._animate()

    def __partition(self, bars, low, high):
        pivot = bars[high]
        pivot.state = State.PIVOT
        self._animate()
        i = low - 1

        for j in range(low, high):
            bars[j].state = State.BEING_SORTED
            self._animate()

            if bars[j] <= pivot:
                i = i + 1
                if i != j:
                    bars[i], bars[j] = bars[j], bars[i]
                    self._animate()

                bars[i].state = State.UNSORTED
                self._animate()

            bars[j].state = State.UNSORTED
            self._animate()

        bars[i + 1], bars[high] = bars[high], bars[i + 1]
        self._animate()
        
        pivot.state = State.UNSORTED
        bars[i + 1].state = State.SORTED
        self._animate()

        return i + 1

    def insertion_sort(self, bars):
        for step in range(1, len(bars)):
            key = bars[step]
            key.state = State.BEING_SORTED
            self._animate()

            j = step - 1
                    
            while j >= 0 and key < bars[j]:
                bars[j].state = State.BEING_SORTED
                bars[j + 1] = bars[j]
                self._animate()

                bars[j].state = State.UNSORTED
                j = j - 1
            
            bars[j + 1] = key
            key.state = State.UNSORTED
            self._animate()

        for bar in bars:
            bar.state = State.SORTED
        self._animate()