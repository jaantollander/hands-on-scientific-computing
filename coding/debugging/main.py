#!/usr/bin/env python3
import sys

from graph import Graph

if __name__ == "__main__":
    # The edge file is given as a command line argument
    if len(sys.argv) < 2 :
        print("Usage: python main.py graph.edges")
        sys.exit(1)
    graphfile = sys.argv[1]

    # The edges in graph.edges will be stored in a list
    edgelist = []
    with open(graphfile, 'r') as graph:
        for edge in graph:
            u, v = edge.split(" ")
            edgelist.append((int(u), int(v)))

    # Calculate the graph's diameter
    graph = Graph(edgelist)
    print('The diameter of the graph with edges stored ' \
            'in the {} is {}.' .format(graphfile, graph.diameter()))
