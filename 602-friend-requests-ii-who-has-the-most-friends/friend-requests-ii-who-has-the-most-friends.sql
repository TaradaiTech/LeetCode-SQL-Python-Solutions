WITH friends_count AS (
    -- Count the number of times each user appears as a requester (sent friend requests)
    SELECT requester_id AS id, COUNT(*) AS num 
    FROM RequestAccepted 
    GROUP BY requester_id

    UNION ALL

    -- Count the number of times each user appears as an accepter (received and accepted friend requests)
    SELECT accepter_id AS id, COUNT(*) AS num 
    FROM RequestAccepted 
    GROUP BY accepter_id
)

-- Sum up the total number of friendships for each user
SELECT id, SUM(num) AS num 
FROM friends_count
GROUP BY id

-- Order by the highest number of friends and select only the top user
ORDER BY num DESC
LIMIT 1;
