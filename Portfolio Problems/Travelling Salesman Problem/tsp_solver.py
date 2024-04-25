import numpy as np
import math

def get_node_quantity():
    """
    A function to obtain a number of nodes for the TSP problem

    Args:
        None
    
    Returns:
        nodes (int): The number of nodes for the TSP problem.
    """
    while True:
        try:
            nodes = int(input('How many nodes (e.g. cities) are there?'))
            if nodes < 2:
                raise ValueError("Number of nodes must be an integer greater than 1.")
            else:
                return nodes
        except ValueError as e:
            print(e)
            print('Please enter an integer greater than 1.')


def tsp_costs_matrix():
    """
    This function generates a matrix containing the costs (e.g. costs)
    between nodes based on user input. The returned matrix, costs, is
    constructed such that costs[i][j] represents the cost of travelling from
    node i to node j.

    Args:
        None

    Returns:
        costs (2D array): An array such that costs[i][j] is the cost of
            travelling between node i and node j.  

    """
    # Get the user inputs ensuring valid input
    # A value error can arise from casting to int so try/except
    
    size = get_node_quantity()
    
    while True:
        symmetry = input("Are the costs independent of direction? ('yes'/'no')").lower().strip()
        if not ((symmetry == 'yes') or (symmetry == 'no')):
            print('Please enter only "yes" or "no".')
        else:
            break

    #Try/except for value errors are needed for the inputs due to float cast
    num_error_string = "Please enter a valid cost (without units)."
    costs = np.zeros([size, size])
    print('Note: In the questions nodes are 1-indexed')
    for row in range(size):
        for cell in range(size):
            if cell > row:
                while True:
                    try: 
                        costs[row][cell] = float(input(f"What is the cost from node {row+1} to node {cell+1}"))
                        break
                    except ValueError as e:
                        print(e)
                        print(num_error_string)
            elif cell == row:
                pass
            else:
                if symmetry == 'yes':
                    costs[row][cell] = costs[cell][row]
                else:
                    try:
                        costs[row][cell] = float(input(f"What is the cost from node {row+1} to node {cell+1}"))
                        break
                    except ValueError as e:
                        print(e)
                        print(num_error_string)
    
    return costs


def tsp_cartesian_costs():
    """
    This function generates a matrix of costs based on the user' inputs of 
    a number of nodes' relative cartesian coordinates. The resulting matrix is
    inherently symmetrical and can be used for the solution of the travelling
    salesman problem

    Args:
        None
    
    Returns:
        costs (2D array): An array such that costs[i][j] is the cost of
            travelling between node i and node j. 
    """
    # Get number of nodes then populate the coordinates array
    nodes = get_node_quantity()
    coordinates = np.zeros([nodes, 2])
    for node in range(nodes):
        while True:
            try:
                # 1-indexing used for human readability
                coordinates[node][0] = float(input(f"What is the X coordinate of node {node+1}?"))
                coordinates[node][1] = float(input(f"What is the Y coordinate of node {node+1}?"))
                break
            except ValueError as e:
                print(e)
                print(f"Please enter valid coordinates (no units) for node {node+1} starting with X")   

    # Construct the costs matrix from the coordinates matrix
    # The 2D euclidian distance is the same as the linalg norm
    costs = np.zeros([nodes, nodes])
    for node1, xy in enumerate(coordinates):
        for node2 in range(node1+1, len(coordinates)):
            costs[node1][node2] = np.linalg.norm(coordinates[node2]-coordinates[node1])
            costs[node2][node1] = costs[node1][node2]
    
    return costs            


def tsp_solver(costs, node=0, visited_mask=0):
    """
    This function returns the solution of the travelling salesman problem (TSP)
    when provided with a square matrix of costs such that costs[i][j]
    represents the cost of travelling from node i to node j. To construct
    the costs matrix, condier using one of the functions tsp_costs_matrix()
    or tsp_cartesian_costs().

    Args:
        costs (2D array): An array such that costs[i][j] is the cost of
            travelling between node i and node j.
        node (int): The starting node. Does not affect resulting total
            cost.
        visited_mask (int): A bitmask that tracks the visited nodes.
            Could be changed for diffent path length calculations but
            not for TSP solution.
    
    Returns:
        lowest_cost (float): The lowest possible cost of a tour that
            visits all other nodes from the starting node and then returns
            to the starting node.
        path (list of strings): The path taken by the lowest cost cycle. This
            list is zero-indexed (it will start and end from node zero).
    """
    # Array for recording the path
    path = []
    # If all of the nodes have been visited (full mask) return final cost
    if visited_mask == ((1 << len(costs)) - 1):
        path.append(0)
        return costs[node][0], path
    # Otherwise return shortest tour of remaining unvisited
    else:
        lowest_cost = float('inf')
        # Get unvisited nodes from mask
        for next_node in range(len(costs)):
            if not (1 << next_node & visited_mask):
                next_mask = visited_mask | (1 << next_node)
                candidate_cost, candidate_path = tsp_solver(costs, next_node, next_mask)
                candidate_cost += costs[node][next_node]
                if candidate_cost < lowest_cost:
                    lowest_cost = candidate_cost
                    path = [next_node] + candidate_path
        return lowest_cost, path
