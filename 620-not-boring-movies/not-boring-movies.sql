select *
from Cinema
where id mod 2 = 1 and description != 'boring'
order by rating desc