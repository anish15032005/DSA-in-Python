class BinarySearchTreeNode:
    def __init__(self, data):
        # Initialize node with data, left, and right children as None
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # If the data already exists, do nothing
        if data == self.data:
            return

        # If the data is less than the current node's data, go to the left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # If the data is greater than the current node's data, go to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        # If the current node's data matches the value, return True
        if self.data == value:
            return True
        # If the value is less than the current node's data, search in the left subtree
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        # If the value is greater than the current node's data, search in the right subtree
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
       if self.left is None:#if you are the leftmost element, return yourself
           return self.data
       return self.left.find_min()#else go to the leftmost element
   
    def find_max(self):
        if self.right is None:#if you are the rightmost element, return yourself
            return self.data
        return self.right.find_max()
       
    

    def in_order_traversal(self):
        elements = []
        # Traverse the left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit the current node
        elements.append(self.data)

        # Traverse the right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, value):
        # If value is lesser, delete the element from left subtree
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        # If value is greater, delete the element from right subtree
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # If the node is a leaf, return None
            if self.left is None and self.right is None:
                return None
            # If the node has no left child, return the right child
            if self.left is None:
                return self.right
            # If the node has no right child, return the left child
            if self.right is None:
                return self.left
            # Find the minimum value in the right subtree
            min_value = self.right.find_min()
            # Replace the node's data with the minimum value
            self.data = min_value
            self.right = self.right.delete(min_value)
            
        return self
    
def build_tree(elements):
    # print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    # Insert remaining elements into the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal before deletion: ",numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("In order traversal after deletion: ",numbers_tree.in_order_traversal())
