# 111. Minimum Depth of Binary Tree || Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

## Intuition
I decided to go with a BFS approach. This would reduce the number of steps taken to find the minimum depth of the tree. 
By going row by row, when no children are found for a node the depth is returned. A DFS approch would force us to check
both the left and right sides of the tree to guarantee the minimum depth is found.

## Approach
BFS (Breadth-First Search): A row by row search allows us to exit early if the end condition is found.
Queue: By using a queue we can guarantee that every node is checked in order.

## Complexity

n = the number of nodes in the binary tree.

- Time complexity: O(n)

- Space complexity: O(n)
