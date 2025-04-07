WITH FirstOrders AS (
    -- For each customer, assign a row number based on the order_date (earliest first)
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
)
SELECT 
    ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
FROM FirstOrders
WHERE rn = 1;