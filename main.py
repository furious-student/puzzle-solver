from state_node import StateNode
from state_tree import StateTree


def main():
    space_matrix = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    space_matrix2 = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    space_matrix3 = [
        [8, 2, 3],
        [4, 5, 1],
        [6, 7, 0]
    ]
    root = StateNode(space_matrix=space_matrix)
    root.create_children()
    state_tree = StateTree(root)

    #state_tree.compute_h1(root.get_children(), space_matrix3)
    state_tree.compute_h2(root.get_children(), space_matrix3)

    for child in root.get_children().values():
        child.print_space_matrix()
        print("H:", str(child.get_heuristic_value()), "Move", child.get_path_operation())
        print()


if __name__ == '__main__':
    main()

