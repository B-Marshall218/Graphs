"""
Vertex =ancestor 
edge = child/parent
DFS for this so use stack 
"""
from util_ancestor import Stack, Queue  # These may come in handy
from collections import deque, defaultdict


# def earliest_ancestor(ancestors, starting_node):
#     visited = set()
#     stack = deque()
#     graph = create_graph(ancestors)
#     stack.append((starting_node, 0))
#     earliestAncestor = (starting_node, 0)

#     while len(stack) > 0:
#         current = stack.pop()
#         currNode, distance = current[0], current[1]
#         visited.add(current)

#         if currNode not in graph:
#             if distance > earliestAncestor[1]:
#                 earliestAncestor = current
#             elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
#                 earliestAncestor = current
#         else:
#             for ancestor in graph[currNode]:
#                 if ancestor not in visited:
#                     stack.append((ancestor, distance) + 1)
#     return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

def earliest_ancestor(ancestors, starting_node):
    # child pair with no parent
    graph = create_graph(ancestors)
    stack = Stack()
    stack.push((starting_node, 0))  # distance from node
    visited = set()
    earliestAncestor = (starting_node, 0)

    while stack.size() > 0:
        current = stack.pop()
        currNode, distance = current[0], current[1]
        visited.add(current)

        if currNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = current
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = current
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.push((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def create_graph(edges):
    graph = defaultdict(set)

    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
