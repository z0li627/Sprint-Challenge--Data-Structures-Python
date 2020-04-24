
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if  self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    def contains(self, target):
        if target == self.value:
            return True
        elif self.right == None and self.left == None:
            return False
        else:
            if self.right != None and self.right.contains(target):
                return True
            if self.left != None and self.left.contains(target):
                return True
