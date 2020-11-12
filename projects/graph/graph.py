"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, from_v1, to_v2):
        """
        Add a directed edge to the graph.
        """
        if from_v1 not in self.vertices or to_v2 not in self.vertices:
            print("attempting to remove edges from absent vertex")
        self.vertices[from_v1].add(to_v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        # add neighbors to que to track
        queue = Queue()
        # add vertexs to the que
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            # when theres something in que
            currNode = queue.dequeue()
            # the oldest que gets removed
            # ?? But wouldnt that be popright?
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                # If the currNode hasnt already been visited, print it
                for neighbor in self.get_neighbors(currNode):
                    # attach current node to a neighbor giving it edges
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        # add neighbors to que to track
        stack = Stack()
        # add vertexs to the que
        stack.push(starting_vertex)
        while stack.size() > 0:
            # when theres something in que
            currNode = stack.pop()
            # the oldest que gets removed
            # ?? But wouldnt that be popright?
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                # If the currNode hasnt already been visited, print it
                for neighbor in self.vertices[currNode]:
                    # attach current node to a neighbor giving it edges
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # IF the vertex has not been visited, add it to visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            # when we create new node in the graph,
            # call recursion and pass in the new node
            # and the property of whether or not it has
            # been visited already
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        # pushes the entire path onto the stack, not just
        # a single vertex
        queue.append([starting_vertex])
        while len(queue) > 0:
            currPath = queue.popleft()
        # the current node you're on, is the current node
        # in the path ???
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    # make a list copy of current path
                    newPath = list(currPath)
                    # adding edges from neighbors to new path
                    newPath.append(neighbor)
                    # adding new path to stack
                    queue.append(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = deque()
        # pushes the entire path onto the stack, not just
        # a single vertex
        stack.append([starting_vertex])
        while len(stack) > 0:
            currPath = stack.pop()
        # the current node you're on, is the current node
        # in the path ???
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    # make a list copy of current path
                    newPath = list(currPath)
                    # adding edges from neighbors to new path
                    newPath.append(neighbor)
                    # adding new path to stack
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        if starting_vertex not in path:
            path = [starting_vertex]
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                newPath = path + [neighbor]
                if neighbor == destination_vertex:
                    return newPath
                dfs_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, newPath)
                if dfs_path is not None:
                    return dfs_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
