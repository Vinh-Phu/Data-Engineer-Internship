use master;
go
if exists(select * from sys.databases where name='Q1')
drop database Q1;
go
create database Q1;
go
use Q1;
go

create table Performance
(
  Athleteld varchar(50),
  Gender Bit,
  Country varchar(50),
  Score float(50)
);

insert into Performance values
('Tan Tai',0,'Viet Nam',10),
('Huynh Nhu',1,'Viet Nam',8),
('Henry',0,'USA',7),
('Robert',0,'Spain',8.5);