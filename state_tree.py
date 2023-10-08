from collections import deque
from typing import Optional, Dict, List, Set, Deque
from state_node import StateNode
from utils import find_element


class StateTree:
    __root: Optional["StateNode"]
    __final_state: List[List[int]]
    __existing_nodes: Set["StateNode"]
    __solution_path: List[str]

    def __init__(self, root: Optional["StateNode"] = None,
                 initial_state: List[List[int]] = None,
                 final_state: List[List[int]] = None):
        if initial_state is not None:
            self.__root = StateNode(initial_state)
        else:
            self.__root = root
        self.__final_state = final_state
        self.__existing_nodes = set()
        self.__solution_path = []

    # ==========> GETTERS AND SETTERS
    def get_solution_path(self) -> List[str]:
        return self.__solution_path

    def get_root(self) -> Optional["StateNode"]:
        return self.__root

    # ==========> METHODS
    def build(self, heuristic_type: int, next_node_select: int = 1) -> Optional["StateNode"]:
        print("Building tree")
        node_deque: Deque[Optional["StateNode"]] = deque()
        node_deque.append(self.__root)
        self.__existing_nodes.add(self.__root)

        while len(node_deque) > 0:
            current_node = node_deque.popleft()
            if current_node.get_space_matrix() == self.__final_state:
                current_node.set_flag("S")
                self.__existing_nodes.add(current_node)
                return current_node

            current_node.create_children()
            children = current_node.get_children()

            if heuristic_type == 1:
                self.compute_h1(children)
            elif heuristic_type == 2:
                self.compute_h2(children)
            else:
                print("No heuristic specified")
            if next_node_select == 1:
                children = sorted(children.items(),
                                  key=lambda ch: ch[1].get_heuristic_value() if ch[1] is not None else -2,
                                  reverse=True)
                children = {key: value for key, value in children}

            for child in children.values():
                if child is None:
                    continue
                if child in self.__existing_nodes:
                    child.set_flag("D")
                else:
                    self.__existing_nodes.add(child)
                    node_deque.appendleft(child)
            if len(node_deque) == 0:
                break
            if next_node_select == 2:
                next_best_node = min(node_deque, key=lambda node: node.get_heuristic_value())
                node_deque.remove(next_best_node)
                node_deque.appendleft(next_best_node)
        return None

    def backtrack(self, solution_leaf: Optional["StateNode"]) -> None:
        print("Backtracking to root")
        if solution_leaf is None:
            return
        current_node = solution_leaf
        while current_node.get_parent() is not None:
            self.__solution_path.append(current_node.get_path_operation())
            current_node.set_flag("S")
            current_node = current_node.get_parent()

    def compute_h1(self, children: Dict[str, Optional["StateNode"]]) -> None:
        # Number of pieces not in the right place
        for child in children.values():
            if child is None:
                continue
            h_val = self.compute_h1_for_child(child.get_space_matrix())
            child.set_heuristic_value(h_val)

    def compute_h1_for_child(self, current_state: List[List[int]]) -> int:
        wrong_placed: int = 0
        for row in range(len(current_state)):
            for col in range(len(current_state[0])):
                if current_state[row][col] != self.__final_state[row][col]:
                    wrong_placed += 1
        return wrong_placed

    def compute_h2(self, children: Dict[str, Optional["StateNode"]]) -> None:
        # Sum of the distances of individual pieces from their final location
        for child in children.values():
            if child is None:
                continue
            h_val = self.compute_h2_for_child(child.get_space_matrix())
            child.set_heuristic_value(h_val)

    def compute_h2_for_child(self, current_state: List[List[int]]) -> int:
        dist_sum: int = 0
        for row in range(len(current_state)):
            for col in range(len(current_state[0])):
                final_elm_pos = find_element(self.__final_state, current_state[row][col])
                dist_sum += abs(row - final_elm_pos[0]) + abs(col - final_elm_pos[1])
        return dist_sum

    def count_nodes(self) -> int:
        print("Counting nodes")
        nodes_to_use = deque()
        nodes_to_use.append(self.__root)
        all_nodes = 0
        while len(nodes_to_use) > 0:
            current_node = nodes_to_use.popleft()
            all_nodes += 1
            children = current_node.get_children()
            for child in children.values():
                if child is not None:
                    nodes_to_use.append(child)
        return all_nodes
