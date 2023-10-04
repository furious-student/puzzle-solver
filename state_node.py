import copy
from typing import List, Optional, Dict


def find_element(space_matrix: List[List[int]], element: int) -> List[int]:
    location: List[int] = [-1, -1]
    for row_i, row in enumerate(space_matrix):
        for col_i, elm in enumerate(row):
            if elm == element:
                location = [row_i, col_i]
    return location


def swap(space_matrix: List[List[int]], el1_pos: List[int], el2_pos: List[int]) -> List[List[int]]:
    new_space_matrix = copy.deepcopy(space_matrix)
    if len(el1_pos) != 2 and len(el2_pos) != 2:
        raise ValueError("Argument \"el1_pos\" and \"el2_pos\" must have exactly two integers.")
    row_len = len(new_space_matrix)
    col_len = len(new_space_matrix[0])
    el1_x, el1_y = el1_pos
    el2_x, el2_y = el2_pos
    if (
            not (row_len, col_len >= el1_x, el1_y and
                 0, 0 <= el1_x, el1_y and
                 row_len, col_len >= el2_x, el2_y and
                 0, 0 <= el2_x, el2_y)
    ):
        return new_space_matrix
    temp = new_space_matrix[el1_x][el1_y]
    new_space_matrix[el1_x][el1_y] = new_space_matrix[el2_x][el2_y]
    new_space_matrix[el2_x][el2_y] = temp
    return new_space_matrix


class StateNode:
    __space_matrix: List[List[int]]
    __parent: Optional["StateNode"]
    __children: Dict[str, Optional["StateNode"]]
    __path_operation: str
    __heuristic_value: int
    __flag: str  # N - new | D - duplicate/dead end | S - solution

    def __init__(self, space_matrix: List[List[int]], parent: Optional["StateNode"] = None, path_operation: str = None):
        self.__space_matrix = space_matrix
        self.__parent = parent
        self.__flag = "N"
        self.__children = {
            "left": None,
            "right": None,
            "up": None,
            "down": None
        }
        self.__path_operation = path_operation
        self.__heuristic_value = -1

    def __eq__(self, other) -> bool:
        if not isinstance(other, StateNode):
            return False
        return self.__space_matrix == other.get_space_matrix()

    def __hash__(self):
        space_matrix_tuple = tuple(tuple(row) for row in self.__space_matrix)
        return hash(space_matrix_tuple)

    def __str__(self):
        string = "Hash: " + str(self.__hash__()) + "\n" + \
                 "Flag: " + self.__flag + "\n" + \
                 "Path OP: " + self.__path_operation + "\n" + \
                 "Space matrix: " + "\n"
        for row in self.__space_matrix:
            string += str(row) + "\n"
        return string

    # ==========> GETTERS & SETTERS
    def get_space_matrix(self) -> List[List[int]]:
        return self.__space_matrix

    def get_children(self) -> Dict[str, Optional["StateNode"]]:
        return self.__children

    def get_heuristic_value(self) -> int:
        return self.__heuristic_value

    def get_path_operation(self) -> str:
        return self.__path_operation

    def get_flag(self) -> str:
        return self.__flag

    def set_heuristic_value(self, h_val: int) -> None:
        self.__heuristic_value = h_val

    def set_flag(self, flag: str) -> None:
        self.__flag = flag

    # ==========> METHODS
    def print_space_matrix(self) -> None:
        for row in self.__space_matrix:
            print(row)

    def create_right_child(self) -> None:
        empty_slot = find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        child_space_matrix = self.__space_matrix
        if empty_y > 0:
            elm_to_move = [empty_x, empty_y - 1]
            child_space_matrix = swap(space_matrix=self.__space_matrix,
                                      el1_pos=empty_slot,
                                      el2_pos=elm_to_move)
        self.__create_child(child_space_matrix, "right")

    def create_left_child(self) -> None:
        empty_slot = find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        child_space_matrix = self.__space_matrix
        if empty_y < len(self.__space_matrix[0]) - 1:
            elm_to_move = [empty_x, empty_y + 1]
            child_space_matrix = swap(space_matrix=self.__space_matrix,
                                      el1_pos=empty_slot,
                                      el2_pos=elm_to_move)
        self.__create_child(child_space_matrix, "right")
        self.__create_child(child_space_matrix, "left")

    def create_down_child(self) -> None:
        empty_slot = find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        child_space_matrix = self.__space_matrix
        if empty_x > 0:
            elm_to_move = [empty_x - 1, empty_y]
            child_space_matrix = swap(space_matrix=self.__space_matrix,
                                      el1_pos=empty_slot,
                                      el2_pos=elm_to_move)
        self.__create_child(child_space_matrix, "down")

    def create_up_child(self) -> None:
        empty_slot = find_element(space_matrix=self.__space_matrix, element=0)
        empty_x, empty_y = empty_slot
        child_space_matrix = self.__space_matrix
        if empty_x < len(self.__space_matrix) - 1:
            elm_to_move = [empty_x + 1, empty_y]
            child_space_matrix = swap(space_matrix=self.__space_matrix,
                                      el1_pos=empty_slot,
                                      el2_pos=elm_to_move)
        self.__create_child(child_space_matrix, "up")

    def create_children(self) -> None:
        self.create_left_child()
        self.create_right_child()
        self.create_up_child()
        self.create_down_child()

    # ==========> PRIVATE METHODS
    def __create_child(self, space_matrix: List[List[int]], path_operation: str = None) -> None:
        ops = ["left", "right", "up", "down"]
        if path_operation not in ops:
            raise Exception(f"Argument \"path_operation\" {path_operation} not from {ops}")
        child = StateNode(space_matrix=space_matrix, parent=self, path_operation=path_operation)
        self.__children[path_operation] = child
