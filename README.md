# DijkstraAlgorithmPython

Simple implementation of a Dijkstra algorithm in Python.

# How to use

Instantiate the Graph class.

```
graph = Graph()
```

Build your graph. The "neighbors" argument of the add_node method takes a dictionary in which the keys are the node names and values the distance from the node you are creating and that neighbor.

```
graph.add_node(name='A', neighbors={'B': 5, 'C': 4})
graph.add_node(name='B', neighbors={'A': 5, 'C': 4, 'D': 1, 'E': 7})
graph.add_node(name='C', neighbors={'A': 4, 'B': 4, 'E': 8, 'F': 10})
graph.add_node(name='D', neighbors={'B': 1, 'E': 1})
graph.add_node(name='E', neighbors={'B': 7, 'C': 8, 'D': 1, 'F': 2})
graph.add_node(name='F', neighbors={'C': 10, 'E': 2})
```

To solve the graph you build, simply call the dijkstra_solution method. The "start" argument is the desired starting node and the "end" argument is the end node. The program shall then print out the minimum distance and path, according to Dijkstra's Algorithm.

```
graph.dijkstra_solution(start='A', end="F")
```