

import ctypes


class Array:

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def _check_bounds(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"

    def __getitem__(self, index):
        self._check_bounds(index)
        return self._elements[index]

    def __setitem__(self, index, value):
        self._check_bounds(index)
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curIndex = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curIndex < len(self._arrayRef):
            entry = self._arrayRef[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration
