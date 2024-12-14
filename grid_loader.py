# Wczytywanie grid.txt
import numpy as np

# Wczytaj mapę z pliku
def load_map(filename):
    with open(filename, 'r') as file:
        grid = [list(map(int, line.split())) for line in file]
    return np.array(grid)
