# Course Notes 
https://www.coursera.org/learn/discrete-optimization

Linear programming, Constraint programming, MIP: Finds optimal solution for small problems but doesn’t scale well

Local search: Finds solution with lower quality, but scales better.



# Constraint programming: 
Uses branch and prune. Finds a feasible solution (no optimization function)
Each constraint needs to:
* Check feasibility
* Prune the search space (limit the domain of some of the variables) 
Each constraint is checked separately. 
Constraint types:
* regular constraints: 
* global constraints: like Lego building blocks. Handle multiple variables at once. Examples:
	* all_different
	* table constraint: specify a subset of all var values combinations as being legal.
	* Lexicographical ordering
	* At most

Symmetry: we want to break it, to reduce the search space.
Many types. For example: Var symmetry, value symmetry.
We can add constraints that break the symmetry for ex. Impose lexicographical order 
Redundant constraints: Don’t change the set of feasible solutions, but speedup search. Surrogate constraints – a linear combination of existing constraints – can provide a global view. 

Dual modeling: model the problem in 2 ways and join them to 1 model.

Searching the search space: “first-fail” – search first where you are more likely to fail.
Searching in constraint programming :
*	variable/value labeling: first choose variable, then assign value. (start with variables with the smallest domain, choose value with the least variable)
*	value/variable labeling: first choose value, then assign it to a variable
*	domain splitting (assigning a weak constraint, lake x > 10, and not an actual value)
*	focusing on the objective 
*	symmetry breaking during search 
*	randomization and restarts

# Local Search
### Tabu search
Keep a list of nodes you have already visited, and don't go back there.
*  short term memory:
  * For efficiency, keep only the last ones 
  * More efficient: keep an abstraction of the suffix. for example: not allowing to repeat a swap for K moves.
* Aspiration: takin a move that is tabu, but leads to a very good objective function
* Diffrentiation: the term for calculating the objective function of potential swaps without performing them.

