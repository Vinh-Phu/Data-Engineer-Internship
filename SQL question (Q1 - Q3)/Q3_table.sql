use master;
go
if exists(select * from sys.databases where name='Q3')
drop database Q3;
go
create database Q3;
go
use Q3;
go

create table Employee
(
  ID int,
  Name varchar(50),
  Salary int,
  DepartmentId int
);

insert into Employee values
(1,'Hung',70000,1),
(2,'Xuan',80000,2),
(3,'Lam',60000,2),
(4,'Minh',90000,1),
(5,'Man',10000,1),
(6,'Nhi',85000,1),
(7,'Tung',65000,3);


create table Department
(
  Id int,
  Name varchar(50)
);

insert into Department values
(1,'IT'),
(2,'Desginers'),
(3,'Marketing');