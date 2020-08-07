class Node:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.data = "/"

    def addWord(self, word):
        currentNode = self.root

        for i, character in enumerate(word):
            if character not in currentNode.children:
                prefix = word[0:i+1]
                currentNode.children[character] = Node(prefix)
            currentNode = currentNode.children[character]
        currentNode.isWord = True

    def find(self, word):
        currentNode = self.root
        for character in word:
            if character not in currentNode.children:
                return None
            currentNode = currentNode.children[character]
        if currentNode.isWord:
            return True

    def begin_with(self, prefix):
        words = list()
        currentNode = self.root
        for character in prefix:
            if character not in currentNode.children:
                # Could also just return words since it's empty by default
                return list()
            currentNode = currentNode.children[character]
        self.child_words(currentNode, words)
        return words
    
    def child_words(self, node, words):
        if node.isWord:
            words.append(node.text)
        for letter in node.children:
            self.child_words(node.children[letter], words)

    def height(self, currentNode = None):
        # By default, get the size of the whole trie, starting at the root
        if not currentNode:
            currentNode = self.root
        count = 1
        for letter in currentNode.children:
            count += self.size(currentNode.children[letter])
        return count


if __name__ == '__main__':
    trie = Trie()
    trie.addWord('apple')
    trie.addWord('app')
    trie.addWord('aposematic')
    trie.addWord('appreciate')
    trie.addWord('book')
    trie.addWord('bad')
    trie.addWord('bear')
    trie.addWord('bat')
    print(trie.begin_with('app'))
    print(trie.find('book'))