from typing import Optional, Dict, List, Set
from state_node import StateNode, find_element


class StateTree:
    __root: Optional["StateNode"]
    __final_state: List[List[int]]
    __existing_nodes: Set["StateNode"]
    __solution_path: List[str]
    __found_solution: bool

    def __init__(self, root: Optional["StateNode"] = None, final_state: List[List[int]] = None):
        self.__root = root
        self.__final_state = final_state
        self.__existing_nodes = {root}
        self.__solution_path = list()
        self.__found_solution = False

    # ==========> METHODS
    def build(self):
        self.build_tree(self.__root)

    def build_tree(self, state_node: Optional["StateNode"]) -> Optional["StateNode"]:
        if state_node.get_space_matrix() == self.__final_state:
            state_node.set_flag("S")
            self.__solution_path.append(state_node.get_path_operation())
            self.__found_solution = True
            return
        if self.__found_solution is True:
            state_node.set_flag("S")
            self.__solution_path.append(state_node.get_path_operation())
            return
        if state_node in self.__existing_nodes:
            state_node.set_flag("D")
            return
        self.__existing_nodes.add(state_node)
        children = state_node.get_children()

        if self.__exist(children):
            for child in children.values():
                if child.get_flag() == "N":
                    self.build_tree(child)
        else:
            state_node.create_children()

        if self.__are_children_d(children):
            state_node.set_flag("D")
            return

        if self.__root.get_flag() == "D":
            self.__solution_path.append("Solution does not exist.")
            return

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

    # ==========> PRIVATE METHODS
    def __are_children_d(self, children: Dict[str, Optional["StateNode"]]) -> bool:
        for child in children.values():
            if child.get_flag() != "D":
                return False
            return True

    def __exist(self, children: Dict[str, Optional["StateNode"]]) -> bool:
        for child in children.values():
            if child is not None:
                return True
            return False
