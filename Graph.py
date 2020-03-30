class Node:
    def __init__(self, name, edges_raw):
        self.name = name
        self.edges_raw = edges_raw
        self.edges = {}
        self.distance_from_start = None
        self.path_origin = ''


class Graph:
    def __init__(self):
        self.node_list = []
        self.start = ''
        self.end = ''

    def add_node(self, **kwargs):
        new_node = Node(kwargs['name'], kwargs['neighbors'])

        self.node_list.append(new_node)

    def names_to_objects(self):
        for node in self.node_list:
            for neighbor_name, neighbor_distance in node.edges_raw.items():
                for node2 in self.node_list:
                    if neighbor_name == node2.name:
                        node.edges[node2] = neighbor_distance

    def print_results(self):
        end_node = None
        for node in self.node_list:
            if node.name == self.end:
                end_node = node
                break

        path = []
        dijkstra_distance = end_node.distance_from_start
        current_node = end_node
        while self.start not in path:
            path.append(current_node.name)
            current_node = current_node.path_origin
        path.reverse()

        path_result = ''
        for node_name in path:
            path_result += node_name + ' -> '
        path_result = path_result[:-4]

        print(f'Shortest path according to Dijkstra\'s algorithm:\nDistance: {dijkstra_distance} | Path: {path_result}')

    def dijkstra_solution(self, **kwargs):
        self.start = kwargs['start']
        self.end = kwargs['end']
        visited_nodes = []
        current_node = None
        end_node = None

        # Creating a List of Nodes out of the List of Strings
        self.names_to_objects()

        # Dijkstra algorithm
        # Step 1: Assign 0 distance from start to the start node and infinite distance to the rest (already assigned
        # as None). Also set the start node as the current node
        # Step 2: Calculate the distance between the current node and its neighbors
        # Step 3: Put the current node in the array of visited nodes
        # Step 4: If the end node is marked as visited, end the algorithm
        # Step 5: Mark the neighbor node closest to the current node as the new current node and go back to Step 2

        # Step 1
        for node in self.node_list:
            if node.name == self.start:
                current_node = node
                current_node.distance_from_start = 0
                break

        for i in range(len(self.node_list)):
            # Step 2
            shortest_distance_from_start = None
            closest_node = None

            if current_node is not None:
                for neighbor_node, distance in current_node.edges.items():
                    if neighbor_node not in visited_nodes:
                        if neighbor_node.distance_from_start is None:
                            neighbor_node.distance_from_start = current_node.distance_from_start + distance
                            neighbor_node.path_origin = current_node
                        elif current_node.distance_from_start + distance < neighbor_node.distance_from_start:
                            neighbor_node.distance_from_start = current_node.distance_from_start + distance
                            neighbor_node.path_origin = current_node

                        if shortest_distance_from_start is None or neighbor_node.distance_from_start < shortest_distance_from_start:
                            closest_node = neighbor_node
                            shortest_distance_from_start = neighbor_node.distance_from_start

                # Step 3
                visited_nodes.append(current_node)

                # Step 4
                if self.end in visited_nodes:
                    break

                # Step 5
                current_node = closest_node

        self.print_results()