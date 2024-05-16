import turtle

class Node:
    def __init__(self, x, y, is_wall=False):
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.neighbors = []
        self.parent = None

    def add_neighbor(self, neighbor):
        if not neighbor.is_wall:
            self.neighbors.append(neighbor)

def build_maze():
    grid = [[Node(x, y) for y in range(6)] for x in range(5)]  # 5 rows and 6 columns

    # Example walls, adjust these based on the actual maze from Fig. 1
    grid[1][2].is_wall = True  # Example wall
    grid[3][4].is_wall = True  # Example wall

    # Connect neighbors excluding walls
    for x in range(5):
        for y in range(6):
            if x > 0:
                grid[x][y].add_neighbor(grid[x-1][y])  # Connect Up
            if x < 4:
                grid[x][y].add_neighbor(grid[x+1][y])  # Connect Down
            if y > 0:
                grid[x][y].add_neighbor(grid[x][y-1])  # Connect Left
            if y < 5:
                grid[x][y].add_neighbor(grid[x][y+1])  # Connect Right
    return grid

def bfs_search(start_node, end_node):
    from collections import deque
    queue = deque([start_node])
    visited = set([start_node])
    traced_nodes = []  # To trace the nodes visited
    while queue:
        current = queue.popleft()
        traced_nodes.append(current)
        if current == end_node:
            return build_path(current), traced_nodes
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = current
                queue.append(neighbor)
    return None, traced_nodes

def build_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    return path

def visualize_maze(maze, path, traced_nodes):
    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.penup()
    scale = 50  # Size of each square

    # Function to draw a single square at (x, y)
    def draw_square(x, y, color):
        turtle.goto(x, y)
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(scale - 1)  # Draw square
            turtle.right(90)
        turtle.end_fill()

    # Draw the entire maze
    for row in maze:
        for node in row:
            x, y = node.x * scale - 250, -node.y * scale + 150
            if node.is_wall:
                draw_square(x, y, 'red')
            else:
                draw_square(x, y, 'white')

    # Highlight traced nodes
    for node in traced_nodes:
        x, y = node.x * scale - 250, -node.y * scale + 150
        draw_square(x, y, 'grey')

    # Draw the path
    for node in path:
        x, y = node.x * scale - 250, -node.y * scale + 150
        draw_square(x, y, 'blue')

    turtle.hideturtle()
    turtle.done()

maze = build_maze()
start_node = maze[0][0]  # Start at (0,0) as per your requirement
end_node = maze[4][5]    # End at (4,5) as per your requirement
path, traced_nodes = bfs_search(start_node, end_node)

if path:
    print("Path found:", [(node.x, node.y) for node in path])
else:
    print("No path found")

visualize_maze(maze, path, traced_nodes)
