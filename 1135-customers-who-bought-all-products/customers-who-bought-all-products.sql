SELECT customer_id
FROM Customer
GROUP BY customer_id  -- Group by customer so we can evaluate their purchases
HAVING COUNT(DISTINCT product_key) = (  -- Check if the number of distinct products they bought matches the total count of products
    SELECT COUNT(product_key)  -- Get the total number of distinct products from the Product table
    FROM Product
)