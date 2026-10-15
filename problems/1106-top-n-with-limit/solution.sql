-- Top 3 earners
SELECT name, salary
FROM employees
order by salary DESC 
limit 3