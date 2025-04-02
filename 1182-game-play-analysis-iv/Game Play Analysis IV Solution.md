## Problem Statement
This problem involves analyzing player activity in a game to determine the fraction of players who logged in on the day immediately following their first login.

### Problem Details
- **Table:** `Activity`
  - Columns:
    - `player_id` (int)
    - `device_id` (int)
    - `event_date` (date)
    - `games_played` (int)
- **Primary Key:** (`player_id`, `event_date`)
- **Task:** Calculate the fraction of players who logged in on the day after their first login, rounded to two decimal places.

## Solution Overview
To solve this problem, we use SQL to efficiently compute the required fraction. The approach involves identifying the first login date for each player, checking for consecutive logins, and calculating the fraction of players with such behavior.

### Step-by-Step Explanation

#### 1. Identify First Login Dates
We start by finding the first login date for each player using a Common Table Expression (CTE) named `FirstLogins`.

```sql
WITH FirstLogins AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
```

#### 2. Check Consecutive Logins
Next, we join the `Activity` table with `FirstLogins` to count players who logged in on the day after their first login. This is achieved through another CTE named `ConsecutiveLogins`.

```sql
ConsecutiveLogins AS (
    SELECT 
        COUNT(DISTINCT a.player_id) AS consecutive_count
    FROM Activity a
    JOIN FirstLogins fl 
        ON a.player_id = fl.player_id
        AND a.event_date = DATE_ADD(fl.first_login, INTERVAL 1 DAY)
)
```

#### 3. Calculate Fraction
Finally, we calculate the fraction by dividing the count of players with consecutive logins by the total number of distinct players and round the result to two decimal places.

```sql
SELECT 
    ROUND(
        (SELECT consecutive_count FROM ConsecutiveLogins) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction;
```

### Complete Solution Code
```sql
WITH FirstLogins AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
ConsecutiveLogins AS (
    SELECT 
        COUNT(DISTINCT a.player_id) AS consecutive_count
    FROM Activity a
    JOIN FirstLogins fl 
        ON a.player_id = fl.player_id
        AND a.event_date = DATE_ADD(fl.first_login, INTERVAL 1 DAY)
)
SELECT 
    ROUND(
        (SELECT consecutive_count FROM ConsecutiveLogins) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction;
```

## Complexity Analysis
- **Time Complexity:** O(n), where n is the number of rows in the `Activity` table, due to the grouping and joining operations.
- **Space Complexity:** O(n), for storing intermediate results in CTEs.
