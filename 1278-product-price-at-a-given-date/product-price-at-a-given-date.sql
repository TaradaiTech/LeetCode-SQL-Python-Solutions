SELECT
    p.product_id,
    -- Use COALESCE to default to 10 if no price change exists before 2019-08-16.
    COALESCE(
        (
            SELECT p2.new_price
            FROM Products p2
            WHERE p2.product_id = p.product_id
              AND p2.change_date <= '2019-08-16'
            ORDER BY p2.change_date DESC  -- Get the most recent change on or before the given date.
            LIMIT 1
        ),
        10  -- Default price if no change has occurred on or before 2019-08-16.
    ) AS price
FROM 
    -- Get a distinct list of product_ids from the Products table.
    (SELECT DISTINCT product_id FROM Products) p;