select *
from Customers
where id not in (select customerld
                   from Orders);