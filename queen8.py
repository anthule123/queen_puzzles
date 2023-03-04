import gurobipy as gp
from gurobipy import GRB

model = gp.Model("queen8")
#tạo biến 8x8
x = model.addVars(8,8,vtype=GRB.BINARY,name="x")
for i in range(8):
    attackList = []
    for j in range(8):
        attackList.append(x[i,j])
    model.addConstr(sum(attackList) <= 1)
for j in range(8):
    attackList = []
    for i in range(8):
        attackList.append(x[i,j])
    model.addConstr(sum(attackList) <= 1)
#set objective
model.setObjective(
    sum(x[i,j] for i in range(8) for j in range(8))
    , sense=GRB.MAXIMIZE)
model.optimize()

