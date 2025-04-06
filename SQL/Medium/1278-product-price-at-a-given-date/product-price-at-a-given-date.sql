-- Step 1: Get the latest change_date for each product on or before '2019-08-16'
WITH LatestChanges AS (
    SELECT 
        product_id,
        MAX(change_date) AS last_change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
),
-- Step 2: Join back to retrieve the corresponding new_price for those changes
ProductPrices AS (
    SELECT 
        p.product_id,
        p.new_price
    FROM Products p
    INNER JOIN LatestChanges lc 
      ON p.product_id = lc.product_id 
     AND p.change_date = lc.last_change_date
)
-- Step 3: Select the final prices for each product, defaulting to 10 if no change exists before 2019-08-16
SELECT 
    d.product_id,
    COALESCE(pp.new_price, 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) d
LEFT JOIN 
    ProductPrices pp
    ON d.product_id = pp.product_id;
