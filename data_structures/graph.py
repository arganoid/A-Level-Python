class Graph:
    def __init__(self):
        # in this case I'm using a dictionary to store our adjacency list so we can quickly look up the neighbours of any
        # node based on its name
        self.node_adjacency_lists = {}   # e.g. {'A': ['B', 'C'], 'B': ['A'], 'C': ['A', 'B'] }

    def insert(self, start, destination):
        if start not in self.node_adjacency_lists:
            self.node_adjacency_lists[start] = [destination]
        elif destination not in self.node_adjacency_lists[start]:
            self.node_adjacency_lists[start].append(destination)

        if destination not in self.node_adjacency_lists:
            self.node_adjacency_lists[destination] = [start]
        elif start not in self.node_adjacency_lists[destination]:
                self.node_adjacency_lists[destination].append(start)

    def is_connected(self, node1, node2):
        # in python, dictionary.get(x) is same as dictionary[x] except it won't crash
        # if there's no such key as x in the dictionary.
        node1_list = self.node_adjacency_lists.get(node1)
        if node1_list is None:
            return False
        else:
            for item in node1_list:
                if item == node2:
                    return True
            return False

            # python also allows you to use 'in' to find out if an item is in a list
            # so as an alternative to the above you could do the following:
            #return node2 in node1_list

    def is_fully_connected(self):
        num_nodes = len(self.node_adjacency_lists)
        for node,node_list in self.node_adjacency_lists.items():
            if len(node_list) != num_nodes - 1:
                return False
        return True

    def test1(self):
        print(self.is_connected('A', 'C'))
        print(self.is_connected('E', 'B'))
        print(self.is_connected('A', 'E'))
        print(self.is_connected('X', 'A'))
        print(self.is_fully_connected())

    # is_connected() function uses dictionary.get() to ensure it doesn't crash if there is no such key in the dictionary.
    # Here are two alternative ways of achieving that:

    def test2(self):
        node = 'X'
        if node in self.node_adjacency_lists:
            node_list = self.node_adjacency_lists[node]
            print(node_list)
        else:
            print("No such item: " + node)

    def test3(self):
        try:
            node = 'X'
            node_list = self.node_adjacency_lists[node]
            print(node_list)
        except KeyError:
            print("No such item: " + node)

    def traverse_depth_first(self, first_node):
        visited = set()
        self.traverse_depth_first_visit(first_node, visited)

    def traverse_depth_first_visit(self, current_node, visited):
        print(current_node)
        visited.add(current_node)
        for connected_node in self.node_adjacency_lists[current_node]:
            if connected_node not in visited:
                self.traverse_depth_first_visit(connected_node, visited)

    def traverse_breadth_first(self, first_node):
        visited = set()
        to_visit_queue = [first_node]
        while len(to_visit_queue) > 0:
            current_node = to_visit_queue[0]
            visited.add(current_node)
            print(current_node)
            for connected_node in self.node_adjacency_lists[current_node]:
                if connected_node not in visited and connected_node not in to_visit_queue:
                    to_visit_queue.append(connected_node)
            del to_visit_queue[0]

def GetTestGraph():
    graph = Graph()
    graph.insert('A', 'B')
    graph.insert('A', 'C')
    graph.insert('B', 'C')
    return graph

if __name__ == "__main__":
    my_graph = GetTestGraph()
    my_graph.test1()
    my_graph.test2()
    my_graph.test3()
    my_graph.traverse_depth_first('A')
    my_graph.traverse_breadth_first('A')
