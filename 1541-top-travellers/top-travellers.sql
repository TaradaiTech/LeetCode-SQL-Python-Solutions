SELECT
    u.name,
    SUM(CASE
            WHEN r.distance IS NULL THEN 0
            ELSE r.distance
        END) AS travelled_distance
FROM users u
LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;