# 1-misol
# select p.product_name,od.unit_price,s.company_name from products p
# join suppliers s on p.supplier_id=s.supplier_id
# join order_details od on p.product_id=od.product_id
# join orders o on od.order_id=o.order_id
# where to_char(o.order_date,'YYYY-MM')='1996-07'
# -- 2-misol
# -- select e.city,c.city from employees e
# -- join customers c on c.city=e.city
# -- 3-misol
# -- select extract(year from o.order_date),p.product_name,c.company_name,sum(od.quantity) from orders o
# -- join order_details od on o.order_id=od.order_id
# -- join products p on p.product_id=od.product_id
# -- join customers c on o.customer_id = c.customer_id
# -- group by extract(year from o.order_date),p.product_name,c.company_name
# -- order by sum(od.quantity) desc
# -- limit 1;
# -- 4-misol
# -- select extract(year from o.order_date),p.product_name,c.company_name,od.unit_price,sum(od.quantity) from orders o
# -- join order_details od on o.order_id=od.order_id
# -- join products p on p.product_id=od.product_id
# -- join customers c on o.customer_id = c.customer_id
# -- where od.unit_price=(select min(unit_price) from order_details)
# -- group by extract(year from o.order_date),p.product_name,c.company_name,od.unit_price
# -- order by sum(od.quantity) desc
# -- limit 1;
# 5-misol
# select distinct on (c.category_name) c.category_name,p.product_name,count(od.order_id) from categories c
# join products p on c.category_id=p.category_id
# join order_details od on od.product_id=p.product_id
# group by c.category_name,p.product_name
# order by c.category_name,count(od.order_id) desc
# 6-misol
# select e.first_name,e.country,count(o.order_id) from orders o
# natural join employees e
# where e.country in('USA')
# group by  e.first_name,e.country
# order by count(o.order_id) desc
# limit 1;
# 7-misol
# select e.country,count(o.order_id) as son from orders o
# natural join employees e
# group by e.country
# order by son desc
# limit 1;
# 8-misol
# select c.contact_name,sum(quantity) from orders o
# join order_details od on o.order_id=od.order_id
# join customers c on o.customer_id=c.customer_id
# where to_char(order_date,'YYYY')='1997'
# group by c.contact_name
# order by sum(quantity) desc
# limit 1;
# 9-misol
# select p.product_name ,count(od.order_id) from products p
# natural join order_details od
# group by p.product_name
# order by count(od.order_id) asc
# limit 1;
# 10-misol

