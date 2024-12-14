# Aplikacja GUI
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from grid_loader import load_map
from a_star import a_star
from visualization import visualize_path

# Stałe
WIDTH, HEIGHT = 20, 20
OBSTACLE = 5  # Wartość oznaczająca przeszkodę

# GUI aplikacji
class PathfindingApp:
    def __init__(self, root, grid):
        self.root = root
        self.grid = grid
        self.start = (0, 0)
        self.goal = (WIDTH - 1, HEIGHT - 1)

        self.root.title("Aplikacja Szukania Trasy")
        self.create_widgets()

    def create_widgets(self):
        # Wprowadzanie punktów Start i Koniec
        tk.Label(self.root, text="Start (x, y):").grid(row=0, column=0, padx=5, pady=5)
        self.start_entry = tk.Entry(self.root, width=10)
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)
        self.start_entry.insert(0, "0, 0")

        tk.Label(self.root, text="Cel (x, y):").grid(row=1, column=0, padx=5, pady=5)
        self.goal_entry = tk.Entry(self.root, width=10)
        self.goal_entry.grid(row=1, column=1, padx=5, pady=5)
        self.goal_entry.insert(0, f"{WIDTH-1}, {HEIGHT-1}")

        # Przycisk do rozpoczęcia wyszukiwania
        tk.Button(self.root, text="Znajdź trasę", command=self.run_pathfinding).grid(row=2, column=0, columnspan=2, pady=10)

        # Miejsce na wizualizację
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

    def run_pathfinding(self):
        try:
            start = tuple(map(int, self.start_entry.get().split(',')))
            goal = tuple(map(int, self.goal_entry.get().split(',')))

            if not (0 <= start[0] < WIDTH and 0 <= start[1] < HEIGHT):
                raise ValueError("Start poza zakresem.")
            if not (0 <= goal[0] < WIDTH and 0 <= goal[1] < HEIGHT):
                raise ValueError("Cel poza zakresem.")
            if self.grid[start] == OBSTACLE or self.grid[goal] == OBSTACLE:
                raise ValueError("Start lub Cel jest przeszkodą.")

            # Uruchomienie algorytmu A*
            visited, path = a_star(self.grid, start, goal)
            if path is None:
                messagebox.showerror("Error", "Nie znaleziono ścieżki!")
                return

            # Wyświetlenie wyniku
            visualize_path(visited, start, goal, self.ax, self.canvas)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Główna funkcja
if __name__ == "__main__":
    grid = load_map('grid.txt')
    root = tk.Tk()
    app = PathfindingApp(root, grid)
    root.mainloop()
