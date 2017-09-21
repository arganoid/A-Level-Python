class Graph:
    def __init__(self, adjacency_list):
        # in this case I'm using a dictionary to store our adjacency list so we can quickly look up the neighbours of any
        # node based on its name
        self.adjacency_list = adjacency_list

    def is_connected(self, node1, node2):
        # in python, dictionary.get(x) is same as dictionary[x] except it won't crash
        # if there's no such key as x in the dictionary.
        node1_list = self.adjacency_list.get(node1)
        if node1_list == None:
            return False
        else:
            for item in node1_list:
                if item == node2:
                    return True
            return False

            # python also allows you to use 'in' to find out if an item is in a list
            # so as an alternative to the above you could do the following:
            #return node2 in node1_list

    def test1(self):
        print(self.is_connected('A', 'C'))
        print(self.is_connected('E', 'B'))
        print(self.is_connected('A', 'E'))
        print(self.is_connected('X', 'A'))


    # is_connected() function uses dictionary.get() to ensure it doesn't crash if there is no such key in the dictionary.
    # Here are two alternative ways of achieving that:

    def test2(self):
        node = 'X'
        if node in adjacency_list:
            node_list = self.adjacency_list[node]
            print(node_list)
        else:
            print("No such item: " + node)

    def test3(self):
        try:
            node = 'X'
            node_list = self.adjacency_list[node]
            print(node_list)
        except KeyError:
            print("No such item: " + node)


    def traverse_depth_first(self, first_node):
        visited = {}
        self.traverse_depth_first_visit(first_node, visited)

    def traverse_depth_first_visit(self, current_node, visited):
        print(current_node)
        visited[current_node] = True
        for connected_node in self.adjacency_list[current_node]:
            if not connected_node in visited:
                self.traverse_depth_first_visit(connected_node, visited)


    def traverse_breadth_first(self, first_node):
        visited = {}
        to_visit_queue = [first_node]
        while len(to_visit_queue) > 0:
            current_node = to_visit_queue[0]
            visited[current_node] = True
            print(current_node)
            for new_value in self.adjacency_list[current_node]:
                if not new_value in visited and not new_value in to_visit_queue:
                    to_visit_queue.append(new_value)
            del to_visit_queue[0]


# in this case I'm using a dictionary to store our adjacency list so we can quickly look up the neighbours of any
# node based on its name
adjacency_list = {}

# graph from figure 12.2
adjacency_list['A'] = ['B']
adjacency_list['B'] = ['A', 'C', 'E']
adjacency_list['C'] = ['B', 'D']
adjacency_list['D'] = ['C', 'E']
adjacency_list['E'] = ['B', 'D']

#circular_adjacency_list = { 'A':['B','E'], 'B':['C'], 'C':['D','Z'], 'D':['E'], 'E':['A', 'D'], 'Z':['C'] }

my_graph = Graph(adjacency_list)

#my_graph.test1()
#my_graph.test2()
#my_graph.test3()
#my_graph.traverse_depth_first('A')
#my_graph.traverse_breadth_first('A')
