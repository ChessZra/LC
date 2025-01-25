select d.contest_id, round(count(*) / j.total_users * 100, 2) as percentage
from (select distinct * from Register) d
cross join (
    select COUNT(*) as total_users
    from Users
) j 
group by d.contest_id
order by percentage desc, contest_id