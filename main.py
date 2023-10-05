from state_node import StateNode
from state_tree import StateTree
from puzzle_solver import PuzzleSolver


def main():
    space_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    space_matrix2 = [
        [5, 1, 0],
        [4, 6, 8],
        [7, 3, 2]
    ]

    space_matrix_15_v1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    space_matrix_15_v2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 15, 14, 0]
    ]
    # root = StateNode(space_matrix=space_matrix)
    # root.create_children()
    state_tree = StateTree(start_state=space_matrix, final_state=space_matrix2)
    state_tree.build()
    solution = state_tree.get_solution_path()
    solution.reverse()
    print(solution, state_tree.get_root().get_flag())


if __name__ == '__main__':
    main()
