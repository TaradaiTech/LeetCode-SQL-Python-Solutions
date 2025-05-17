select
    e2.employee_id, 
    e2.name, 
    count(e1.reports_to) as reports_count, 
    round(avg(e1.age)) as average_age
from employees e1
join employees e2 on 
    e2.employee_id = e1.reports_to
group by
    e2.employee_id, e2.name
having
    count(e1.reports_to) > 0
order by
    e2.employee_id