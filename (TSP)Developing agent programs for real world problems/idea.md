- Consider city 1 as the starting and ending point. Since the route is cyclic, we can consider any point as a starting point.
- Generate all (n-1)! permutations of cities.
- Calculate the cost of every permutation and keep track of the minimum cost permutation.
`Return the permutation with minimum cost.`



The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once
Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle.
[reference](https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/)
