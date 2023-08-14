# PuLP-Workforce-Cost-Minimisation
Integer linear programming to minimise workforce cost for a healthcare call centre while adhereing to all constraints.

# The case study
The nurses answering telephones in a healthcare call centre are expected to speak to 5 patients each per hour. The
service operates between 9am and 5pm. As many patients call in their lunch breaks the service is busiest in the middle
of the day.

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


**Objective function:**

| Objective function   | 
| ------------- | 
Min = 80X1 + 80X2 + 64Y1 + 64Y2 + 64Y3 + 64Y4 + 64Y5


**Constraints and Non-negativity:**

| Demand constraint   | 
| ------------- | 
9am-10am: 5x1 + 5x2 + 5y1  ≥ 45 					
10am-11am: 5x1 + 5x2 + 5y1  + 5y2  ≥ 55					
11am-12pm: 5x1 + 5x2 + 5y1 + 5y2  + 5y3  ≥ 70					
12pm-1pm: 5x2 + 5y1 + 5y2  + 5y3 + 5y4  ≥ 85					
1pm-2pm: 5x1 + 5y2 + 5y3  + 5y4 + 5y5  ≥ 88					
2pm-3pm: 5x1 + 5x2 + 5y3 + 5y4  + 5y5  ≥ 84					
3pm-4pm: 5x1 + 5x2 + 5y4 + 5y5  ≥ 70					
4pm-5pm: 5x1 + 5x2 + 5y5  ≥ 60								

Demand constraints ensure that the number of patients requiring treatment each hours is satisfied where the total number of patients nurses can attend to must be greater than or equal to the number of patients in that hour.


| Maximum and minimum full time and part time workers constraints   | 
| ------------- | 
Maximum full-time: x1 + x2  ≤ 20					
Minimum full-time: x1 + x2  ≥ 4					
Maximum part-time: y1 + y2 + y3  + y4 + y5  ≤ 20

This constraints specifies the minimum and maximum number of full-time and part-time nurses required during the day. This shows that there needs to be at least 4 full-time nurses but no more than 20 full-time nurses and no more than 20 part-time nurses working. 


| Break constraints   | 
| ------------- | 
Break constraint lower bound: x1 - x2  ≥ 0					
Break constraint upper bound: x1 - x2  ≤ 1		




| Non-negativity   | 
| ------------- | 
Non-negativity: x1 , x2 , y1 , y2 , y3 , y4 , y5  ≥ 0 and integer




# Output
