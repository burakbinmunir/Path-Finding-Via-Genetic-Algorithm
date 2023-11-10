# A* Algorithm with Genetic Algorithm Optimization

This program demonstrates the combination of the A* algorithm with a genetic algorithm to find an optimal path in a grid-based environment. The A* algorithm is used for pathfinding, and the genetic algorithm optimizes the path by evolving a population of potential solutions.

<p align='center'>
  <img src='https://github.com/burakbinmunir/Path-Finding-Via-Genetic-Algorithm/assets/108978796/77faee91-7c3a-4097-be7d-bcdf8877d57d'/>
</p>

## Requirements

- Python 3.x
- Tkinter library

## Usage

1. Run the program in a Python environment.
2. The grid-based environment is displayed with the start and end points marked.
3. The A* algorithm finds the optimal path between two points in a population.
4. The genetic algorithm then optimizes the path with multiple generations.
5. The final result is displayed, showing the total cost of the optimal path and the paths found by the genetic algorithm.

## Code Overview

- `node` class: Represents a node in the grid with attributes like coordinates, cost, and parent node.
- `initialize_grid(size, goal)`: Initializes the grid with nodes, setting blocked nodes as obstacles.
- `a_star(start, grid, size, goal)`: Performs the A* search algorithm to find the optimal path between two points.
- `draw_grid(canvas, grid, size, path)`: Draws the grid on a Tkinter canvas, highlighting the optimal path.
- Genetic Algorithm:
  - Initializes a population with fixed start and end nodes and random intermediate nodes.
  - Runs the genetic algorithm for a specified number of generations.
  - Performs crossover and mutation to evolve the population.
  - Replaces the worst chromosomes with the best children.
  - Finds the optimal path using A* between each pair of genes (nodes) in the best chromosome.

## Customization

You can customize the following parameters in the code:

- `grid_size`: Size of the grid.
- `population_size`: Size of the genetic algorithm population.
- `chromosome_size`: Number of nodes in each chromosome.
- `mutation_rate`: Probability of mutation during crossover.
- `generation_gap`: Percentage of the population replaced in each generation.

## Credits

- The A* algorithm is a widely used pathfinding algorithm.
- The genetic algorithm is a heuristic optimization technique inspired by natural selection.
