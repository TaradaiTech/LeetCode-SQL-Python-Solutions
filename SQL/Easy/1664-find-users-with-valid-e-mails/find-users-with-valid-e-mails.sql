SELECT 
    user_id, 
    name, 
    mail
FROM 
    users
WHERE 
    mail ~* '^[a-z][a-z0-9_.-]*@leetcode\.com$'