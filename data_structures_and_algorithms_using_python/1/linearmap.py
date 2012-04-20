

class Map:

    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        index = self._findPosition(key)
        return index is not None

    def add(self,key,value):
        index = self._findPosition(key)
        if index is not None:
            self._entryList[index].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def _check_index(self,key):
        index = self._findPosition(key)
        assert index is not None, "Invalid map key"
        return index

    def valueOf(self, key):
        index = self._check_index(key)
        return self._entryList[index].value

    def remove(self, key):
        index = self._check_index(key)
        self._entryList.pop(index)

    def __iter__(self):
        return _MapInterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
