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
                
    def find_sum(self):
        #start with the value of current node
        total = self.data
        
        if self.left:#check if there is a right child of current node
            total += self.left.find_sum()#add the left child to the total
            
        if self.right:#check if  there is a left child of current node
            total += self.right.find_sum()#add the right child to the total
            
            
        return total

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
    
    def pre_order_traversal(self):
        elements = [self.data]#visit the base node first
        #visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        #visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        #visit the left tree
        if self.left:
            elements += self.left.post_order_traversal()
        #visit the right tree
        if self.right:
            elements +=  self.right.post_order_traversal()
        #visit the base node
        elements.append(self.data)
        return elements
    
    # as we know that left tree node is always smaller than the parent node (In Binary search tree), so the minimum element will be the leftmost of the tree 
    def find_min(self):
        current = self
        #loop down to find the leftmost leaf
        while current.left:
            current = current.left
        return current.data
    def find_max(self):
        current = self
        #loop down to find the rightmost leaf
        while current.right:
            current = current.right
        return current.data
    
        
    
    

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    # Insert remaining elements into the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    elements = [17,4,1,20,9,23,18,34]
    tree = build_tree(elements)
    
    
    print("In order traversal of the tree:",tree.in_order_traversal())
    print("The minimum value in the tree is",tree.find_min())
    print("The maximum value in the tree is",tree.find_max())
    print("The sum of this tree is ",tree.find_sum())
    print("The pre order traversal of this tree is",tree.pre_order_traversal())
    print("Post order traversal of this tree will be",tree.post_order_traversal())