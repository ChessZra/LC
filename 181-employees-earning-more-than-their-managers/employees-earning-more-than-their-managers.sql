select Employee.name as Employee from Employee
join Employee as e 
on Employee.managerId = e.id
where Employee.salary > e.salary