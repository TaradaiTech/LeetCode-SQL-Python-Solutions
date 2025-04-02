-- Select the names of managers who have at least 5 direct reports.
SELECT name 
FROM (
    -- Join the Employee table with itself to match managers with their direct reports.
    SELECT 
        a.id,                           -- Manager's id
        a.name AS name,                 -- Manager's name
        COUNT(*) AS report_count        -- Count of direct reports for the manager
    FROM employee a 
    JOIN employee b 
        ON a.id = b.managerId           -- Join condition: b is a direct report of a
    GROUP BY a.id, a.name               -- Group by manager id and name to aggregate direct reports
    HAVING COUNT(*) >= 5                -- Filter to keep only managers with at least 5 direct reports
) AS t;                               -- Use a subquery (aliased as t) to select only the manager names