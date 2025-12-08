"""
Name: Rawda Hassanin
Date: 12/8/2025
Lab15_Rawda_Hassanin_1_
Sin_Wave

Compute and plot a sine wave using matplotlib.

This module provides functions to generate (x, y) samples of the sine
function for degree inputs and to plot the resulting waveform. The
script is safe to import (it will not display plots on import) and
keeps the original behavior when executed as a script.

Functions provided:
    - generate_sine_points: return lists of degree and sine values.
    - plot_sine: render the sine wave with simple styling.
"""

import math
import matplotlib.pyplot as plt


def generate_sine_points(start_deg=0, end_deg=360, step=1):
    """
    Generate degree and sine-value lists for a range of angles.

    Args:
        start_deg (int): Starting degree (inclusive).
        end_deg (int): Ending degree (exclusive).
        step (int): Step between degrees.

    Returns:
        tuple: Two lists `(degrees, sine_values)` where `degrees` are
        the integer degree values and `sine_values` are the corresponding
        floating-point sine values.
    """
    degrees = list(range(start_deg, end_deg, step))
    sine_values = [math.sin(math.radians(d)) for d in degrees]
    return degrees, sine_values


def plot_sine(start_deg=0, end_deg=360, step=1, figsize=(8, 4),
              color='red', linewidth=2, linestyle='--'):
    """
    Plot a sine wave using matplotlib.

    Args:
        start_deg (int): Starting degree (inclusive).
        end_deg (int): Ending degree (exclusive).
        step (int): Degree step between samples.
        figsize (tuple): Matplotlib figure size (width, height) in inches.
        color (str): Line color for the plot.
        linewidth (int|float): Thickness of the plotted line.
        linestyle (str): Line style.
    """
    x_values, y_values = generate_sine_points(start_deg, end_deg, step)
    plt.figure(figsize=figsize)
    plt.plot(x_values, y_values, color=color, linewidth=linewidth, linestyle=linestyle)
    plt.title("Sine Wave")
    plt.xlabel("Degrees")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_sine()
