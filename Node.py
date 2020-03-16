# Node class
class Node:
    def __init__(self, value, char):
        self.value  = value
        self.char   = char
        self.left   = None
        self.right  = None

    def __add__(self, node):
        return Node(self.value + node.value, None)

    def __lt__(self, node):
        return self.value < node.value
    
    def __gt__(self, node):
        return self.value > node.value
    
    def __eq__(self, node):
        return self.value == node.value

