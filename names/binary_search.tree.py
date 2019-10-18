class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # # LEFT CASE
        # # check if the new nodes value is less than our current ones value
        # if value < self.value:
        #     # if the is no left child,
        #     if self.left: 
        #         # place a new node here
        #         self.left.insert(value)
        #     # otherwise
        #     else:
        #         # repeat process for left
        #         self.left = BinarySearchTree(value)
        # # RIGHT CASE
        # # check if the new nodes value is greater than or equal to the current parent value
        # elif value > self.value:
        #     # if there is no right child here,
        #     if self.right: 
        #         # place a new one
        #         self.right.insert(value)
        #     # otherwise
        #     else:
        #         # repeat process right
        #         self.right = BinarySearchTree(value)
        
        # iterative approach
        new_node = BinarySearchTree(value)
        current_node = self
        parent = None
        
        while current_node:
          parent = current_node

          if current_node.value > value:
            current_node = current_node.left
          
          elif current_node.value < value:
            current_node = current_node.right 
          
        if parent.value > value:
          parent.left = new_node
        elif parent.value < value:
          parent.right = new_node
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        if self.value == target:
          return True
        # LEFT CASE
        elif self.value > target:
          if self.left == None:
            return False
          return self.left.contains(target)
        # RIGHT CASE
        else: #(if self.value < target)
          if self.right == None:
            return False
          return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE 
        # if empty tree
        if self.value == None:
            # return none
            return None
        
        # RECURSIVE
        # if the the is no right value
        if self.right == None: 
            # return the root value
            return self.value
        # return the get max of the the right node
        return self.right.get_max()

        # ITTERATIVE
        # set a max value variable to keep track of max value
        # get a ref to current node
        # check if we are at a valid tree node
            # if our current value is greater than the max value
                # update the max value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
        # return our max value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # # base case
        if self.right is None and self.left is None:
        #   return
            return
        else:
        #  left case
            if self.left:
                self.left.for_each(cb)
        #   right case
            if self.right:
                 self.right.for_each(cb)