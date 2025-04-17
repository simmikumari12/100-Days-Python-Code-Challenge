class Node:
    def __init__(self, value):
        # The value is the person's number (0, 1, 2, ..., n-1)
        self.value = value
        self.next = None  # Pointer to the next node in the circular list


def counting_out_game(n, k):
    # Create a circular linked list with n nodes
    head = Node(0)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    current.next = head  # Make the list circular

    # Start the elimination game
    current = head
    while current.next != current:  # Keep going until only one node is left
        for _ in range(k - 1):  # Move k-1 steps forward
            current = current.next
        # current is now the person to be eliminated
        current.value = current.next.value
        current.next = current.next.next

    return current.value  # The last remaining person's number


# Example usage:
n = 11  # Number of people
k = 8   # Number of steps in the rhyme
# Output: 8 (zero-based index of the last person remaining)
print(counting_out_game(n, k))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_info(node):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def count_leaves(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return count_leaves(node.left) + count_leaves(node.right)

    def is_full(node):
        if not node:
            return True
        if (node.left and not node.right) or (not node.left and node.right):
            return False
        return is_full(node.left) and is_full(node.right)

    def is_balanced(node):
        if not node:
            return True
        left_height = height(node.left)
        right_height = height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)

    # Calculate and print the required information
    # Height of the tree (root node height is 0)
    tree_height = height(node) - 1
    leaf_count = count_leaves(node)
    full = "Yes" if is_full(node) else "No"
    balanced = "Yes" if is_balanced(node) else "No"

    print(f"Height of the tree: {tree_height}")
    print(f"Number of leaf nodes: {leaf_count}")
    print(f"Is Full: {full}")
    print(f"Is Balanced: {balanced}")


# Example usage:
# Constructing the tree as described in the problem statement
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

tree_info(root)
