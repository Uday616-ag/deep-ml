-- Employee name + department name
SELECT e.name, d.name AS department
FROM employees e ,departments d where e.department_id=d.id
