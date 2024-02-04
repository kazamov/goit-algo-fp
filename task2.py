import matplotlib.pyplot as plt
import numpy as np


def draw_pifagoras_tree(ax, x, y, length, angle, level):
    if level == 0:
        return
    else:
        # Calculate the end point of the branch
        x_end = x + length * np.cos(np.radians(angle))
        y_end = y + length * np.sin(np.radians(angle))

        # Draw the branch
        ax.plot([x, x_end], [y, y_end], color="brown", linewidth=1)

        # Recursive call for the right branch
        draw_pifagoras_tree(ax, x_end, y_end, 0.7 * length, angle - 45, level - 1)

        # Recursive call for the left branch
        draw_pifagoras_tree(ax, x_end, y_end, 0.7 * length, angle + 45, level - 1)


if __name__ == "__main__":
    # Set up the figure
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")

    # Specify the recursion level
    recursion_level = int(input("Enter the recursion level: "))

    # Draw the Pifagoras tree
    draw_pifagoras_tree(ax, 0, 0, 100, 90, recursion_level)

    # Show the plot
    plt.show()