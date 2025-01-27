select q.query_name, 
    ifnull(round(sum(q.rating / q.position) / count(*), 2), 0) as quality,
    ifnull(round(sum(case when rating < 3 then 1 else 0 end) / count(*) * 100, 2), 0) as poor_query_percentage
from Queries q
group by q.query_name