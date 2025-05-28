SELECT
    user_id,
    UPPER(LEFT(name, 1)) || LOWER(SUBSTRING(name FROM 2)) AS name
FROM
    users
ORDER BY
    user_id;