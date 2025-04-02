-- First, we define a CTE (Common Table Expression) to calculate averages and other necessary data for analysis.
WITH analyze_sub AS (
    SELECT * 
    FROM (
        SELECT 
            user_id,
            activity_type,              -- The type of activity ('free_trial', 'paid', or 'cancelled')
            activity_duration,
            ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration ELSE 0 END) 
                OVER (PARTITION BY user_id, activity_type), 2) AS trial_avg_duration, -- Avg duration for free_trial, rounded to 2 decimals
            ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration ELSE 0 END) 
                OVER (PARTITION BY user_id, activity_type), 2) AS paid_avg_duration, -- Avg duration for paid, rounded to 2 decimals
            MIN(CASE WHEN activity_type = 'free_trial' THEN activity_date ELSE NULL END) 
                OVER (PARTITION BY user_id) AS min_trial_actdate, -- First date of the free trial activity
            MIN(CASE WHEN activity_type = 'paid' THEN activity_date ELSE NULL END) 
                OVER (PARTITION BY user_id) AS min_paid_actdate -- First date of the paid activity
        FROM UserActivity
    ) sub
    -- Filter to ensure we only include users who converted from free trial to paid
    WHERE min_trial_actdate <= min_paid_actdate
)
-- Now, we select the user_id and calculate the maximum of the trial and paid averages for each user.
SELECT 
    user_id,                                           -- User ID
    MAX(trial_avg_duration) AS trial_avg_duration,      -- Max of trial avg duration, to ensure we get the correct value
    MAX(paid_avg_duration) AS paid_avg_duration        -- Max of paid avg duration, to ensure we get the correct value
FROM analyze_sub
GROUP BY user_id                                     -- Group by user_id to get results per user
ORDER BY user_id;                                     -- Sort the results by user_id in ascending order