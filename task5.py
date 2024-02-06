import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal_function):
    tree_root = traversal_function(tree_root)
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def darken_color(hex_color, factor=0.8):
    hex_color = hex_color.lstrip("#")

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    red = max(0, int(red * factor))
    green = max(0, int(green * factor))
    blue = max(0, int(blue * factor))

    dark_hex_color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return dark_hex_color


def bread_first_traversal(tree_root):
    main_color = "#FF7F7F"
    queue = [(tree_root, main_color)]

    while queue:
        node, color = queue.pop(0)
        node.color = color

        if node.left:
            main_color = darken_color(main_color)
            queue.append((node.left, main_color))
        if node.right:
            main_color = darken_color(main_color)
            queue.append((node.right, main_color))

    return tree_root


def depth_first_traversal(root, color="#90EE90"):
    if root:
        root.color = color
        depth_first_traversal(root.left, darken_color(color))
        depth_first_traversal(root.right, darken_color(color))

    return root


if __name__ == "__main__":
    first_root = Node(0)
    first_root.left = Node(4)
    first_root.left.left = Node(5)
    first_root.left.right = Node(10)
    first_root.right = Node(1)
    first_root.right.left = Node(3)

    draw_tree(first_root, bread_first_traversal)

    second_root = Node(0)
    second_root.left = Node(4)
    second_root.left.left = Node(5)
    second_root.left.right = Node(10)
    second_root.right = Node(1)
    second_root.right.left = Node(3)

    draw_tree(second_root, depth_first_traversal)
