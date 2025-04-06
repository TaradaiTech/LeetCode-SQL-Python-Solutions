SELECT 
    U.user_id AS buyer_id,         -- Rename user_id as buyer_id for clarity
    U.join_date,                  -- Select the join date of the user
    COUNT(O.order_id) AS orders_in_2019  -- Count the number of orders made in 2019; returns 0 if none
FROM Users U
-- Use LEFT JOIN so that users with no orders in 2019 still appear in the result
LEFT JOIN Orders O
    ON U.user_id = O.buyer_id    -- Join users with orders based on buyer_id
    AND YEAR(O.order_date) = 2019 -- Filter the joined orders to only include those from 2019
GROUP BY U.user_id, U.join_date; -- Group by user_id and join_date to aggregate orders per user