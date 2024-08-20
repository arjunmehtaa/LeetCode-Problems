class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self.compare(self.root, word)
    
    def compare(self, node, word):
        for i in range(len(word)):
            if word[i] == ".":
                for child in node.children.values():
                    if self.compare(child, word[i + 1:]):
                        return True
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)