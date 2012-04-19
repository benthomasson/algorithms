
import array2d

class Matrix(object):

    def __init__(self, numRows, numCols):
        self._theGrid = array2d.Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, indexTuple):
        return self._theGrid[indexTuple[0], indexTuple[1]]

    def __setitem__(self, indexTuple, scalar):
        self._theGrid(indexTuple[0], indexTuple[1]] = scalar

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols):
                self[r,c] *= scalar

    def transpose(self):
        pass

    def __add__(self, rhsMatrix):
        pass

    def __sub__(self, rhsMatrix):
        pass

    def __mul__(self, rhsMatrix):
        pass

