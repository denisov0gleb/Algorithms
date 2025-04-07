class Graph():
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


    def print_graph(self):    
        for key in self.graph:
            print(f"{key} -> {self.graph[key]}")
        print("-"*10)



def test():
    g = Graph()
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

    print(f"Is 'a' connected to 'f'? {g.is_connected('a', 'f')}")
    print(f"Is 'a' connected to 'x'? {g.is_connected('a', 'x')}")



if __name__ == "__main__":
    test()