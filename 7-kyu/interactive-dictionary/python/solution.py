class Dictionary():
    def __init__(self):
        self._dict = {}
        
    def newentry(self, word, definition):
        self._dict[word] = definition
        
    def look(self, key):
        error_message = f"Can\'t find entry for {key}"
        return self._dict.get(key, error_message)