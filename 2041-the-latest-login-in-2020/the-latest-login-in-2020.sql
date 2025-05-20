select
    user_id,
    max(time_stamp) as last_stamp
from
    logins
where
    extract(year from time_stamp) = 2020
group by
    user_id;