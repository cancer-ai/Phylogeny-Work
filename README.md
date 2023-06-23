# Phylogeny-Work

Contained is a binary tree traveral code that accepts a binary tree and returns all of the preorder paths starting with the root node. It also returns incomplete paths, i.e. a path starting at the root node and ending at a non-leaf node. An example is shown below:

# Example usage
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Count and store all possible preorder traversal paths
preorder_paths = count_preorder_paths(root)

# Print the paths
print("All possible preorder traversal paths:")
for path in preorder_paths:
    print(path)
print("Total number of traversal paths:",len(preorder_paths))
#running the example produces the following output:
#All possible preorder traversal paths:
#[1]
#[1, 2]
#[1, 2, 4]
#[1, 2, 5]
#[1, 3]
#[1, 3, 6]
#[1, 3, 7]
#Total number of traversal paths: 7
