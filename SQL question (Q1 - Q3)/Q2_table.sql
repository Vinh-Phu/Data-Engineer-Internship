use master;
go
if exists(select * from sys.databases where name='Q2')
drop database Q2;
go
create database Q2;
go
use Q2;
go

create table Customers
(
  ID int,
  Name varchar(50),
);

insert into Customers values
(1,'Ngoc'),
(2,'Xuan'),
(3,'Lam'),
(4,'Tung');


create table Orders
(
  Id int,
  customerId int
);

insert into Orders values
(1,3),
(2,1);