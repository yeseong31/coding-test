select year(sales_date) as year, month(sales_date) as month, gender, count(distinct a.user_id) as users
from online_sale a join user_info b on a.user_id = b.user_id
where gender is not null
group by year(sales_date), month(sales_date), gender
order by year(sales_date), month(sales_date), gender