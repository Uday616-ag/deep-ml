-- Employees per department
SELECT department_id, COUNT(*) AS headcount
FROM employees group by department_id
