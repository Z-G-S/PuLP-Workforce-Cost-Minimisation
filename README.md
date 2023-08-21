# PuLP-Workforce-Cost-Minimisation
Integer linear programming to minimise workforce cost for a healthcare call centre while adhereing to all constraints.

# The case study
The nurses answering telephones in a healthcare call centre are expected to speak to 5 patients each per hour. The
service operates between 9am and 5pm. As many patients call in their lunch breaks the service is busiest in the middle
of the day.
######
**TABLE 1: Average number of customers by time period.**
| Time period   | No. of patients |
| ------------- | ------------- |
| 9am-10am  | 45  |
| 10am-11am  | 55  |
| 11am-12pm  | 70  |
| 12pm-1pm  | 85  |
| 1pm-2pm  | 88  |
| 2pm-3pm  | 84  |
| 3pm-4pm  | 70  |
| 4pm-5pm  | 60  |
######
The call centre can employ up to 20 full-time nurses and up to 20 part-time nurses at most. Part-time nurses work 4 consecutive hours a day if they are requested to work at all, and can start anytime from 9am to 1pm. They earn £16 per hour. Full-time nurses work 8 hours from 9 am to 5 pm and are entitled to one hour break where half the full-time nurses start their break at noon and the other half at 1pm (if there are an odd number of fulltime nurses then the higher number of nurses have an earlier break), they earn £80 per day. For consistency there must be at least 4 full time nurses working each day.

# Formulation
**Decision variables:**
| Decision variables   | 
| ------------- | 
X1 = The number of full-time nurses that work from 9am to 5pm and take a break at 12pm	
X2 = The number of full-time nurses that work from 9am to 5pm and take a break at 1pm						
Y1 = The number of part-time nurses that work from 9am to 1pm						
Y2 = The number of part-time nurses that work from 10am to 2pm						
Y3 = The number of part-time nurses that work from 11am to 3pm						
Y4 = The number of part-time nurses that work from 12pm to 4pm						
Y5 = The number of part-time nurses that work from 1pm to 5pm						
######
Part of the optimal solution will be shown through the value of the decision variables, where the number of full-time and part-time workers are configured to minimise workforce cost whilst also satisfying the constraints. Full-time nurses have been split into two groups (x1 and x2) in order to formulate the break constraints. 
######
**Objective function:**
| Objective function   | 
| ------------- | 
Min = 80X1 + 80X2 + 64Y1 + 64Y2 + 64Y3 + 64Y4 + 64Y5
######
The coefficients of the decision variables represents the cost of each worker in each group. full-time workers (X1, X2) cost £80 per day and part-time workers (Y1, Y2, Y3, Y4, Y5) cost £16 per hour with a 4 hour shift and so, cost £64 each time they work (£16 * 4).
######
**Constraints and Non-negativity:**
| Demand constraint   | 
| ------------- | 
9am-10am: 5X1 + 5X2 + 5Y1  ≥ 45 					
10am-11am: 5X1 + 5X2 + 5Y1  + 5Y2  ≥ 55					
11am-12pm: 5X1 + 5X2 + 5Y1 + 5Y2  + 5Y3  ≥ 70					
12pm-1pm: 5X2 + 5Y1 + 5Y2  + 5Y3 + 5Y4  ≥ 85					
1pm-2pm: 5X1 + 5Y2 + 5Y3  + 5Y4 + 5Y5  ≥ 88					
2pm-3pm: 5X1 + 5X2 + 5Y3 + 5Y4  + 5Y5  ≥ 84					
3pm-4pm: 5X1 + 5X2 + 5Y4 + 5Y5  ≥ 70					
4pm-5pm: 5X1 + 5X2 + 5Y5  ≥ 60								
######
Demand constraints ensure that the number of patients requiring treatment each hours is satisfied where the total number of patients nurses can attend to must be greater than or equal to the number of patients in that hour.
######
| Maximum and minimum full time and part time workers constraints   | 
| ------------- | 
Maximum full-time: x1 + x2  ≤ 20					
Minimum full-time: x1 + x2  ≥ 4					
Maximum part-time: y1 + y2 + y3  + y4 + y5  ≤ 20
######
This constraints specifies the minimum and maximum number of full-time and part-time nurses required during the day. This shows that there needs to be at least 4 full-time nurses but no more than 20 full-time nurses and no more than 20 part-time nurses working. 
######
| Break constraints   | 
| ------------- | 
Break constraint lower bound: X1 - X2  ≥ 0					
Break constraint upper bound: X1 - X2  ≤ 1
Break constraint 3: X1 >= X2
######
The break constraints represent the lower and upper bound of X1 - X2. With both variables being integer due to the non-negativity/integer constraint (below) this limits the value of X1 - X2 to 1 or 0, which ensures that when there is an odd number of full-time nurses working, the larger group (X1) will take their break at 12pm and the smaller group (X2) will take their break at 1pm due to the X1 >= X2 constraint. For example, if there are 11 full-time workers across groups X1 and X2 then X1 must be 6 and X2 must be 5 because X1 must be greater than (or equal to) X2 and integer, but can only be 1 greater than X2. 
######
| Non-negativity   | 
| ------------- | 
Non-negativity: X1 , X2 , Y1 , Y2 , Y3 , Y4 , Y5  ≥ 0 and integer
######
The non-negativity constraint ensures that the decision variables are greater than or equal to zero (cannot have a negative number of workers) and are integer (cannot have a fraction of a worker).
######

