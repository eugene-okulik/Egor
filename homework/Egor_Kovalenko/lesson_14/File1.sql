
 -- part 1

1. insert into students (name, second_name) values ('Janie', 'Smith')
2. insert into books (title, taken_by_student_id) values ('The Prince and the Pauper', 858), ('tom sawyer', 858)
3. insert into `groups` (title, start_date, end_date) values ('Mark Twen', 'june 2021', 'august 2024')
4. update students set group_id = 808 where id = 858
5. insert into subjets (title) values ('chemistry'), ('biology')
6. insert into lessons (title, subject_id)
values ('atoms', 1087), ('molekuls', 1087), ('anatomty', 1088), ('botanic', 1088)
7. insert into marks (value, lesson_id, student_id)
values ('good', 2930, 858), ('Well', 2931, 858), ('poor', 2928, 858), ('perfect', 2929, 858)


 -- part 2

1. select value from marks where student_id = 858
2. select title from books where taken_by_student_id = 858
3. select s.name, g.title, b.title, m.value, l.title, s2.title
from students s
join `groups` g
on s.group_id = g.id
join books b
on s.id = b.taken_by_student_id
join marks m
on s.id = m.student_id
join lessons l
on m.lesson_id = l.id
join subjets s2
on s2.id  = l.subject_id
where s.id = 858