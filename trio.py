class Node(object):
    def __init__(self):
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.data = "/"
