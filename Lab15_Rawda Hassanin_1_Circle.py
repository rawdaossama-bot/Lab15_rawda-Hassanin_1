"""
Lab15_Rawda_Hassanin_1_Circle
Nmae: Rawda Hassanin
Date: 12/8/2025
Generate and display a 2D circle using matplotlib.

This module computes (x, y) coordinates for a circle of a fixed
radius by iterating angles in degrees, converting to radians with
the :mod:`math` module, and plotting the result using
:mod:`matplotlib.pyplot`.

The script is designed to be run directly; it produces a simple
plot with equal axis scaling so the circle appears round.
"""

import math
import matplotlib.pyplot as plt

def generate_circle_points(radius=5, steps=360):
    """
    Generate x and y coordinate lists for a circle.

    The function iterates `steps` discrete angles in degrees, converts
    each to radians, and computes the corresponding (x, y) coordinates
    for a circle with the given `radius`.

    Args:
        radius (float): Radius of the circle.
        steps (int): Number of points (degrees) to generate. Default 360.

    Returns:
        tuple: Two lists `(x_values, y_values)` containing the circle
        coordinates.
    """
    x_values = []
    y_values = []
    for angle in range(steps):  # degrees
        rad = math.radians(angle)  # convert to radians
        x_values.append(radius * math.cos(rad))
        y_values.append(radius * math.sin(rad))
    return x_values, y_values


def plot_circle(radius=5, steps=360, figsize=(6, 6), color='blue', linewidth=2):
    """
    Plot a circle using matplotlib.

    This function obtains circle coordinates from :func:`generate_circle_points`
    and renders them with the provided plotting options. The plot uses
    equal axis scaling so the circle is not distorted.

    Args:
        radius (float): Radius of the circle to plot.
        steps (int): Number of points to compute along the circle.
        figsize (tuple): Figure size (width, height) in inches.
        color (str): Line color for the circle.
        linewidth (int|float): Width of the plotted line.
    """
    x_values, y_values = generate_circle_points(radius, steps)
    plt.figure(figsize=figsize)
    plt.plot(x_values, y_values, color=color, linewidth=linewidth)  # circle
    plt.title("Circle")
    plt.axis("equal")  # equal scaling on x and y
    plt.show()


if __name__ == "__main__":
    # Default behavior when run as a script: plot a circle of radius 5
    plot_circle()
