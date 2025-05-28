SELECT
    query_name,
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(SUM(rating < 3) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM
    queries
GROUP BY 
    query_name;