class Trie(object):


    def __init__(self):
        
        self.children={}
        self.isend=False
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self

        for ch in word:
            if ch not in node.children:
                node.children[ch]=Trie()
            node=node.children[ch]
            
        
        node.isend = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node=self

        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        
        return node.isend
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node=self

        for ch in prefix:
            if ch not in node.children:
                return False
            node=node.children[ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)