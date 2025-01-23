select st.student_id, st.student_name, su.subject_name, ifnull(t2.attended_exams, 0) as attended_exams
from Students st
cross join Subjects su
left join (
    select ex.student_id, ex.subject_name, count(*) as attended_exams
    from Examinations ex
    join Students st on st.student_id = ex.student_id
    group by ex.student_id, ex.subject_name
) t2 on st.student_id = t2.student_id and su.subject_name = t2.subject_name
order by student_id, su.subject_name