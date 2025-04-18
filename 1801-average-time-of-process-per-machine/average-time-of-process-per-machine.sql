WITH process_times AS (
  SELECT
    s.machine_id,
    e.timestamp - s.timestamp AS duration
  FROM activity AS s
  JOIN activity AS e
    ON  s.machine_id = e.machine_id
    AND s.process_id = e.process_id
WHERE
    s.activity_type = 'start'
    AND e.activity_type = 'end'
)
SELECT
    machine_id, ROUND(AVG(duration) , 3 ) AS processing_time
FROM
    process_times
GROUP BY
    machine_id;