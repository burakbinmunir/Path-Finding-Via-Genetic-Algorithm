import random
import tkinter as tk

# Class to represent a node in the grid
class node:
    x = -1
    y = -1
    g = -1
    h = -1
    f = -1
    visited = False
    blocked = False
    parent = None
    
    def __init__(self):
        x = -1
        y = -1
        g = -1
        h = -1
        f = -1
        visited = False
        blocked = False
        parent = None

# Function to calculate the Euclidean distance between two points
ecludian_distance = lambda x1, y1, x2, y2 : ((x2-x1)**2 + (y2-y1)**2)**0.5

# Initialize the grid with nodes
def initialize_grid( size , goal):
    grid = [[0 for x in range(size)] for y in range(size)]
    for _ in range(size):
        for __ in range(size):
            n = node()
            n.x = _
            n.y = __
            n.g = 1
            n.h = ecludian_distance(_, __, goal.x, goal.y) # Use Euclidean distance as the heuristic
            grid[_][__] = n
    
    # grid[5][0].blocked = True
    # grid[5][1].blocked = True
    # grid[5][2].blocked = True
    # grid[5][3].blocked = True
    grid[5][4].blocked = True
    grid[5][5].blocked = True
    grid[5][6].blocked = True
    grid[5][7].blocked = True
    grid[5][8].blocked = True
    grid[5][9].blocked = True
    grid[9][3].blocked = True
    grid[4][4].blocked = True
    grid[2][5].blocked = True
    grid[7][4].blocked = True
    # grid[5][4].blocked = True
    # grid[3][6].blocked = True
    # grid[1][2].blocked = True
    
    return grid

# Function to sort the open list based on `f` value
def sort_open_list(open_list):
    for _ in range(len(open_list)):
        for __ in range(len(open_list)):
            if open_list[_].f < open_list[__].f:
                temp = open_list[_]
                open_list[_] = open_list[__]
                open_list[__] = temp
    return open_list

# Function to extract the path from the closed list
def extract_path(closed_list):
    path = []
    current = closed_list[-1]  
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]  

# Function to perform A* search
def a_star(start, grid, size, goal):
    open_list = []
    open_list.append(grid[start.x][start.y])
    closed_list = []
    
    # Check if the goal or start is blocked
    if grid[goal.x][goal.y].blocked == True or grid[start.x][start.y].blocked == True:
        return None , None
    
    g_t = 0 # Total cost from start to current node
    goal_found = False
    while open_list and goal_found == False:
        open_list = sort_open_list(open_list)
        current = open_list[0]
        
        if current.visited == False:
            current.visited = True            
        
            g_t += current.g
            
            if current.x == goal.x and current.y == goal.y:
                goal_found = True
                closed_list.append(current)
                path = extract_path(closed_list)
                cost = 0
                for _ in range(len(path)):
                    cost += path[_].g
                return path , cost
            
            if current.x - 1 >= 0 and current.x - 1 < size  and current.y >= 0 and current.y < size and grid[current.x - 1][current.y].visited == False and grid[current.x - 1][current.y].blocked == False:
                grid[current.x - 1][current.y].f = g_t + grid[current.x - 1][current.y].h
                grid[current.x - 1][current.y].parent = current
                if  grid[current.x - 1][current.y] not in open_list:
                    open_list.append(grid[current.x - 1][current.y])
                
            if current.x + 1 >= 0 and current.x + 1 < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x + 1][current.y + 1].visited == False and grid[current.x + 1][current.y + 1].blocked == False:
                grid[current.x + 1][current.y + 1].f = g_t + grid[current.x + 1][current.y + 1].h
                grid[current.x + 1][current.y + 1].parent = current
                if grid[current.x + 1][current.y + 1] not in open_list:
                    open_list.append(grid[current.x + 1][current.y + 1])
                
            if current.x + 1 >= 0 and  current.x + 1 < size and current.y >= 0 and current.y < size and grid[current.x + 1][current.y].visited == False and grid[current.x + 1][current.y].blocked == False:
                grid[current.x + 1][current.y].f = g_t + grid[current.x + 1][current.y].h
                grid[current.x + 1][current.y].parent = current
                if grid[current.x + 1][current.y] not in open_list:
                    open_list.append(grid[current.x + 1][current.y])
                
            if current.x >= 0 and current.x < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x][current.y + 1].visited == False and grid[current.x][current.y + 1].blocked == False:
                grid[current.x][current.y + 1].f = g_t + grid[current.x][current.y + 1].h
                grid[current.x][current.y + 1].parent = current
                if grid[current.x][current.y + 1] not in open_list:
                    open_list.append(grid[current.x][current.y + 1])
                
            if current.x - 1 >= 0 and  current.x - 1 < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x - 1][current.y + 1].visited == False and grid[current.x - 1][current.y + 1].blocked == False:
                grid[current.x - 1][current.y + 1].f = g_t + grid[current.x - 1][current.y + 1].h
                grid[current.x - 1][current.y + 1].parent = current
                if grid[current.x - 1][current.y + 1] not in open_list:
                    open_list.append(grid[current.x - 1][current.y + 1])
                
            if current.x + 1 >= 0 and current.x + 1 < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x + 1][current.y - 1].visited == False and grid[current.x + 1][current.y - 1].blocked == False:
                grid[current.x + 1][current.y - 1].f = g_t + grid[current.x + 1][current.y - 1].h
                grid[current.x + 1][current.y - 1].parent = current
                if grid[current.x + 1][current.y - 1] not in open_list:
                    open_list.append(grid[current.x + 1][current.y - 1])
                
            if current.x >= 0 and current.x < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x][current.y - 1].visited == False and grid[current.x][current.y - 1].blocked == False:
                grid[current.x][current.y - 1].f = g_t + grid[current.x][current.y - 1].h
                grid[current.x][current.y - 1].parent = current
                if grid[current.x][current.y - 1] not in open_list:
                    open_list.append(grid[current.x][current.y - 1])
                
            if current.x - 1 >= 0 and current.x - 1 < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x - 1][current.y - 1].visited == False and grid[current.x - 1][current.y - 1].blocked == False:
                grid[current.x - 1][current.y - 1].f = g_t + grid[current.x - 1][current.y - 1].h
                grid[current.x - 1][current.y - 1].parent = current
                if grid[current.x - 1][current.y - 1] not in open_list:
                    open_list.append(grid[current.x - 1][current.y - 1])
                
            
            open_list.remove(current)
            closed_list.append(current)
    
    return None , None        

