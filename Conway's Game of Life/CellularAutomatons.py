class CellularAutomatons(object):
    """base class for cellular automaton"""
    __cells = list()
    __size = tuple()
    def __init__(self, *size):
        self.__size = size
        return self
    def FieldLooped():
        """Returns a value indicating whether the field is looped"""
        return None
    def GetCells():
        return __cells
    def GetCell(*index):
        if len(index)!=len(__size):
            raise IndexError()
        return __cells[map(lambda x,y: x*y,__size[:-1],index[:-1])+index[-1]]
    def NextStep():
        """Returns the next state of the cellular automaton"""
        return None

    class GameOfLife(CellularAutomatons):
        def FieldLooped():
            return False
        d