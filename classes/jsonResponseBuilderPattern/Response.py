class Response:
    def __init__(self):
        self.items = []
        pass
    def add(self, item):
        self.items.append(item)
    def build(self):
        json = {}
        for x in self.items:
            json[x.key] = x.value
        return json
