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
    g.add_node(1, [9])
    g.add_node(9, [])
    g.add_node(10, [9])
    g.add_connection(1, 10)
    g.print_graph()
    g.delete_connection(1, 9)
    g.print_graph()

    g.delete_node(10)
    g.add_nodes_dict({2: [1, 3], 4: [5, 6, 1, 1], 1: [2, 4]})
    g.print_graph()

    print(f"Is 1 connected to 6? {g.is_connected(1, 6)}")
    print(f"Is 1 connected to 9? {g.is_connected(1, 9)}")



if __name__ == "__main__":
    test()