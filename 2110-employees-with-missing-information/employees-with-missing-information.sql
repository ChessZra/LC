select employee_id from (
    select e.employee_id, salary as data from Employees e
    left join Salaries s 
    on e.employee_id = s.employee_id
    union
    select s.employee_id, name as data from Employees e
    right join Salaries s
    on e.employee_id = s.employee_id
) tab
where isnull(data)
order by employee_id
