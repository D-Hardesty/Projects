# Intuition
I decided to go with a BFS approach. This would reduce the number of steps taken to find the minimum depth of the tree. 
By going row by row, the first time no children are found for a node the depth is returned. Unlike a DFS approach, where 
both the left and right sides of the tree would need to be checked to guarantee the minimum depth has been found. 

# Approach
BFS (Breadth-First Search): A row by row search allows us to exit early if the end condition is found.
Queue: By using a queue we can guarantee that every node is checked in order.

# Complexity

n = the number of nodes in the binary tree.

- Time complexity: O(n)

- Space complexity: O(n)
