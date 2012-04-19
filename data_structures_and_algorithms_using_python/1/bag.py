

class Bag:

    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def remove(self, item):
        assert item in self._items, "The item must be in the bag."
        index = self._theItems.index(item)
        return self._theItems.pop( index )

    def __iter__(self, item):
        pass
