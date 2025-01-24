select product_id, round(sum(summation / total_units), 2) as average_price
from (
    select p.product_id, ifnull(sum(u.units * p.price), 0) as summation, ifnull(t2.total_units, 1) as total_units
    from UnitsSold u
    right join Prices p on u.purchase_date between p.start_date and p.end_date and u.product_id = p.product_id
    left join (
        select product_id, sum(units) as total_units
        from UnitsSold 
        group by product_id
    ) t2 on t2.product_id = u.product_id
    group by p.start_date, p.product_id
) o
group by product_id