cell_size = 20 # Size of each cell in the grid
# Function to draw the grid
def draw_grid(canvas, grid, size, path):
    
    label_frame = tk.Frame(window, bg="black")
    label_frame.pack(side=tk.TOP)  # Place at the top of the window

    # Label for the result
    result_label = tk.Label(label_frame, text=f"Total Cost: {total_cost}\n\n\nGA Path: {' '.join([f'({node.x},{node.y})' for node in population[0]])}\n\n\n\nA-star Path: {' '.join([f'({node.x},{node.y})' for node in complete_path])}", fg="black", bg="white", wraplength=2000)
    result_label.pack(side=tk.TOP, padx=5, pady=5)  # Place at the top of label_frame

    # Canvas frame for the grid
    grid_frame = tk.Frame(window, bg="black")
    grid_frame.pack(side=tk.TOP)  # Place at the top of the window

    
    for i in range(size):
        for j in range(size):
            color = 'red' if grid[i][j].blocked else 'white'
            canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill=color, outline='black')
            found = False

            for _ in path:
                if i == _.x and j == _.y:
                    found = True
                    break

            if found:
                canvas.create_oval(j*cell_size+5, i*cell_size+5, (j+1)*cell_size-5, (i+1)*cell_size-5, fill='green')  # Highlight path in green

    return canvas

# Genetic Algorithm
grid_size = 10
population_size = 10
chromosome_size = 5
population = []

start_node = node()
start_node.x = 2
start_node.y = 3

end_node = node()
end_node.x = 8
end_node.y = 9

# Find the optimal path using A*
optimal_path , optimal_cost = a_star(start = start_node, grid = initialize_grid( size = grid_size, goal = end_node), size = grid_size, goal = end_node)
print(f"Optimal Cost: {optimal_cost}")

# Initialize the population with fixed start and end nodes and random intermediate nodes
for i in range(population_size):
        chromosome = []
        chromosome.append(start_node)

        for i in range(chromosome_size  - 2):
            new_node = node()
            new_node.x = random.randint(0,population_size - 1)
            new_node.y = random.randint(0,population_size - 1)
            chromosome.append(new_node)
            
        chromosome.append(end_node)
        population.append(chromosome)

