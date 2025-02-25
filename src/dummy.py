import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            matrix = [list(map(float, line.split())) for line in f]
    except FileNotFoundError:
        return "No file found. Upload a file first."
    except ValueError:
        return "Invalid file format. Ensure it contains only numbers."

    fig, ax = plt.subplots()
    heatmap = ax.imshow(matrix, cmap="viridis", aspect="auto")
    plt.colorbar(heatmap)
    return fig


def plot_loss_curve():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig
