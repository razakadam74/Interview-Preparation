class Node(Object):

    __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    


class Tree(Object):

    __init__(self, root_data):
        self.root = Node(root_data)


    addLeft(node, data):
        if not node.left:
            node.left = Node(data)
            return node
        else:
            return self.addLeft(node.left, data)

    addRight(node, data):
        if not

    