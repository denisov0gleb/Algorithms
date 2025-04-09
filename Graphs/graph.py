class Unweighted_Graph():
    def __init__(self):
        self.graph = {}


    def add_node(self, node, links):
        links = set(links)
        if not self.graph or node not in self.graph:
            self.graph[node] = links
        else:
            self.graph[node].update(links)
        for neighbor_node in links:
            if neighbor_node in self.graph:
                self.graph[neighbor_node].update([node])
            else:
                self.add_node(neighbor_node, [node])
        return self.graph
    

    def add_nodes_dict(self, node_dict):
        for node in node_dict:
            self.add_node(node, node_dict[node])        
        return self.graph


    def is_connected(self, start_node, search_node):
        search_queue = list(self.graph.get(start_node))
        searched = set()
        while search_queue:
            data = search_queue.pop(0)
            for neighbor_node in self.graph[data]:
                if data not in searched:
                    search_queue.append(neighbor_node)
                    searched.add(neighbor_node)
                if neighbor_node == search_node:
                    return True
        return False   


    def add_connection(self, node_1, node_2):
        self.add_node(node_1, [node_2])
        return self.graph


    def delete_node(self, node):
        if self.graph and node in self.graph:
            for neighbor_node in self.graph[node]:
                self.graph[neighbor_node].discard(node) # better than 'remove' cause no Error is raised
            self.graph.pop(node, None) # my choice instead of `del self.graph(node)`
        return self.graph


    def delete_connection(self, node_1, node_2):
        if self.graph and node_1 in self.graph and node_2 in self.graph:
            if node_2 in self.graph[node_1]:
                self.graph[node_1].discard(node_2)
            if node_1 in self.graph[node_2]:
                self.graph[node_2].discard(node_1)
        return self.graph


    def BFS(self, start_node):
        distances = {}
        for node in self.graph:
            distances[node] = [float('inf'), None]
        distances[start_node] = [0, start_node]
        queue = [(0, start_node)]
        while queue:
            parent_value, current_node = queue.pop(0)
            for neighbor_node in self.graph[current_node]:
                if parent_value + 1 < distances[neighbor_node][0]:
                    distances[neighbor_node] = [ parent_value + 1, current_node ]
                    queue.append( (distances[neighbor_node][0],  neighbor_node) )
        return distances


    def print_BFS(self, start_node, search_node, distances):
        path = []
        if distances[search_node][0] < float('inf'):
            current_node = search_node
            while current_node != start_node:
                path.insert(0, current_node)
                current_node = distances[current_node][1]
            path.insert(0, start_node)
        return path


    def print_graph(self):    
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
        print("-"*10)



class Weighted_Graph():
    def __init__(self):
        self.graph = {}


    def add_node(self, node, links_dict):
        if not self.graph or node not in self.graph:
            self.graph[node] = links_dict
        else:
            self.graph[node].update(links_dict)
        for neighbor_node in links_dict:
            if neighbor_node in self.graph:
                self.graph[neighbor_node].update({node: links_dict[neighbor_node]})
            else:
                self.add_node(neighbor_node, {node: links_dict[neighbor_node]})
        return self.graph
    

    def add_nodes_dict(self, node_dict):
        for node in node_dict:
            self.add_node(node, node_dict[node])        
        return self.graph


    def print_graph(self):    
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
        print("-"*10)


    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        parents = {node: None for node in self.graph}
        queue = [(0, start_node)]

        while queue:
            current_distance, current_node = queue.pop(0)
            if current_distance <= distances[current_node]:
                for neighbor_node, weight in self.graph[current_node].items():
                    neighbor_distance = current_distance + weight

                    if neighbor_distance < distances[neighbor_node]:
                        distances[neighbor_node] = neighbor_distance
                        parents[neighbor_node] = current_node
                        queue.append((neighbor_distance, neighbor_node))
        return distances, parents
    

    def print_dijkstra(self, start_node, end_node, parents):
        path = []
        if start_node in parents and end_node in parents and parents[end_node]:
            current_node = end_node
            while parents[current_node]:
                path.insert(0, current_node)
                current_node = parents[current_node]
            path.insert(0, start_node)
        return path



def test_unweighted_graph():
    g = Unweighted_Graph()
    g.add_node('a', ['x'])
    g.add_node('x', [])
    g.add_node('y', ['x'])
    g.add_connection('a', 'y')
    g.print_graph()
    g.delete_connection('a', 'x')
    g.print_graph()

    g.delete_node('y')
    g.add_nodes_dict({'b': ['a', 'c'], 'd': ['e', 'f', 'a', 'a'], 'a': ['b', 'd']})
    g.print_graph()

    print(f"BFS. Is 'a' connected to 'f'? {g.is_connected('a', 'f')}")
    print(f"BFS. Is 'a' connected to 'x'? {g.is_connected('a', 'x')}")

    dist = g.BFS('a')
    print(f"BFS. Path from 'a' to 'f' is {g.print_BFS('a', 'f', dist)}")


def test_weighted_graph():
    gw = Weighted_Graph()
    gw.add_node('a', {'b' : 1, 'c' : 2})
    gw.print_graph()

    gw.add_node('c', {'d' : 10, 'a' : 5})
    gw.print_graph()

    gw.add_nodes_dict({'e': {'a' : 3, 'b' : 5}, 'f' : {'g' : 12, 'b' : 2}})
    gw.print_graph()
    d, p = gw.dijkstra('a')
    print(f"Dijkstra for 'a': {d}")
    print(f"Dijkstra. Path from 'a' to 'g' is {gw.print_dijkstra('a', 'g', p)}")



if __name__ == "__main__":
    test_unweighted_graph()
    print()
    test_weighted_graph()