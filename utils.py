from typing import List
from copy import deepcopy


def find_element(space_matrix: List[List[int]], element: int) -> List[int]:
    location: List[int] = [-1, -1]
    for row_i, row in enumerate(space_matrix):
        for col_i, elm in enumerate(row):
            if elm == element:
                location = [row_i, col_i]
    return location


def swap(space_matrix: List[List[int]], el1_pos: List[int], el2_pos: List[int]) -> List[List[int]]:
    new_space_matrix = deepcopy(space_matrix)
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
