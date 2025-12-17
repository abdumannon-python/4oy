# 1========
# select to_char(order_date,'YYYY-MM'),count(distinct o.order_id) from orders o
# join order_details od on o.order_id=od.order_id
# join products p on p.product_id=od.product_id
# where p.category_id=1 and od.unit_price>10 and to_char(o.order_date,'YYYY')='1996'
# group by to_char(order_date,'YYYY-MM')
# 2 ========
# select p.product_name,e.first_name,o.shipped_date from products p
# join order_details od on p.product_id=od.product_id
# join orders o on od.order_id=o.order_id
# join employees e on o.employee_id=e.employee_id
# where p.category_id=3 and p.unit_price=(select min(unit_price) from products where category_id=3) and to_char(shipped_date,'YYYY-MM')='1997-08';
# 3 ====================
# select e.first_name,count(o.order_id) from orders o
# join employees e on e.employee_id= o.employee_id
# where to_char(shipped_date,'YYYY-MM')='1998-03'
# group by e.first_name
# 4=================
# select product_name,category_id,od.unit_price,count(o.order_id) from products p
# join order_details od on p.product_id=od.product_id
# join orders o on od.order_id=o.order_id
# where p.unit_price=(select max(unit_price) from products) and to_char(order_date,'YYYY')='1996'
# group by p.product_name,p.category_id,od.unit_price;
# 5===============
# select e.first_name,count(o.order_id) from orders o
# join employees e on e.employee_id=o.employee_id
# join customers c on o.customer_id=c.customer_id
# where e.country in('USA') and c.country in('USA')
# group by e.first_name
# 6==================
# select e.first_name,count(o.order_id) from products p
# join order_details od on p.product_id=od.product_id
# join orders o on o.order_id=od.order_id
# join employees e on o.employee_id=e.employee_id
# where to_char(order_date,'YYYY')='1997' and p.category_id=5
# group by e.first_name
# 7 ======================
# select c.contact_name,count(o.order_id) from customers c
# join orders o on c.customer_id=o.customer_id
# where to_char(order_date,'YYYY')='1997'
# group by c.contact_name





