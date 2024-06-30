class BinarySearchTreeNode:
    def __init__(self, data):
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

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    # Insert remaining elements into the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ['India', 'Japan', 'South Korea', 'Turkey', 'Serbia', 'Malaysia', 'Japan']
    country_tree = build_tree(countries)

    # Search for countries in the tree
    print("Turkey is in the list?", country_tree.search("Turkey"))
    print("USA is in the list?", country_tree.search("USA"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # Print the elements in in-order traversal
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())

        
        