# Optimal solution

**Decison variable optimal values**
| Group   | No. of workers |
| ------------- | ------------- |
| X1  | 5  |
| X2  | 5  |
| Y1  | 1  |
| Y2  | 6  |
| Y3  | 3  |
| Y4  | 2  |
| Y5  | 2  |
######
The decision variable values show the optimum number of workers allocated to each group (shift) to minimise cost while satisfying all constraints.

**Objective function optimal value**

| Minimum workforce cost   |
| ------------- |
£1696.0
######
This value is the minimum workforce cost achieved when satisfying all constraints and is calculated by multiplying the cost coefficients in the objective function with the decision variable values.
######
**Workforce cost breakdown**
| Group   | Cost |
| ------------- | ------------- |
| X1  | £400.0 |
| X2  | £400.0  |
| Y1  | £64.0  |
| Y2  | £384.0  |
| Y3  | £192.0 |
| Y4  | £128.0  |
| Y5  | £128.0  |
######
The table above breaksdown the workforce cost for each group. For example, X1's cost of £400.0 has been calculated by taking the cost coefficient in the objective function (£80) and multiplying it with the optimal value of X1 (5).
######
# Extended model
**Workers and capacity per hour**
######
The model is extended to create a timetable, showing the number of workers per hour and capacity per hour. This is useful for the healthcare call centre as the model alone does not include this and the centre would need to know how many nurses are working at a point in time.
######
| Hour   | No. of workers | Capacity of patients |
| ------------- | ------------- |------------- |
| 9am-10am  | 11 | 55 |
| 10am-11am  | 17  | 85  |
| 11am-12pm  | 20  | 100  |
| 12pm-1pm  | 17  | 85  |
| 1pm-2pm  | 18 | 90  |
| 2pm-3pm  | 17 | 85  |
| 3pm-4pm  | 14  | 70  |
| 4pm-5pm  | 12  | 60  |
######
**Slack and binding status**
######
The model also incorporates the slack and binding status for each constraint. Slack refers to an additional variable used in the algorithm and inequality equations that represent how much room there is before the constraint becomes "binding". A binding constraint refers to a constraint with a slack value of 0.0 that forms the feasible region. In the healthcare call centre case study, for the demand constraints, slack refers to the additional capacity over the right hand side of the equation. More specifically, in the hour 9am-10am, the demand constraint requires there be a capacity of at least "45" and through the optimal solution we see that the capacity for this hour is 55 patients and thus, the slack variable has a value of "10.0".
######
| Constraint name   | Slack | Status |
| ------------- | ------------- |------------- |
| 9am-10am  | 10.0 | 55 | Not Binding
| 10am-11am  | 30.0  | 85  | Not Binding
| 11am-12pm  | 30.0  | 100  | Not Binding
| 12pm-1pm  | 0.0  | 85  | Binding
| 1pm-2pm  | 2.0 | 90  | Not Binding
| 2pm-3pm  | 1.0 | 85  | Not Binding
| 3pm-4pm  | 0.0  | 70  | Binding
| 4pm-5pm  | 0.0  | 60  | Binding
| Max full-time  | 10.0 | 90  | Not Binding
| Min full-time  | 6.0 | 85  | Not Binding
| Max part-time  | 6.0  | 70  | Not Binding
| BC1  | 12  | 0.0  | Binding
| BC2  | 14  | 1.0  | Not Binding
| BC3  | 12  | 0.0  | Binding
