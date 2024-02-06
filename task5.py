import uuid

import networkx as nx
import matplotlib.pyplot as plt

PALETTE = ["#FA0505", "#FB3404", "#FC6403", "#FD9302", "#FEC301", "#FFF200"]


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


def draw_tree(tree_root, traversal_function, title):
    tree_root = traversal_function(tree_root)
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def bread_first_traversal(tree_root):
    palette = PALETTE.copy()

    queue = [(tree_root, palette.pop(0))]

    while queue:
        node, color = queue.pop(0)
        node.color = color

        if node.left:
            queue.append((node.left, palette.pop(0)))
        if node.right:
            queue.append((node.right, palette.pop(0)))

    return tree_root


def depth_first_traversal(root, palette=PALETTE.copy()):
    if root:
        root.color = palette.pop(0)
        depth_first_traversal(root.left, palette)
        depth_first_traversal(root.right, palette)

    return root


if __name__ == "__main__":
    first_root = Node(0)
    first_root.left = Node(4)
    first_root.left.left = Node(5)
    first_root.left.right = Node(10)
    first_root.right = Node(1)
    first_root.right.left = Node(3)

    draw_tree(first_root, bread_first_traversal, "Breadth First Traversal")

    second_root = Node(0)
    second_root.left = Node(4)
    second_root.left.left = Node(5)
    second_root.left.right = Node(10)
    second_root.right = Node(1)
    second_root.right.left = Node(3)

    draw_tree(second_root, depth_first_traversal, "Depth First Traversal")
