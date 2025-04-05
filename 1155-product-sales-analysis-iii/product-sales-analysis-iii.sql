SELECT 
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
WHERE (product_id, year) IN (
    -- For each product, select the minimum (first) year of sale.
    SELECT 
        product_id,
        MIN(year)
    FROM Sales
    GROUP BY product_id
);