# Run the genetic algorithm for 20 generations
for _ in range(20):

    fitness = [0 for x in range(population_size)] # fitness array to store the cost of each chromosome
    
    for j in range(population_size):   
        i = 1
        temp_cost = 0
        
        # calculate the cost of each chromosome by running A* algorithm between each pair of genes (nodes)
        while i in range(len(population[j])):
            grid = initialize_grid( size = grid_size, goal = population[j][i])
            
            # check if the node is blocked then find a new node
            if grid[population[j][i].x][population[j][i].y].blocked == True:
                while grid[population[j][i].x][population[j][i].y].blocked == True:
                    population[j][i].x = random.randint(2,population_size - 1)
                    population[j][i].y = random.randint(2,population_size - 1)
                grid = initialize_grid( size = grid_size, goal = population[j][i])
                
            # run A* algorithm
            path , cost = a_star (start = population[j][i - 1], grid = grid, size = grid_size, goal = population[j][i])
            
            # if path is found then add the cost to the total cost
            if cost:
                temp_cost += cost
            i += 1
            
        fitness[j] = temp_cost
        

    # sort fitness array and population array according to fitness array
    for i in range(population_size):
        for j in range(population_size):
            if fitness[i] < fitness[j]:
                temp = fitness[i]
                fitness[i] = fitness[j]
                fitness[j] = temp
                
                temp = population[i]
                population[i] = population[j]
                population[j] = temp

    print(fitness)
    # check if the optimal path is found
    if fitness[0] >= optimal_cost and fitness[0] <= optimal_cost + 3:
        print("Goal Found")
        break

    # perform crossover
    parent1 = population[0]
    parent2 = population[1]
    child1 = []
    child2 = []
    cut_point = random.randint(2, chromosome_size - 1)
    
    # perform crossover
    for i in range(cut_point):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(cut_point,chromosome_size):
        child1.append(parent2[i])
        child2.append(parent1[i])
        
    # perform mutation
    mutation_rate = 0.2 # 20% mutation rate: 20% of the genes will be mutated of each chromosome
    m = 2
    while m in range(chromosome_size -2):
        if random.random() < mutation_rate:
            child1[m].x = random.randint(2,population_size - 1)
            child1[m].y = random.randint(2,population_size - 1)
            m += 1
    
    # generation gap
    generation_gap = 0.1 # 10% generation gap: 10% of the population will be replaced by the best child
    for i in range(int(generation_gap * population_size)):
        chromosome = []
        chromosome.append(start_node)

        for i in range(chromosome_size  - 2):
            new_node = node()
            new_node.x = random.randint(0,population_size - 1)
            new_node.y = random.randint(0,population_size - 1)
            chromosome.append(new_node)
            
        chromosome.append(end_node)
        population[population_size - 1 - i] = chromosome
    
    # replace the worst chromosome with the best child
    population[population_size - 1] = child1
    population[population_size - 2] = child2


 
# sort the population according to the sum of x and y coordinates of each chromosome
sum = []
for i in range(len(population[0])):
    sum.append(population[0][i].x + population[0][i].y)
    
for i in range(len(population[0])):
    for j in range(len(population[0])):
        if sum[i] < sum[j]:
            temp = sum[i]
            sum[i] = sum[j]
            sum[j] = temp
            
            temp = population[0][i]
            population[0][i] = population[0][j]
            population[0][j] = temp
    
# run A* algorithm between each pair of genes (nodes) to find the optimal path
i = 1
total_cost = 0
complete_path = []

while i in range(len(population[0])):    
    
    grid = initialize_grid( size = grid_size, goal = population[0][i])
    path , cost = a_star (start = population[0][i - 1], grid = grid, size = grid_size, goal = population[0][i])
    if cost:
        total_cost += cost
         
    if path:
        for _ in range(len(path)):
            complete_path.append(path[_])
  
    i += 1
    
# remove duplicates
i = 0
while i in range(len(complete_path)):
    j = i + 1
    while j in range(len(complete_path)):
        if complete_path[i].x == complete_path[j].x and complete_path[i].y == complete_path[j].y:
            complete_path.remove(complete_path[j])
            total_cost -= 1
        j += 1
    i += 1

        
# Create GUI window
window = tk.Tk()
window.title("A* Algorithm with Genetic Algorithm Optimization")
window.geometry("600x400")

# Create a canvas frame for the labels
canvas_frame = tk.Frame(window)
canvas_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create a canvas for scrolling
canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create horizontal scrollbar
scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.configure(xscrollcommand=scrollbar.set)

# Bind the canvas to the scrollbar
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
draw_grid(canvas, initialize_grid( size = grid_size, goal = end_node), size = grid_size, path = complete_path)

# Run the tkinter main loop
window.mainloop()