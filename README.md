# Code Challenge

Python CLI program for finding the shortest path between a start node and a goal node from a CSV graph file.

## Problem Summary

The program should:

- Read graph data from a CSV file
- Treat the graph as bidirectional
- Ask the user for:
  - graph file name
  - start node
  - goal node
- Return the shortest path and total cost

Example rule:

- `A,B,5` means `A -> B = 5` and `B -> A = 5`

## Input Format

The CSV file uses this format:

```csv
start_node,end_node,cost
```

Example:

```csv
A,B,5
A,D,3
A,E,4
B,C,4
E,F,6
C,G,2
D,G,6
G,H,3
H,F,5
I,0,0
```

Notes:

- `I,0,0` is treated as an isolated node
- The program builds both directions automatically

## Project Files

- `main.py` contains the CLI program and shortest-path logic
- `test_main.py` contains unit tests
- `graph.csv` is the sample input file

## How It Works

The solution uses a simple Dijkstra-style search:

1. Load the CSV file into a graph structure
2. Track the best known cost to each node in `distances`
3. Track the previous node in the best path in `previous`
4. Repeatedly visit the unvisited node with the lowest current cost
5. Rebuild the final path by walking backward from the goal node

## Run The Program

On Windows:

```powershell
py -3 main.py
```

Example:

```text
What is graph file name: graph.csv
What is start node?: C
What is goal node?: F
Path from C to F is C->G->H->F, and have cost 10.
```

## Run Tests

```powershell
py -3 -m unittest -v
```

## Test Coverage

The tests cover:

- loading bidirectional edges from CSV
- direct path lookup
- reverse-direction path lookup
- multi-step shortest path
- unreachable node handling
- unknown node handling

## Current Note

The current local version of `main.py` prints intermediate debugging information inside `shortest_path()` such as `current`, `previous`, and `distances`. This is useful for learning and tracing the algorithm, but those print statements can be removed if you want cleaner final CLI output for submission.
