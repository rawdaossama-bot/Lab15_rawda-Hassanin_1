"""
Spiral
Name: Rawda Hassanin
Date: 12/8/2025
Lab15_Rawda_Hassanin_1_Spiral
Generate and plot an outward spiral using matplotlib.

This module computes (x, y) points for a spiral where the radius grows
with angle and renders the result. The implementation is split into
reusable functions so the behavior is import-safe (no plotting on
import) and can be customized programmatically.
"""

import math
import matplotlib.pyplot as plt


def generate_spiral_points(start_deg=0, end_deg=720, step_deg=2, growth=0.05):
    """
    Generate x and y coordinates for a spiral.

    The spiral is defined in polar coordinates where the radius increases
    linearly with the angle: radius = growth * angle. Angles are provided
    in degrees and converted to radians for the trigonometric functions.

    Args:
        start_deg (int): Starting angle in degrees (inclusive).
        end_deg (int): Ending angle in degrees (exclusive).
        step_deg (int): Step between angle samples in degrees.
        growth (float): Growth factor that multiplies the angle to obtain radius.

    Returns:
        tuple: Two lists `(x_values, y_values)` representing the Cartesian
        coordinates of the spiral points.
    """
    x_values = []
    y_values = []
    for angle in range(start_deg, end_deg, step_deg):
        rad = math.radians(angle)
        radius = growth * angle
        x_values.append(radius * math.cos(rad))
        y_values.append(radius * math.sin(rad))
    return x_values, y_values


def plot_spiral(start_deg=0, end_deg=720, step_deg=2, growth=0.05,
                figsize=(6, 6), color='green', linewidth=2):
    """
    Plot an outward spiral using matplotlib.

    Args:
        start_deg (int): Starting angle in degrees (inclusive).
        end_deg (int): Ending angle in degrees (exclusive).
        step_deg (int): Degree increment between samples.
        growth (float): Radius growth per degree.
        figsize (tuple): Figure size (width, height) in inches.
        color (str): Line color for the spiral.
        linewidth (int|float): Line thickness.
    """
    x_values, y_values = generate_spiral_points(start_deg, end_deg, step_deg, growth)
    plt.figure(figsize=figsize)
    plt.plot(x_values, y_values, color=color, linewidth=linewidth)
    plt.title("Spiral")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plot_spiral()
