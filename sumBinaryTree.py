
def sumBinaryTree(node):
    if not node:
        return 0
    else:
        old_value = node.data
        node.data = sumBinaryTree(node.left) + sumBinaryTree(node.right)
        return node.data + old_value
