from typing import List, Optional, Dict, Tuple


class StateNode:
    __space_matrix: List[List[int]]
    __parent: Optional["StateNode"]
    __children: Dict[str, Optional["StateNode"]]
    __path_operation: str

    def __init__(self, space_matrix: List[List[int]], parent: Optional["StateNode"] = None, path_operation: str = None):
        self.__space_matrix = space_matrix
        self.__parent = parent
        self.__children = {
            "left": None,
            "right": None,
            "up": None,
            "down": None
        }
        self.__path_operation: path_operation

    def get_space_matrix(self) -> List[List[int]]:
        return self.__space_matrix

    def print_space_matrix(self) -> None:
        for row in self.__space_matrix:
            print(row)

    def create_right_child(self) -> None:
        empty_slot = self.__find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        if empty_y > 0:
            elm_to_move = [empty_x, empty_y - 1]
            self.__space_matrix = self.__swap(space_matrix=self.__space_matrix,
                                              el1_pos=empty_slot,
                                              el2_pos=elm_to_move)

    def create_left_child(self) -> None:
        empty_slot = self.__find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        if empty_y < len(self.__space_matrix[0]) - 1:
            elm_to_move = [empty_x, empty_y + 1]
            self.__space_matrix = self.__swap(space_matrix=self.__space_matrix,
                                              el1_pos=empty_slot,
                                              el2_pos=elm_to_move)

    def create_down_child(self) -> None:
        empty_slot = self.__find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        if empty_x > 0:
            elm_to_move = [empty_x - 1, empty_y]
            self.__space_matrix = self.__swap(space_matrix=self.__space_matrix,
                                              el1_pos=empty_slot,
                                              el2_pos=elm_to_move)

    def create_up_child(self) -> None:
        empty_slot = self.__find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        if empty_x < len(self.__space_matrix) - 1:
            elm_to_move = [empty_x + 1, empty_y]
            self.__space_matrix = self.__swap(space_matrix=self.__space_matrix,
                                              el1_pos=empty_slot,
                                              el2_pos=elm_to_move)

    def __create_child(self, space_matrix: List[List[int]], path_operation: str = None) -> None:
        ops = ["left, right, up, down"]
        if path_operation not in ops:
            raise Exception(f"Argument \"path_operation\" {path_operation} not from {ops}")
        child = StateNode(space_matrix=space_matrix, parent=self, path_operation=path_operation)
        self.__children.__setitem__(path_operation, child)

    def __find_element(self, space_matrix: List[List[int]], element: int) -> List[int]:
        location: List[int] = [-1, -1]
        for row_i, row in enumerate(space_matrix):
            for col_i, elm in enumerate(row):
                if elm == element:
                    location = [row_i, col_i]
        return location

    def __swap(self, space_matrix: List[List[int]], el1_pos: List[int], el2_pos: List[int]) -> List[List[int]]:
        if len(el1_pos) != 2 and len(el2_pos) != 2:
            raise ValueError("Argument \"el1_pos\" and \"el2_pos\" must have exactly two integers.")
        row_len = len(space_matrix)
        col_len = len(space_matrix[0])
        el1_x, el1_y = el1_pos
        el2_x, el2_y = el2_pos
        if(
            not(
                row_len, col_len >= el1_x, el1_y and
                0, 0 <= el1_x, el1_y and
                row_len, col_len >= el2_x, el2_y and
                0, 0 <= el2_x, el2_y
            )
        ):
            return space_matrix
        temp = space_matrix[el1_x][el1_y]
        space_matrix[el1_x][el1_y] = space_matrix[el2_x][el2_y]
        space_matrix[el2_x][el2_y] = temp
        return space_matrix
