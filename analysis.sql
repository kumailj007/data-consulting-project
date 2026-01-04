SELECT 
    product,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

SELECT 
    region,
    SUM(price * quantity) AS regional_revenue
FROM sales
GROUP BY region;
