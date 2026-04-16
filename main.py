"""CLI program for finding the shortest path in a bidirectional graph."""


def load_graph(filename):
    """Load graph data from CSV and build a bidirectional adjacency map."""
    graph = {}

    with open(filename, "r", encoding="utf-8") as graph_file:
        for raw_line in graph_file:
            line = raw_line.strip()
            if not line:
                continue

            parts = line.split(",")
            start = parts[0].strip()
            end = parts[1].strip()
            cost = int(parts[2].strip())

            if start not in graph:
                graph[start] = {}

            # Input such as I,0,0 represents an isolated node.
            if end == "0" and cost == 0:
                continue

            if end not in graph:
                graph[end] = {}

            graph[start][end] = cost
            graph[end][start] = cost

    return graph


def find_lowest_distance_node(unvisited, distances):
    """Return the unvisited node that currently has the lowest distance."""
    lowest_node = None
    lowest_distance = float("inf")

    for node in unvisited:
        if distances[node] < lowest_distance:
            lowest_distance = distances[node]
            lowest_node = node

    return lowest_node


def shortest_path(graph, start, goal):
    """Return the shortest path and total cost using a simple Dijkstra search."""
    if start not in graph or goal not in graph:
        return None, None

    distances = {}
    previous = {}
    unvisited = list(graph.keys())

    for node in graph:
        distances[node] = float("inf")
        previous[node] = None

    distances[start] = 0

    # Keep visiting nodes until there are no unvisited nodes left
    # or we have already found the goal.
    while unvisited:
        current = find_lowest_distance_node(unvisited, distances)
        if current is None or distances[current] == float("inf"):
            break

        unvisited.remove(current)
        # print("current:", current)
        if current == goal:
            break

        for neighbor, cost in graph[current].items():
            new_cost = distances[current] + cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current

        # print("previous:", previous)
        # print("distances:", distances)

    if distances[goal] == float("inf"):
        return None, None

    path = []
    current = goal
    # Walk backward from goal to start by following the previous node record.
    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[goal]


def main():
    filename = input("What is graph file name: ").strip()
    start = input("What is start node?: ").strip()
    goal = input("What is goal node?: ").strip()

    graph = load_graph(filename)
    path, cost = shortest_path(graph, start, goal)

    if path is None:
        print(f"No path from {start} to {goal}.")
        return

    print(f"Path from {start} to {goal} is {'->'.join(path)}, and have cost {cost}.")


if __name__ == "__main__":
    main()
