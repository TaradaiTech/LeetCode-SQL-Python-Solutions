-- Step 1: Compute the first sale year for each product using a window function
WITH SalesWithFirstYear AS (
    SELECT 
        product_id,
        year,
        quantity,
        price,
        first_value(year) OVER (PARTITION BY product_id ORDER BY year) AS first_year
    FROM Sales
)

-- Step 2: Select only the rows where the sale year is the first sale year for that product
SELECT 
    product_id, 
    first_year AS first_year, 
    quantity, 
    price
FROM SalesWithFirstYear
WHERE year = first_year;