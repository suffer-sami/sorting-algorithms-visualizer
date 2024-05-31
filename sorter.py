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
