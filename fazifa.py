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