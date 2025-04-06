WITH FirstLogins AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
ConsecutiveLogins AS (
    SELECT 
        COUNT(DISTINCT a.player_id) AS consecutive_count
    FROM Activity a
    JOIN FirstLogins fl 
        ON a.player_id = fl.player_id
        AND a.event_date = DATE_ADD(fl.first_login, INTERVAL 1 DAY)
)
SELECT 
    ROUND(
        (SELECT consecutive_count FROM ConsecutiveLogins) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction;
