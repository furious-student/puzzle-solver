from utils import find_element
from typing import List
from state_tree import StateTree


class PuzzleSolver:
    __initial_state: List[List[int]]
    __final_state: List[List[int]]
    __solution_path: List[str]

    def __init__(self, initial_state: List[List[int]] = None, final_state: List[List[int]] = None):
        self.__initial_state = initial_state
        self.__final_state = final_state

    # ==========> GETTERS & SETTERS
    def set_states(self, initial_state: List[List[int]], final_state: List[List[int]]) -> None:
        self.__initial_state = initial_state
        self.__final_state = final_state

    # ==========> METHODS
    def solve(self, heuristic_type: int = 1, next_node_select: int = 1) -> tuple[List[str], int, int]:
        print("Solving")
        if not self.are_comparable():
            return ["Non-comparable states. Dimensions or elements differ."], -1, -1
        elif not self.is_solvable():
            return ["Non-solvable problem."], -1, -1
        elif self.__initial_state == self.__final_state:
            return ["Initial and final state are equal."], 0, 1
        state_tree = StateTree(initial_state=self.__initial_state, final_state=self.__final_state)
        solution_node = state_tree.build(heuristic_type, next_node_select)
        state_tree.backtrack(solution_node)
        solution_path = state_tree.get_solution_path()
        solution_path.reverse()
        if solution_path is None:
            solution_path = ["No solution found."]
        return solution_path, len(solution_path), state_tree.count_nodes()

    def is_solvable(self) -> bool:
        def __flatten(list_2d: List[List[int]]) -> List[int]:
            return [element for row in list_2d for element in row]

        def __count_state_n(lst: List[int]) -> int:
            def __count_elem_n(elem: int) -> int:
                elem_n: int = 0
                for el in lst:
                    if el == elem or elem == 0:
                        return elem_n
                    if el == 0:
                        continue
                    if el > elem:
                        elem_n += 1
                return elem_n

            state_n: int = 0
            for e in lst:
                state_n += __count_elem_n(e)
            return state_n

        flt_initial: List[int] = __flatten(self.__initial_state)
        flt_final: List[int] = __flatten(self.__final_state)
        initial_n: int = __count_state_n(flt_initial)
        final_n: int = __count_state_n(flt_final)
        if len(self.__final_state) == len(self.__initial_state) and len(self.__initial_state) % 2 == 0:
            print("======")
            initial_n += find_element(self.__initial_state, 0)[0] + 1
            final_n += find_element(self.__final_state, 0)[0] + 1
        return initial_n % 2 == final_n % 2

    def are_comparable(self) -> bool:
        matrix_1 = self.__initial_state
        matrix_2 = self.__final_state
        if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
            return False
        for row_i, row in enumerate(matrix_1):
            for col_i, col in enumerate(row):
                wanted_element_pos = find_element(matrix_2, matrix_1[row_i][col_i])
                if wanted_element_pos[0] < 0 or wanted_element_pos[1] < 0:
                    return False
        return True
