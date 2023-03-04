
class Queen:
    def __init__(self, col, row):
        self.col = col
        self.row = row
    def __str__(self):
        return f"Queen at ({self.col}, {self.row})"
    def __repr__(self):
        return f"Queen at ({self.col}, {self.row})"
    def doesAttack(self, queen):
        if self.col == queen.col or self.row == queen.row:
            return True
        if abs(self.col - queen.col) == abs(self.row - queen.row):
            return True
        return False
        
    