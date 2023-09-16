class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.head = Node()
        
    def insert(self, word: str) -> None:
        i = 0
        curr = self.head
        while i < len(word):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            curr = curr.children[word[i]]
            i += 1
        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        curr = self.head
        i = 0
        while i < len(word):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
            i += 1
        return curr.isEnd
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        i = 0
        while i < len(prefix):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
            i += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)