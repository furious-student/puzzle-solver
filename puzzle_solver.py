from state_tree import StateTree
from state_node import find_element
from typing import List


class PuzzleSolver:
    __initial_state: List[List[int]]
    __final_state: List[List[int]]
    __solution_path: List[str]

    def __init__(self, initial_state: List[List[int]], final_state: List[List[int]]):
        self.__initial_state = initial_state
        self.__final_state = final_state

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
        initial_n: int = find_element(self.__initial_state, 0)[0] + __count_state_n(flt_initial) + 1
        final_n: int = find_element(self.__final_state, 0)[0] + __count_state_n(flt_final) + 1
        print("initial_n:", initial_n, "final_n", final_n)
        return initial_n % 2 == final_n % 2
