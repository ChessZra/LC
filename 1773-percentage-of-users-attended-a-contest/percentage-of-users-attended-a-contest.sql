select d.contest_id, round(count(*) / (select COUNT(*) from Users) * 100, 2) as percentage
from (select distinct * from Register) d
group by d.contest_id
order by percentage desc, contest_id