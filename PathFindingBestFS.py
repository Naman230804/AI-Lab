import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append((cost, neighbor))
        self.graph[neighbor].append((cost, node))  # Assuming an undirected graph

    def best_first_search(self, start, goal, heuristic):
        priority_queue = []
        heapq.heappush(priority_queue, (heuristic[start], start))  # Push (heuristic, node)
        visited = set()

        while priority_queue:
            _, current = heapq.heappop(priority_queue)

            if current in visited:
                continue
            visited.add(current)

            print(f"Visiting: {current}")

            if current == goal:
                print("Goal reached!")
                return True

            for cost, neighbor in self.graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic.get(neighbor, float('inf')), neighbor))

        print("Path not found")
        return False


# Predefined heuristic values
heuristic = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 0  # Lower is better
}

# Taking user input for graph
graph = Graph()
num_edges = int(input("Enter the number of edges: "))

print("Enter edges in the format: node1 node2 cost")
for _ in range(num_edges):
    node1, node2, cost = input().split()
    graph.add_edge(node1, node2, int(cost))

# Taking start and goal nodes
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Running Best First Search
graph.best_first_search(start, goal, heuristic)
