# create table student(
# -- id serial primary key,
# -- name varchar(50) not null,
# -- surname varchar(50) not null,
# -- email varchar(50) unique not null,
# -- phone varchar(20) not null,
# -- age integer check (age>0),
# -- tugulgan_kun date,
# -- adres text
# -- );
# create table guruh(
# id serial primary key,
# fan_id int,
# teacher_id int,
# dars_jadval text
# )
# create table fan(
# id serial primary key,
# name varchar(50)
# );
# create table homwork(
# id serial primary key,
# guruh_id int,
# student_id int,
# vasifa text,
# start_date date,
# stop_date date
# );
# =====
# masala 1 pradact jadvalidan categoriy id 3 dan katta bolgan podact name boyicha chiqarish
# 2 castimor jadvalidan countrid=si brazilia bolgan kampaniya nameining 3 harfi kichik n bolgan chiqarilsin
# 3 kastimir jadvalidan regioni biritaniya bolgan va campaniyna name ning oxiridan 3-harji kichik a bolgan capaniya chiqarilsin
# 4 prodact jadvalidagi ortacha narxni chiqaring
# 5 oreders jadvalidan 1997 7 oyidagi kechikkan zakaslar soni
# 6 prodact jadvalidagi 1 kategoriydaga eng qimmat mahsult barcha malumotlari chiqsin
# 7

# select product_name,category_id from products
# where category_id>3

# 1. chi categoriydagi productlar 96 yilning har bir oyida qancadan zakaz tushgan
# 2. 3 chi categoriyadagi eng arzon mahsulaot 97 yildagi yetkazib berilgan sapllayirlar
# 3) 98 yilning 03 oydagi zakzalarga zakazlarni sotib olgan mijozlarni hizmat korsatgan hodimlar
# 4)har bir categoriyadagi eng qimmat mahsulot 96 yilda qanchadan sotilgan
# 5) 97-yilda amerikarlik castimerlarga hizmat korsatgan saplayirlar
# 6) 5 chi categoriyadagi mahsulatlarga 97 yilda hizmat korstaga hodimlar
# 7) amaerikalik har bir shaxri 97 yilning har bir oyida qanchadan zakaz olgan
