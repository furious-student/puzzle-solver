from typing import Optional
from state_node import StateNode


class StateTree:
    __root: Optional["StateNode"]

    def __init__(self):
        __root = None

    def compute_h_1(self):
        pass  # Number of pieces not on the right place

    def compute_h_2(self):
        pass  # Sum of the distances of individual pieces from their final location

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass