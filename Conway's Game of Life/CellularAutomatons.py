class GameOfLife(CellularAutomatons):
    __looped = None
    __hight = 0
    __width = 0
    __cells = list()
    __birthconst = 3
    __underpopulationconst = 1
    __overpopulationconst = 4


    def __init__(self,hight,width,looped):
        self.__looped = looped
        self.__hight = hight
        self.__width = width
        return self
    def SetConst(self,birth,underpopulation,overpopulation):
        self.__birthconst = birth
        self.__underpopulationconst = underpopulation
        self.__overpopulationconst = overpopulation
    def FieldLooped(self):
            return self.__looped
    def GetDimensionality(self):
            return 2
    def GetSize(self):
        return tuple([self.__width,self.__hight])
    def __len__(self):
        return len(self.__cells)
    def ____getitem__(self, x,y):

        looped = self.FieldLooped()
        xIsCorrect = 0<=x<self.__width
        yIsCorrect = 0<=y<self.__hight
        if xIsCorrect and yIsCorrect:
            return __cells[x+y*self.__width]
        else:
            if looped:
                return __cells[x%self.__width+(y%self.__hight)*self.__width]
            else:
                return 0
    def __setitem__(self,x,y,value):
        looped = self.FieldLooped()
        xIsCorrect = 0<=x<self.__width
        yIsCorrect = 0<=y<self.__hight
        if xIsCorrect and yIsCorrect:
            __cells[x+y*self.__width] = value
        else:
            if looped:
                __cells[x%self.__width+(y%self.__hight)*self.__width] = value
            else:
                raise IndexError()
    def __delitem__(self, x,y):
        self[x,y]=0
    def __iter__(self):
        return iter(self.__cells)
    def SurroundingCells(self,x,y):
        return [self[x-1,y-1],self[x,y-1],self[x+1,y-1],self[x-1,y],self[x+1,y],self[x-1,y+1],self[x,y+1],self[x+1,y+1]]
    def NextStep(self):
        newStates = list()
        for i in xrange(__width):
            for j in xrange(__hight):
                state = self[i,j]
                around = sum(self.SurroundingCells(x,y))
                if state == 0:
                    if around==self.__birthconst:
                        newStates.append(1)
                    else:
                        newStates.append(0)
                else:
                    if self.__underpopulationconst<around<self.__overpopulationconst:
                        newStates.append(1)
                    else:
                        newStates.append(0)
        self.__cells = newStates

