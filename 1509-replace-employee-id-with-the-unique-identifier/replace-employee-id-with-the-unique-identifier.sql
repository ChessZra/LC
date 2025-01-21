select emp.name, uni.unique_id 
from Employees emp
left join EmployeeUNI uni 
on emp.id = uni.id