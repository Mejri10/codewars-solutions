class running_average(float):
    def __init__(self, cache=0, count=0):
        self.cache = cache
        self.count = count
    def __call__(self, n):
        self.cache += n
        self.count += 1
        return round(self.cache/self.count, 2)