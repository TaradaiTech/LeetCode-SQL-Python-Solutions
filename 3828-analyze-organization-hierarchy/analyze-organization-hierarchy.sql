WITH RECURSIVE CTE_manager AS (
    -- Step 1: Calculate levels using recursive CTE
    SELECT 
        employee_id,
        employee_name,
        manager_id,
        salary,
        department,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL  -- The CEO has no manager (manager_id is NULL)

    UNION ALL

    SELECT
        E1.employee_id,
        E1.employee_name,
        E1.manager_id,
        E1.salary,
        E1.department,
        E2.level + 1 AS level  -- Increment level for direct reports
    FROM Employees E1
    INNER JOIN CTE_manager E2 ON E1.manager_id = E2.employee_id  -- Join to recursively calculate levels
),

-- Step 2: Create a union of manager and employee relationships
CTE_calcu AS (
    SELECT 
        employee_id AS employee,
        manager_id AS manager,
        employee_name,
        salary,
        department
    FROM CTE_manager
    
    UNION ALL

    SELECT 
        manager_id AS employee,
        employee_id AS manager,
        employee_name,
        salary,
        department
    FROM CTE_manager
),

-- Step 3: Calculate team size and total salary (budget)
CTE_calcu_total AS (
    SELECT 
        E1.manager_id,
        COUNT(C1.employee_name) AS team_size,  -- Count of employees under this manager
        SUM(C1.salary) AS budget  -- Total salary of the manager's team
    FROM Employees E1
    JOIN CTE_calcu C1 ON E1.employee_id = C1.employee
    WHERE E1.manager_id IS NOT NULL  -- Only consider employees with managers
    GROUP BY E1.manager_id
)

-- Step 4: Final result: Get employee details along with team size and budget
SELECT
    E.employee_id,
    E.employee_name,
    C1.level,
    CASE 
        WHEN E.manager_id IS NULL THEN (SELECT COUNT(employee_id) FROM CTE_manager WHERE manager_id IS NOT NULL) 
        ELSE COALESCE(team_size, 0) 
    END AS team_size, 
    CASE 
        WHEN E.manager_id IS NULL THEN (SELECT SUM(salary) FROM CTE_manager) 
        ELSE COALESCE(E.salary, 0) + COALESCE(budget, 0) 
    END AS budget
FROM Employees E
LEFT JOIN CTE_calcu_total C ON E.employee_id = C.manager_id
LEFT JOIN CTE_manager C1 ON E.employee_id = C1.employee_id
ORDER BY C1.level ASC, budget DESC, employee_name ASC;