SELECT 
    id,  -- The ID remains the same, no need to change that
    CASE
        -- For even-numbered IDs, get the student in the previous row (LAG function)
        WHEN id % 2 = 0 THEN LAG(student) OVER(ORDER BY id)
        
        -- For odd-numbered IDs, get the student in the next row (LEAD function), but ensure the last student stays in place if there's no pair
        ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
    END AS student
FROM Seat