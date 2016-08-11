import pdb

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return 'Node({self.value})'.format(self=self)

    __repr__ = __str__


def inorder_walk(tree):
    if tree is None:
        return
        
    inorder_walk(tree.left)
    print(tree)
    inorder_walk(tree.right)
    

def search(tree, value):
    if tree == None:
        return None 

    previous = None
    current = tree
    while current is not None:
        previous = current
        if value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
        else:
            return current

    return None
        

def insert(root, node):
    if root is None:
        raise ValueError("nope")

    # Find the correct place for the node
    previous = None
    current = root
    while current is not None:
        previous = current
        if node.value <= current.value:
            current = current.left
        elif node.value > current.value:
            current = current.right

    # current is none here, we have found the right place
    # previous now is the parent of the current root.
    if node.value <= previous.value:
        previous.left = node
    else:
        previous.right = node

    node.parent = previous

            
def max_node(tree):
    if tree is None:
        raise ValueError("Empty tree provided")
    else:
        node = tree
        while node.right is not None:
            node = node.right

        return node


def min_node(tree):
    if tree is None:
        raise ValueError("Empty tree provided")
    else:
        node = tree
        while node.left is not None:
            node = node.left

        return node


def successor(node):
    if node.right is not None:
        return min_node(node.right)

    if node.parent is None:
        return None

    # As long as this node is along the right-child's path (where
    # every node is a right child of the previous node), we will
    # keep getting a smaller value (since this node is the right
    # child, therefore larger than these nodes).
    # Find an ancestor node which is not the right child of it's
    # parent. This node's parent will be larger (since node is
    # the left child) and therefore the successor.
    
    current = node
    parent = node.parent
    while parent is not None and current == parent.right:
        current = parent
        parent = current.parent
        
    return parent


def predecessor(node):
    if node.left is not None:
        return min_node(node.left)

    if node.parent is None:
        return None
    
    current = node
    parent = node.parent
    while parent is not None and current == parent.left:
        current = parent
        parent = current.parent
        
    return parent


def delete_node(tree, node):

    #pdb.set_trace()
    def correctly_setup_children(node, value):
        if node == node.parent.left:
            node.parent.left = value 
        else:
            node.parent.right = value

    # Case: If node has no children, then simply
    # update the parent
    if node.left is None and node.right is None:
        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    #Case: If node has only one child, make it replace
    # the node
    if (node.left is None and node.right is not None):
        if node == node.parent.left:
            node.parent.left = node.right
        else:
            node.parent.right = node.right
            
    elif node.right is None and node.left is not None:
        if node == node.parent.left:
            node.parent.left = node.left
        else:
            node.parent.right = node.left

    # Case: If node has 2 children, then find the successor,
    # which will be in the right tree (because it cannot be in the
    # left tree of the parent because node itself has a right tree
    # in this case), and the successor will not have a left child
    # otherwise a smaller element would be in this left child:

    nxt = successor(node)
    # Case a. Successor is right child of z, then simply replace
    # z with successor

    if nxt == node.right:
        nxt.parent = node.parent
        if node == node.parent.left:
            node.parent.left = nxt
        else:
            node.parent.right = nxt

    # Case b. Successor is not an exact child of the node, but lives
    # a few levels down in the tree.
    # Replace successor by its own right child, and replace z by successor.
    else:
        if nxt == nxt.parent.left:
            nxt.parent.left = nxt.right
        else:
            nxt.parent.right = nxt.right

        nxt.right = node.right
        nxt.left = node.left
        nxt.parent = node.parent

        if node == node.parent.left:
            node.parent.left = nxt
        else:
            node.parent.right = nxt


def a_tree():
    root = Node(10)
    insert(root, Node(5))
    insert(root, Node(7))
    insert(root, Node(18))
    insert(root, Node(1))
    insert(root, Node(8))
    insert(root, Node(9))
    insert(root, Node(16))
    insert(root, Node(21))
    insert(root, Node(14))
    insert(root, Node(17))
    return root
