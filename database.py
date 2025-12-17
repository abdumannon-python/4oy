# 1
# select product_name,category_id from products
# where category_id>3
# 2 select country,company_name from customers
# where country in ('Brazil') and company_name like '__n%'
# 3 select region,company_name from customers
# where region in ('UK') and company_name like '%a__'
# 4 select avg (unit_price) from products
# 5 select * from orders
# where to_char(order_date,'YYYY-MM')='1997-07' and shipped_date>required_date
# 6 select * from products
# where unit_price=(select max(unit_price) from products)


# create table categories (
# category_id integer primary key,
# catergory_name varchar not null,
# description text,
# picture bytea
# # );
# create table suppliers(
# supplier_id integer primary key,
# company_name varchar(50) not null,
# contact_name varchar(50) not null,
# contact_title varchar(50) not null,
# address varchar(50) not null,
# city varchar(50) not null,
# region varchar(50) not null,
# postal_code varchar(50) not null,
# country varchar(50) not null,
# phone varchar(20) not null,
# fax varchar(50) not null,
# homepage text
# );
# create table products (
# product_id integer primary key,
# product_name varchar(50) not null,
# supplier_id integer,
# category_id integer,
# quantity_per_unit varchar(50) not null,
# unit_price numeric(10,4),
# unit_in_stock smallint,
# unit_in_order smallint,
# reorder_level smallint,
# discontinued boolean null default False,
# foreign key(supplier_id) references suppliers(supplier_id),
# foreign key(category_id) references categories(category_id)
# );
# create table orders(
# order_id integer primary key,
# order_date date,
# required_date date,
# shipped_date date,
# ship_name varchar(50) not null,
# ship_adress varchar(50) not null,
# ship_city varchar(50) not null,
# ship_region varchar(50) not null,
# ship_country varchar(50) not null
# );
# create table order_date(
# order_id integer primary key,
# product_id integer,
# unit_price numeric(10,4),
# quantity varchar(50),
# discount varchar(50),
# foreign key(order_id) references orders(order_id),
# foreign key(product_id) references products(product_id)
# );
