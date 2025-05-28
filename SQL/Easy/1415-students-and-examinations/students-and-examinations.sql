SELECT
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(exa.subject_name) AS attended_exams
FROM
    students s
CROSS JOIN 
    subjects sub
LEFT JOIN 
    examinations exa ON s.student_id = exa.student_id 
                      AND sub.subject_name = exa.subject_name
GROUP BY
    s.student_id,
    s.student_name,
    sub.subject_name
ORDER BY
    s.student_id, sub.subject_name;
