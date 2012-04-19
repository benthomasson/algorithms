

import array

class Array2D:

    def __init__(self, numRows, numCols):
        self._theRows = array.Array(numRows)

        for i in range(numRows):
            self._theRows[i] = array.Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)

    def _check_bounds(self,indexTuple):
        assert len(indexTuple) == 2, "Invalid number of array subscripts."
        row, col = indexTuple
        assert (row >= 0 and row < self.numRows() and
                col >= 0 and col < self.numCols()), "Array subscript out of range."
        the1dArray = self._theRows[row]
        return indexTuple

    def __getitem__(self, indexTuple):
        row, col = self._check_bounds(indexTuple)
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, indexTuple, value):
        row, col = self._check_bounds(indexTuple)
        the1dArray = self._theRows[row]
        the1dArray[col] = value
