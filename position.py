

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def isAttackedRow(self,other):
        return self.y == other.y
    def isAttackedCol(self,other):
        return self.x == other.x
    def isAttackedDiag(self,other):
        return abs(self.x - other.x) == abs(self.y - other.y)
    def isAttackedBy(self,other):
        return self.isAttackedRow(other) or self.isAttackedCol(other) or self.isAttackedDiag(other)
    