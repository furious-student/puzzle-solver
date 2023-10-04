from typing import Optional, Dict, List
from state_node import StateNode, find_element


class StateTree:
    __root: Optional["StateNode"]

    def __init__(self, root: Optional["StateNode"] = None):
        __root = root

# ==========> METHODS
    def compute_h1(self, children: Dict[str, Optional["StateNode"]], final_state: List[List[int]]) -> None:
        # Number of pieces not in the right place
        for child in children.values():
            h_val = self.compute_h1_for_child(child.get_space_matrix(), final_state)
            child.set_heuristic_value(h_val)

    def compute_h1_for_child(self, current_state: List[List[int]], final_state: List[List[int]]) -> int:
        wrong_placed: int = 0
        for row in range(len(current_state)):
            for col in range(len(current_state[0])):
                if current_state[row][col] != final_state[row][col]:
                    wrong_placed += 1
        return wrong_placed

    def compute_h2(self, children: Dict[str, Optional["StateNode"]], final_state: List[List[int]]) -> None:
        # Sum of the distances of individual pieces from their final location
        for child in children.values():
            h_val = self.compute_h2_for_child(child.get_space_matrix(), final_state)
            child.set_heuristic_value(h_val)

    def compute_h2_for_child(self, current_state: List[List[int]], final_state: List[List[int]]) -> int:
        dist_sum: int = 0
        for row in range(len(current_state)):
            for col in range(len(current_state[0])):
                final_elm_pos = find_element(final_state, current_state[row][col])
                dist_sum += abs(row - final_elm_pos[0]) + abs(col - final_elm_pos[1])
        return dist_sum

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass