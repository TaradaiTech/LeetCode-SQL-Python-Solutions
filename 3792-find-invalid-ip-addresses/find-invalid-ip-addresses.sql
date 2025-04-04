SELECT 
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    -- Check that there are exactly 4 parts
    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3
    OR EXISTS (
        SELECT 1
        FROM regexp_split_to_table(ip, E'\\.') AS part
        WHERE 
            part !~ '^\d+$'  -- Non-numeric
            OR LENGTH(part) > 1 AND LEFT(part, 1) = '0'  -- Leading zero
            OR CAST(part AS INTEGER) > 255  -- Greater than 255
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
