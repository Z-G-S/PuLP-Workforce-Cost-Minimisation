# PuLP-Workforce-Cost-Minimisation
Integer linear programming to minimise workforce cost for a healthcare call centre.

# The case study:
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

The call centre can employ up to 20 full-time nurses and up to 20 part-time nurses at most. Part-time nurses work 4 consecutive hours a day if they are requested to work at all, and can start anytime from 9am to 1pm. They earn £16 per hour. Full-time nurses work 8 hours from 9 am to 5 pm and are entitled to one hour break where
half the full-time nurses start their break at noon and the other half at 1pm (if there are an odd number of fulltime nurses then the higher number of nurses have an earlier break), they earn £80 per day. For consistency there must be at least 4 full time nurses working each day.

