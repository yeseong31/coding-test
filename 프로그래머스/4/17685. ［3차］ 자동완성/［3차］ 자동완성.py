class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            
            node = node.children[c]
            node.count += 1
            
    def find(self, word):
        node = self.root
        
        for i, c in enumerate(word):
            if node.children[c].count == 1:
                return i + 1
            
            node = node.children[c]
    
        return len(word)
        

def solution(words):
    trie = Trie()
    
    for word in words:
        trie.insert(word)
    
    return sum(trie.find(word) for word in words)
