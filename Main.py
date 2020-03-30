# ---Author: André Gomes Cecchi
# ---Date: 03/29/2020
#
# ---Objective: Solve weighted graphs using Dijkstra's Algorithm
#
# ---Guide:
# -Instantiate the Graph class
# -Use add_nodes to build your graph's nodes and edges
# -The "neighbors" argument of the add_node method takes a dictionary in which the keys are the node names and values the
# distance from the node you are creating and that neighbor
# -Call dijkstra_solution to print the shortest path from "start" to "end" according to Dijkstra's Algorithm


from Graph import Graph


if __name__ == '__main__':
    graph = Graph()

    graph.add_node(name='A', neighbors={'B': 5, 'C': 4})
    graph.add_node(name='B', neighbors={'A': 5, 'C': 4, 'D': 1, 'E': 7})
    graph.add_node(name='C', neighbors={'A': 4, 'B': 4, 'E': 8, 'F': 10})
    graph.add_node(name='D', neighbors={'B': 1, 'E': 1})
    graph.add_node(name='E', neighbors={'B': 7, 'C': 8, 'D': 1, 'F': 2})
    graph.add_node(name='F', neighbors={'C': 10, 'E': 2})

    graph.dijkstra_solution(start='A', end="F")