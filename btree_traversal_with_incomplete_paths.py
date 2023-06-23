#!/usr/bin/env python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_preorder_paths(root, path=None):
    if root is None:
        return []

    if path is None:
        path = []

    # Add current node's data to the path
    path.append(root.data)

    # Base case: leaf node
    if root.left is None and root.right is None:
        return [path]

    # Recursively calculate paths from left and right subtrees
    left_paths = count_preorder_paths(root.left, path.copy())
    right_paths = count_preorder_paths(root.right, path.copy())

    # Combine paths from left and right subtrees
    paths = [path] + left_paths + right_paths

    return paths
