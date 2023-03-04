
import gurobipy as gp
#import GRB
from gurobipy import GRB
#how to import queen from chap1
#import file queen.py từ thư mục chap1
#sửa lỗi no module named chap1
from queen import Queen

#xep quan hau tren ban cờ nxn sao cho 1 quân hậu tấn công tối đa k quân hậu khác

class GurobiQueenAttackKSolve:
    def __init__(self,n,k):
        self.n = n
        self.k = k
        self.model = gp.Model("QueenAttackK")
        #tao n x n bien xij
        self.x = [[self.model.addVar(
            vtype=GRB.BINARY, lb = 0, ub= 1, name = f'x_{i}_{j}')
              for i in range(n)] for j in range(n)]
    
    def setSubVars(self):
        #left la bien self.nxself.n
        self.left = [[self.model.addVar(
            vtype=GRB.BINARY,lb=0, ub=1,  name = f'left_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        
        #left <=x
        #right la bien self.nxself.n
        self.right = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'right_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        
        #top la bien self.nxself.n
        self.up = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'up_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        self.down = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'down_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        self.left_up = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'left_up_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        self.left_down = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'left_down_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        self.right_up = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'right_up_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        self.right_down = [[self.model.addVar(
            vtype=GRB.BINARY,  name = f'right_down_{i}_{j}')
             for i in range(self.n)] for j in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                self.model.addConstr(self.left[i][j] >= self.x[i][j])
                self.model.addConstr(self.right[i][j] >= self.x[i][j])
                self.model.addConstr(self.up[i][j] >= self.x[i][j])
                self.model.addConstr(self.down[i][j] >= self.x[i][j])
                self.model.addConstr(self.left_up[i][j] >= self.x[i][j])
                self.model.addConstr(self.left_down[i][j] >= self.x[i][j])
                self.model.addConstr(self.right_up[i][j] >= self.x[i][j])
                self.model.addConstr(self.right_down[i][j] >= self.x[i][j])
                self.setConstraintLeft(i,j)
                self.setConstraintRight(i,j)
                self.setConstraintUp(i,j)
                self.setConstraintDown(i,j)
                self.setConstraintLeftUp(i,j)
                self.setConstraintLeftDown(i,j)
                self.setConstraintRightUp(i,j)
                self.setConstraintRightDown(i,j)
    def setConstraintLeft(self,i,j):
        if(j==0):
            return
        self.model.addConstr(self.left[i][j] >= self.left[i][j-1])
    def setConstraintRight(self, i, j):
                if(j==self.n-1):
                    return
                self.model.addConstr(self.right[i][j] >= self.right[i][j+1])
    def setConstraintUp(self,i,j):
                if(i==0):
                    return
                self.model.addConstr(self.up[i][j] >= self.up[i-1][j])
    def setConstraintDown(self,i,j):
                if(i==self.n-1):
                    return
                self.model.addConstr(self.down[i][j] >= self.down[i+1][j])
    def setConstraintLeftUp(self,i,j):
        if(i==0 or j==0):
            return
        self.model.addConstr(self.left_up[i][j] >= self.left_up[i-1][j-1])
    def setConstraintLeftDown(self,i,j):
        if(i==self.n-1 or j==0):
            return
        self.model.addConstr(self.left_down[i][j] >= self.left_down[i+1][j-1])
    def setConstraintRightUp(self,i,j):
        if(i==0 or j==self.n-1):
            return
        self.model.addConstr(self.right_up[i][j] >= self.right_up[i-1][j+1])
    def setConstraintRightDown(self,i,j):
        if(i==self.n-1 or j==self.n-1):
            return
        self.model.addConstr(self.right_down[i][j] >= self.right_down[i+1][j+1])
    def solve(self):
        self.setSubVars()
        self.setConstraints()
        self.setObjective()
        self.model.optimize()
        return self.getSolution()
    def setConstraints(self):
        for i in range(self.n):
           for j in range(self.n):
                attackList =[]
                if(i>0):
                    attackList.append(self.up[i-1][j])  
                if(i<self.n-1):
                    attackList.append(self.down[i+1][j]) 
                if(j>0):
                    attackList.append(self.left[i][j-1])
                if(j<self.n-1):
                    attackList.append(self.right[i][j+1])
                if(i>0 and j>0):
                    attackList.append(self.left_up[i-1][j-1])
                if(i<self.n-1 and j>0):
                    attackList.append(self.left_down[i+1][j-1])
                if(i>0 and j<self.n-1):
                    attackList.append(self.right_up[i-1][j+1])
                if(i<self.n-1 and j<self.n-1):
                    attackList.append(self.right_down[i+1][j+1])
                M= len(attackList)
                self.model.addConstr(
                   sum(attackList) <= M*(1-self.x[i][j]) + self.k*self.x[i][j], 
                   name="c_%s_%s" % (i,j))
    def setObjective(self):
        #tổng các ô bàn cờ
        self.model.setObjective(sum([sum(self.x[i]) for i in range(self.n)]),
                                 sense=GRB.MAXIMIZE)
    def getSolution(self):
        solution = []
        for i in range(self.n):
            for j in range(self.n):
                if self.x[i][j].x !=0:
                    solution.append(Queen(i,j))
        return solution
               

















