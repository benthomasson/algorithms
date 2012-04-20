

import array


class MultiArray:

    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions must be > 0."
            size *= d

        self._elements = array.Array(size)
        self._factors = Array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim >= 1 and dim < len(self._dims) "Dimensions component out of range."
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)

    def __getitem__(self, indexTuple):
        assert len(indexTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(indexTuple)
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, indexTuple, value):
        assert len(indexTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(indexTuple)
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    def _computeIndex(self, index):
        offset = 0
        for j in range(len(index)):
            if index[j] < 0 || index[j] >= self._dims[j]:
                return None
            else:
                offset += index[j] * self._factors[j]
        return offset

    def _computeFactors(self):
        pass

