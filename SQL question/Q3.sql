select Dep.name, Emp.name, Emp.salary
from Employee as Emp INNER JOIN Department as Dep ON Emp.DepartmentId = Dep.Id
where 3 > ( select count(distinct Emp1.salary) 
	   from Employee as Emp1
	   where Emp1.salary > Emp.salary and Emp.DepartmentId = Emp1.DepartmentId )
group by Dep.name, Emp.name, Emp. salary  