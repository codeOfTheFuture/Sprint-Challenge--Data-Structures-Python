class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
        else:
            self.value = value


    def contains(self, target):
        if self.value:
            if target == self.value:
                return True
            elif target < self.value and self.left:
                return self.left.contains(target)
            elif target > self.value and self.right:
                return self.right.contains(target)
        return False

   
