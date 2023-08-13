import pulp 
import math

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
Hour_one_9am_to_10am = 5 * X1 + 5 * X2 + 5 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 45
Hour_two_10am_to_11am = 5 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 55
Hour_three_11am_to_12pm = 5 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 5 * Y3 + 0 * Y4 + 0 * Y5 >= 70
Hour_four_12pm_to_1pm = 0 * X1 + 5 * X2 + 5 * Y1 + 5 * Y2 + 5 * Y3 + 5 * Y4 + 0 * Y5 >= 85
Hour_five_1pm_to_2pm = 5 * X1 + 0 * X2 + 0 * Y1 + 5 * Y2 + 5 * Y3 + 5 * Y4 + 5 * Y5 >= 88
Hour_six_2pm_to_3pm = 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 5 * Y3 + 5 * Y4 + 5 * Y5 >= 84
Hour_seven_3pm_to_4pm = 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 5 * Y4 + 5 * Y5 >= 70
Hour_eight_4pm_to_10am = 5 * X1 + 5 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 5 * Y5 >= 60

problem += Hour_one_9am_to_10am
problem += Hour_two_10am_to_11am
problem += Hour_three_11am_to_12pm
problem += Hour_four_12pm_to_1pm
problem += Hour_five_1pm_to_2pm
problem += Hour_six_2pm_to_3pm
problem += Hour_seven_3pm_to_4pm
problem += Hour_eight_4pm_to_10am

#Maximum and minimum full time and part time workers constraints (2)
Max_full_time = 1 * X1 + 1 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 <= 20
Min_full_time = 1 * X1 + 1 * X2 + 0 * Y1 + 0 * Y2 + 0 * Y3 + 0 * Y4 + 0 * Y5 >= 4
Max_part_time = 0 * X1 + 0 * X2 + 1 * Y1 + 1 * Y2 + 1 * Y3 + 1 * Y4 + 1 * Y5 <= 20

problem += Max_full_time
problem += Min_full_time
problem += Max_part_time

#Break constraints (3)
Break_constraint_1 = X1-X2 >= 0
Break_constraint_2 = X1-X2 <= 1

problem += Break_constraint_1
problem += Break_constraint_2

#Solve the linear program
problem.solve()

#Print results
print("Status:", pulp.LpStatus[problem.status])
print("Optimal Solution:")
print("Number of workers in group X1:", int(X1.varValue))
print("Number of workers in group X2:", int(X2.varValue))
print("Number of workers in group Y1:", int(Y1.varValue))
print("Number of workers in group Y2:", int(Y2.varValue))
print("Number of workers in group Y3:", int(Y3.varValue))
print("Number of workers in group Y4:", int(Y4.varValue))
print("Number of workers in group Y5:", int(Y5.varValue))
print("Total Cost: £", pulp.value(workforce_cost))