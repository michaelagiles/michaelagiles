# Travelling Salesman Problem Solver

## The Problem
The [travelling salesman problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem) is a famous problem that asks the question:

>Given a list of cities and the distances between each pair of cities, what is
the shortest possible route that visits each city exactly once and returns to
the origin city?

One possible solution is to calculate each possible tour and select the one
with the minimum length. However, this incurs a running time of O(*n*!) which
quickly becomes infeasible for large numbers of cities. However, using
recursion this can be reduced to O(*n*<sup>2</sup>2<sup>*n*</sup>). Please note
that this is still exponential and for large *n* approximate solutions may be
required.

The TSP does not only apply to distances but any cost between nodes, therefore,
the cost matrix does not have to be symmetrical (e.g. the cost of travelling
from node 1 to node 2 may not be the same as travelling from node 2 to node 1).

## How to Use the Solver
The functions used for solving this problem are contained in the file
`tsp_solver.py`. There is the main solver function `tsp_solver` and two
supplementary functions that offer a user-friendly way of constructing the
costs graph. 

### `tsp_solver(costs, node=0, visited_mask=0)`

This function takes in a matrix `costs` which is a 2D square array where the
entry `costs[i][j]` represents the cost associated with travelling **from node 
_i_ to node _j_**. `costs[j][i]` represents the cost of travelling **from node
_j_ to node _i_** and may be different depending on the nature of the TSP. 

The other arguments are for the recursion in the program. It is not necessary
to change `node` because the optimal tour is a Hamiltonian cycle, the starting
node does not change it. Finding cycles of a subset of nodes is possible by
changing the `visited_mask` but this should really be left alone.

`tsp_solver` returns as a tuple, the shortest cycle length and the path itself.
The path is given as a list of node numbers.

### Cost Matrix Builder Functions 

There are two functions designed to help create costs matrices for the TSP.
Both ask for user-input using 1-indexing for better human-readability.

#### `tsp_costs_matrix()`

This is the first function that constructs the costs matrix by asking the user
to input the costs between each pair of nodes. It will ask if the costs are the
same in each direction to avoid redundant questions. The function takes no
arguments. For example:

```
costs_matrix = tsp_costs_matrix()
total_cost, shortest_cycle = tsp_solver(costs_matrix)
```

#### `tsp_cartesian_costs()`

The second function that constructs the costs matrix from user-input does so
from the cartesian coordinates (2D) of the nodes. This is naturally more suited
to distances as the crow flies and will return a symmetrical costs matrix. For
example:

```
costs_matrix = tsp_cartesian_costs()
total_cost, shortest_cycle = tsp_solver(costs_matrix)
```

### Example

Using [this example graph from GeeksforGeeks:](https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/)

![Graph of a 4 node TSP](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Euler12.png)


#### Costs Matrix Construction

The costs matrix can be produced using `tsp_costs_matrix()`:

```
costs_matrix = tsp_costs_matrix()
print(costs_matrix)
```

Output with sample user input:

```
How many nodes (e.g. cities) are there?
4
Are the costs independent of direction? ('yes'/'no')
yes
Note: In the questions nodes are 1-indexed
What is the cost from node 1 to node 2
10
What is the cost from node 1 to node 3
15
What is the cost from node 1 to node 4
20
What is the cost from node 2 to node 3
35
What is the cost from node 2 to node 4
25
What is the cost from node 3 to node 4
30
[[ 0. 10. 15. 20.]
 [10.  0. 35. 25.]
 [15. 35.  0. 30.]
 [20. 25. 30.  0.]]
```

This output can then used to get the solution to the TSP:

```
distance, path = tsp_solver(costs_matrix)
print(distance)
print(path)
```

Output:

```
80
[0, 1, 3, 2, 0]
```

Remembering that the returned path is zero indexed in case it will be used
in further python processing etc.

## Helpful Resources
These resources helped me to understand the problem:
- [TSP on Wikipedia](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- [TSP using Dynamic Programming - GeeksforGeeks](https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/)