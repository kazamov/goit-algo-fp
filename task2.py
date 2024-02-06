import matplotlib.pyplot as plt
import numpy as np


def draw_pifagoras_tree(ax, x, y, length, angle, level):
    if level == 0:
        return
    else:
        x_end = x + length * np.cos(np.radians(angle))
        y_end = y + length * np.sin(np.radians(angle))

        ax.plot([x, x_end], [y, y_end], color="brown", linewidth=1)

        draw_pifagoras_tree(ax, x_end, y_end, 0.7 * length, angle - 45, level - 1)

        draw_pifagoras_tree(ax, x_end, y_end, 0.7 * length, angle + 45, level - 1)


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")

    recursion_level = int(input("Enter the recursion level: "))

    draw_pifagoras_tree(ax, 0, 0, 100, 90, recursion_level)

    plt.show()
