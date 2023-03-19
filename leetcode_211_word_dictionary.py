class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        if len(word) not in self.words:
            self.words[len(word)] = []
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.words:
            return False
        # findableWords = filter(lambda w: len(w) == len(word), self.words)
        findableWords = self.words[len(word)]
        for value in findableWords:
            foundCtr = 0
            for i in range(len(word)):
                if word[i] == value[i] or word[i] == ".":
                    foundCtr += 1
                else:
                    break
            if foundCtr == len(word):
                return True 
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

### Notes: Could've used DFS to solve this but trie-map came to mind first
### Challenge faced: Time running out as dataset got bigger with 5-7k `findableWords`
