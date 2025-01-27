select q.query_name, 
    ifnull(round(sum(q.rating / q.position) / count(*), 2), 0) as quality,
    ifnull(round(total_less_than_3 / count(*) * 100, 2), 0) as poor_query_percentage
from Queries q
left join (
    select query_name, COUNT(*) as total_less_than_3
    from Queries
    where rating < 3
    group by query_name
) q2 on q.query_name = q2.query_name
group by q.query_name