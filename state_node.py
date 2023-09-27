from typing import List, Optional, Dict


class StateNode:
    __space: List[List[int]]
    __parent: Optional["StateNode"]
    __children: Dict[str, Optional["StateNode"]]
    __path_operation: str

    def __init__(self, space: List[List[int]]):
        self.__space = space
        self.__parent = None
        self.__children = {
            "left": None,
            "right": None,
            "up": None,
            "down": None
        }
        self.__path_operation: None

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass

    def compute_h_1(self):
        pass  # Number of pieces not on the right place

    def compute_h_2(self):
        pass  # Sum of the distances of individual pieces from their final location
