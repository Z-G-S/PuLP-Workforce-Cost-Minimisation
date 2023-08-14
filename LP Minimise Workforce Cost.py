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

#Number of workers in each hour interval
NumOfWorkers_9am_to_10am = int(X1.varValue) + int(X2.varValue) + int(Y1.varValue)
NumOfWorkers_10am_to_11am = int(X1.varValue) + int(X2.varValue) + int(Y1.varValue) + int(Y2.varValue)
NumOfWorkers_11am_to_12pm = int(X1.varValue) + int(X2.varValue) + int(Y1.varValue) + int(Y2.varValue) + int(Y3.varValue)
NumOfWorkers_12pm_to_1pm = int(X2.varValue) + int(Y1.varValue) + int(Y2.varValue) + int(Y3.varValue) + int(Y4.varValue)
NumOfWorkers_1pm_to_2pm = int(X1.varValue) + int(Y2.varValue) + int(Y3.varValue) + int(Y4.varValue) + int(Y5.varValue)
NumOfWorkers_2pm_to_3pm = int(X1.varValue) + int(X2.varValue) + int(Y3.varValue) + int(Y4.varValue) + int(Y5.varValue)
NumOfWorkers_3pm_to_4pm = int(X1.varValue) + int(X2.varValue) + int(Y4.varValue) + int(Y5.varValue)
NumOfWorkers_4pm_to_5pm = int(X1.varValue) + int(X2.varValue) + int(Y5.varValue)

#Capacity per hour
Capacity_9am_to_10am = NumOfWorkers_9am_to_10am * 5
Capacity_10am_to_11am = NumOfWorkers_10am_to_11am * 5
Capacity_11am_to_12pm = NumOfWorkers_11am_to_12pm * 5
Capacity_12pm_to_1pm = NumOfWorkers_12pm_to_1pm * 5
Capacity_1pm_to_2pm = NumOfWorkers_1pm_to_2pm * 5
Capacity_2pm_to_3pm = NumOfWorkers_2pm_to_3pm * 5
Capacity_3pm_to_4pm = NumOfWorkers_3pm_to_4pm * 5
Capacity_4pm_to_5pm = NumOfWorkers_4pm_to_5pm * 5 

#Cost per group
X1_cost = X1.varValue * 80
X2_cost = X2.varValue * 80
Y1_cost = Y1.varValue * 64
Y2_cost = Y2.varValue * 64
Y3_cost = Y3.varValue * 64
Y4_cost = Y4.varValue * 64
Y5_cost = Y5.varValue * 64
Total_cost = X1_cost + X2_cost + Y1_cost + Y2_cost + Y3_cost + Y4_cost + Y5_cost

#Print results
print("Status:", pulp.LpStatus[problem.status])
print() #blank line

print("Optimal Solution:")
print() #blank line

#Optimal decision variable values
print("Number of workers in group X1:", int(X1.varValue))
print("Number of workers in group X2:", int(X2.varValue))
print("Number of workers in group Y1:", int(Y1.varValue))
print("Number of workers in group Y2:", int(Y2.varValue))
print("Number of workers in group Y3:", int(Y3.varValue))
print("Number of workers in group Y4:", int(Y4.varValue))
print("Number of workers in group Y5:", int(Y5.varValue))
print() #blank line

#Workers and capacity per hour
print("Number of workers and capacity of patients for each hour:")
print() #blank line

print("9am-10am:")
print(f"Number of Workers: {NumOfWorkers_9am_to_10am}")
print(f"Capacity of patients: {Capacity_9am_to_10am}")
print() #blank line

print("10am-11am:")
print(f"Number of Workers: {NumOfWorkers_10am_to_11am}")
print(f"Capacity of patients: {Capacity_10am_to_11am}")
print() #blank line

print("11am-12pm:")
print(f"Number of Workers: {NumOfWorkers_11am_to_12pm}")
print(f"Capacity of patients: {Capacity_11am_to_12pm}")
print() #blank line

print("12pm-1pm:")
print(f"Number of Workers: {NumOfWorkers_12pm_to_1pm}")
print(f"Capacity of patients: {Capacity_12pm_to_1pm}")
print() #blank line

print("1pm-2pm:")
print(f"Number of Workers: {NumOfWorkers_1pm_to_2pm}")
print(f"Capacity of patients: {Capacity_1pm_to_2pm}")
print() #blank line

print("2pm-3pm:")
print(f"Number of Workers: {NumOfWorkers_2pm_to_3pm}")
print(f"Capacity of patients: {Capacity_2pm_to_3pm}")
print() #blank line

print("3pm-4pm:")
print(f"Number of Workers: {NumOfWorkers_3pm_to_4pm}")
print(f"Capacity of patients: {Capacity_3pm_to_4pm}")
print() #blank line

print("4pm-5pm:")
print(f"Number of Workers: {NumOfWorkers_4pm_to_5pm}")
print(f"Capacity of patients: {Capacity_4pm_to_5pm}")
print() #blank line

#Objective function value
print(f"Minimum workforce cost: £{pulp.value(workforce_cost)}")
print() #blank line

print("Work force cost breakdown:")
print() #blank line

print(f"Cost of group X1: £{X1_cost}")
print(f"Cost of group X2: £{X2_cost}")
print(f"Cost of group Y1: £{Y1_cost}")
print(f"Cost of group Y2: £{Y2_cost}")
print(f"Cost of group Y3: £{Y3_cost}")
print(f"Cost of group Y4: £{Y4_cost}")
print(f"Cost of group Y5: £{Y5_cost}")
print(f"Sum:              £{Total_cost}")