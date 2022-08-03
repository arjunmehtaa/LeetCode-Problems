# Let L be the length of the word to be inserted/searched
# Time Complexity   : O(L) (for methods)
# Space Complexity  : O(N) (generally), O(L) (for methods)

class TrieNode:
    def __init__(self):
        self. isEnd = False
        self.keys = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, node = None):
        if node == None:
            node = self.root
        if len(word) == 0:
            node.isEnd = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        else:
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node = None):
        if node == None:
            node = self.root
        if len(word) == 0 and node.isEnd:
            return True
        elif len(word) == 0:
            return False
        elif word[0] not in node.keys:
            return False
        else:
            return self.search(word[1:], node.keys[word[0]])

    def starts_with(self, prefix, node = None):
        if node == None:
            node = self.root
        if len(prefix) == 0:
            return True
        elif prefix[0] not in node.keys:
            return False
        else:
            return self.starts_with(prefix[1:], node.keys[prefix[0]])
        
trie = Trie()
trie.insert("apple")
print(trie.search("dog"))
trie.insert("dog")
print(trie.search("dog"))
print(trie.starts_with("app"))
print(trie.search("app"))
trie.insert("app")
print(trie.search("app"))
