# Wyświetlanie siatki i znalezionej ścieżki
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Wizualizuj siatkę i wynik
def visualize_path(grid, start, goal, ax, canvas):
    ax.clear()
    ax.imshow(grid, cmap="viridis", origin="lower")
    ax.scatter(start[1], start[0], color="red", label="Start", s=100, edgecolor='black')
    ax.scatter(goal[1], goal[0], color="blue", label="Cel", s=100, edgecolor='black')

    # Dodanie siatki z wyraźniejszymi liniami
    ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="--", linewidth=0.5, alpha=0.7)

    # Dodanie numeracji pozycji na osiach
    ax.set_xticks(np.arange(0, grid.shape[1], 1))
    ax.set_yticks(np.arange(0, grid.shape[0], 1))
    ax.set_xticklabels(np.arange(0, grid.shape[1], 1))
    ax.set_yticklabels(np.arange(0, grid.shape[0], 1))

    ax.legend()
    ax.set_title("Znaleziona Najkrótsza Ścieżka")
    canvas.draw()
