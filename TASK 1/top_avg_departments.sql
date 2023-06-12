-- picking up database 
USE onlinesales_ai; 


-- creating table with top 3 avg salary departments
SELECT d.NAME AS DEPT_NAME, ROUND(AVG(emp_avg_salary), 2) AS AVG_MONTHLY_SALARY
FROM departments d
JOIN employees e ON d.ID = e.`DEPT ID`
JOIN (
    -- creating a table with avg salary of employees
    SELECT s.EMP_ID, AVG(s.`AMT (USD)`) AS emp_avg_salary
    FROM salaries s
    GROUP BY s.EMP_ID
    
) AS emp_salaries ON e.ID = emp_salaries.EMP_ID
GROUP BY d.NAME
ORDER BY AVG_MONTHLY_SALARY DESC
LIMIT 3;