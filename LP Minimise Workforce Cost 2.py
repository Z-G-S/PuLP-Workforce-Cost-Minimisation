import pulp
import pandas as pd 

#Create a linear programming problem
problem = pulp.LpProblem("LP_Minimise_Workforce_Cost", pulp.LpMinimize)

#Define decision variables: Name, Non-negativity, Integer
X1 = pulp.LpVariable("Group X1" , lowBound=0, cat='Integer')
X2 = pulp.LpVariable("Group X2" , lowBound=0, cat='Integer')
Y1 = pulp.LpVariable("Group Y1" , lowBound=0, cat='Integer')
Y2 = pulp.LpVariable("Group Y2" , lowBound=0, cat='Integer')
Y3 = pulp.LpVariable("Group Y3" , lowBound=0, cat='Integer')
Y4 = pulp.LpVariable("Group Y4" , lowBound=0, cat='Integer')
Y5 = pulp.LpVariable("Group Y5" , lowBound=0, cat='Integer')

#Define the objective function (minimise workforce cost)
workforce_cost = 80 * X1 + 80 * X2 + 64 * Y1 + 64 * Y2 + 64 * Y3 + 64 * Y4 + 64 * Y5
problem += workforce_cost

#Consraints (3)
#Demand Constraints (1)
problem += 5 * X1 + 5 * X2 + 5 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 45, "9am-10am"
problem += 5 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 55, "10am-11am"
problem += 5 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 5 * Y3 + 0 * Y4 + 0 * Y5 >= 70, "11am-12pm"
problem += 0 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 5 * Y3 + 5 * Y4 + 0 * Y5 >= 85, "12pm-1pm"
problem += 5 * X1 + 0 * X2 + 0 * Y1 + 5 * Y2 + 5 * Y3 + 5 * Y4 + 5 * Y5 >= 88, "1pm-2pm"
problem += 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 5 * Y3 + 5 * Y4 + 5 * Y5 >= 84, "2pm-3pm"
problem += 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 5 * Y4 + 5 * Y5 >= 70, "3pm-4pm"
problem += 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 5 * Y5 >= 60, "4pm-5pm"

#Maximum and minimum full time and part time workers constraints (2)
problem += 1 * X1 + 1 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 <= 20, "Max full time"
problem += 1 * X1 + 1 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 4, "Min full time"
problem += 0 * X1 + 0 * X2 + 1 * Y1 + 1 * Y2 + 1 * Y3 + 1 * Y4 + 1 * Y5 <= 20, "Max part time"

#Break constraints (3)
problem += X1-X2 >= 0, "BC1"
problem += X1-X2 <= 1, "BC2"
problem += X1>=X2, "BC3"

#Solve the linear program
problem.solve()

#Print results
print("Status:", pulp.LpStatus[problem.status])
print() #blank line

print("Optimal Solution:")
print() #blank line

#Optimal decision variable values
for v in problem.variables():
    print(f"{v.name} = {int(v.varValue)}")
print() #blank line

#Objective function value
print(f"Minimum workforce cost: £{pulp.value(workforce_cost)}")
print() #blank line

print("Workforce cost breakdown:")
print() #blank line
Cost_coefficients = [80, 80, 64, 64, 64, 64, 64, 64]
Variable_values = [X1.varValue, X2.varValue, Y1.varValue, Y2.varValue, Y3.varValue, Y4.varValue, Y5.varValue]
Variable_names = ["X1", "X2", "Y1", "Y2", "Y3", "Y4", "Y5"]
Total_cost = 0 
for Cost_coefficients, Variable_values, Variable_names in zip(Cost_coefficients, Variable_values, Variable_names):
    cost = Cost_coefficients*Variable_values
    Total_cost += cost
    print(f"Cost of Group {Variable_names}: £{cost}")
print(f"Total cost:       £{Total_cost}")
print() #blank line

#Workers and capacity per hour
print("Number of workers and capacity of patients for each hour:")
print() #blank line
removed_constraints = ["Max_full_time", "Min_full_time", "Max_part_time", "BC1", "BC2", "BC3"]
for name, constraint in problem.constraints.items():
    if name not in removed_constraints:
        Capacity = sum([v.varValue * coeff for v, coeff in constraint.items()])
        NumOfWorkers = Capacity/5
        print(f"{name}:")
        print(f"Number of workers: {int(NumOfWorkers)}")
        print(f"Capacity of patients: {int(Capacity)}")
        print()  # Blank line

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack}
for name, c in problem.constraints.items()]
print(pd.DataFrame(o))
df = pd.DataFrame(o)