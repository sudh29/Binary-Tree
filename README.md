# Binary-Tree

[0 Level order traversal](0_Level_order_traversal.py)

[1 Reverse Level Order traversal](1_Reverse_Level_Order_traversal.py)

[2 Height of a tree](2_Height_of_a_tree.py)

[3 Diameter of a tree](3_Diameter_of_a_tree.py)

[4 Mirror of a tree](4_Mirror_of_a_tree.py)

[5 Inorder Traversal](5_Inorder_Traversal.py)

[6 Preorder Traversal](6_Preorder_Traversal.py)

[7 Postorder Traversal](7_Postorder_Traversal.py)

[8 Left View tree](8_Left_View_tree.py)

[9 Right View Tree](9_Right_View_Tree.py)

[10 Top View tree](10_Top_View_tree.py)

[11 Bottom View tree](11_Bottom_View_tree.py)

[12 Zig Zag tree](12_Zig_Zag_tree.py)

[13 Check tree balanced or not](13_Check_tree_balanced_or_not.py)

[14 Diagonal Traversal tree](14_Diagonal_Traversal_tree.py)

[15 Boundary traversal tree](15_Boundary_traversal_tree.py)

[16 Construct Binary Tree String Bracket Representation](16_Construct_Binary_Tree_String_Bracket_Representation.py)

[17 Convert Binary tree Doubly Linked List](17_Convert_Binary_tree_Doubly_Linked_List.py)

[18 Convert Binary tree Sum tree](18_Convert_Binary_tree_Sum_tree.py)

[19 Construct Binary tree from Inorder and preorder traversal](19_Construct_Binary_tree_from_Inorder_and_preorder_traversal.py)

[20 Find minimum swaps required convert Binary tree into BST](20_Find_minimum_swaps_required_convert_Binary_tree_into_BST.py)

[21 Check if Binary tree is Sum tree or not](21_Check_if_Binary_tree_is_Sum_tree_or_not.py)

[22 Leaf at same level](22_Leaf_at_same_leve.py)

[23 Check Binary Tree duplicate subtrees](23_Check_Binary_Tree_duplicate_subtrees.py)

[24 Check Mirror N-ary tree](24_Check_Mirror_N-ary_tree.py)

[25 Sum Nodes Longest path from root leaf node](25_Sum_Nodes_Longest_path_from_root_leaf_node.py)

[26 Check graph tree or not](26_Check_graph_tree_or_not.py)

[27 Find Largest subtree sum tree](27_Find_Largest_subtree_sum_tree.py)

[28 Maximum Sum nodes Binary tree adjacent](28_Maximum_Sum_nodes_Binary_tree_adjacent.py)

[29 Print all K Sum paths Binary tree](29_Print_all_K_Sum_paths_Binary_tree.py)

[30 Find LCA Binary tree](30_Find_LCA_Binary_tree.py)

[31 Find distance between nodes Binary tree](31_Find_distance_between_nodes_Binary_tree.py)

[32 Kth Ancestor node Binary tree](32_Kth_Ancestor_node_Binary_tree.py)

[33 Find all Duplicate subtrees Binary tree](33_Find_all_Duplicate_subtrees_Binary_tree.py)

[34 Tree Isomorphism Problem](34_Tree_Isomorphism_Problem.py)


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

