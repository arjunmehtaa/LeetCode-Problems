class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(head, word):
            for i in range(len(word)):
                if word[i] == ".":
                    for node in head.children.values():
                        if dfs(node, word[i+1:]):
                            return True
                    return False
                if word[i] not in head.children:
                    return False
                head = head.children[word[i]]
            return head.isEnd
        
        return dfs(self.root, word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)