class Trie:

    def __init__(self):
        self.trie = (T := lambda: defaultdict(T))()

    def insert(self, word: str) -> None:
        reduce(getitem,word+"#",self.trie)

    def search(self, word: str) -> bool:
        return "#" in reduce(lambda d, c: d.get(c, {}), word, self.trie)

    def startsWith(self, prefix: str) -> bool:
        return bool(reduce(lambda d, c: d.get(c, {}), prefix, self.trie))
