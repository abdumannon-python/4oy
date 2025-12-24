# 11-masala
# select od.unit_price , count(o.order_id) from orders o
# natural join order_details od
# where od.unit_price=(select min(unit_price) from order_details)
# group by od.unit_price
# order by count(o.order_id) desc
# 12-masala
# select s.company_name ,count(od.order_id) from suppliers s
# join products p on p.supplier_id=s.supplier_id
# join order_details od on od.product_id=p.product_id
# where s.city='London'
# group by s.company_name
# order by count desc







