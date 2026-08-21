# Write your MySQL query statement below
select c.name as Customers from Customers as c
where not exists(select customerId from Orders as o where o.customerId = c.id);