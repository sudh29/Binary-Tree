

# Binary-Tree

In a tree structure, Depth First Search (DFS) and Breadth First Search (BFS) algorithms are used to traverse the nodes. Here's how they work:

# Depth First Search (DFS):

DFS explores as far as possible along each branch before backtracking. It starts at the root node and explores as far as possible along each branch before backtracking.
There are three types of DFS: Pre-order, In-order, and Post-order.
Pre-order: Visit the current node, then recursively visit the left subtree, and then recursively visit the right subtree.
In-order: Recursively visit the left subtree, visit the current node, and then recursively visit the right subtree.
Post-order: Recursively visit the left subtree, recursively visit the right subtree, and then visit the current node.

# Breadth First Search (BFS):

BFS explores neighbors of the current vertex before moving to the next level of vertices.
It starts at the root node and explores all the neighbor nodes at the present depth before moving on to the nodes at the next depth level.
BFS uses a queue data structure to keep track of the nodes to be visited next.

## Below are the Python implementations of DFS and BFS for a binary tree:

```python 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search (DFS) implementations
def dfs_preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    dfs_preorder(node.left)
    dfs_preorder(node.right)

def dfs_inorder(node):
    if node is None:
        return
    dfs_inorder(node.left)
    print(node.val, end=' ')
    dfs_inorder(node.right)

def dfs_postorder(node):
    if node is None:
        return
    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.val, end=' ')

# Breadth First Search (BFS) implementation
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Output of different DFS traversals
print("DFS Pre-order:")
dfs_preorder(root)  # Output: 1 2 4 5 3
print("\nDFS In-order:")
dfs_inorder(root)   # Output: 4 2 5 1 3
print("\nDFS Post-order:")
dfs_postorder(root) # Output: 4 5 2 3 1

# Output of BFS traversal
print("\nBFS:")
bfs(root)  # Output: 1 2 3 4 5
```

