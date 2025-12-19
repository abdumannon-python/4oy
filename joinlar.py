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