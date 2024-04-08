import mysql.connector as mysql

connect = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = connect.cursor(dictionary=True)
query = 'insert into students (name, second_name) values (%s, %s)'
values = ('Jammie', 'Smith')
cursor.execute(query, values)
student_id = cursor.lastrowid

query1 = 'insert into books (title, taken_by_student_id) values (%s, %s)'
value1 = [
    ('Принц и нищий', student_id),
    ('Приключения Тома Сойера', student_id)
]
cursor.executemany(query1, value1)

query2 = 'insert into `groups` (title, start_date, end_date) values (%s, %s, %s)'
value2 = ('Mark Twen', 'june 2021', 'august 2024')
cursor.execute(query2, value2)
group_id = cursor.lastrowid

cursor.execute(f'update students set group_id = {group_id} where id = {student_id}')

query3 = 'insert into subjets (title) values (%s)'
value3 = ('chemistry',)
cursor.execute(query3, value3)
subject_id_1 = cursor.lastrowid

query4 = 'insert into subjets (title) values (%s)'
value4 = ('biology',)
cursor.execute(query4, value4)
subject_id_2 = cursor.lastrowid

query5 = 'insert into lessons (title, subject_id) values (%s, %s)'
value5 = ('atoms', subject_id_1)
cursor.execute(query5, value5)
atoms_id = cursor.lastrowid

query6 = 'insert into lessons (title, subject_id) values (%s, %s)'
value6 = ('molekuls', subject_id_1)
cursor.execute(query6, value6)
molekuls_id = cursor.lastrowid

query7 = 'insert into lessons (title, subject_id) values (%s, %s)'
value7 = ('anatomy', subject_id_2)
cursor.execute(query7, value7)
anatomy_id = cursor.lastrowid

query7 = 'insert into lessons (title, subject_id) values (%s, %s)'
value7 = ('botanic', subject_id_2)
cursor.execute(query7, value7)
botanic_id = cursor.lastrowid

query8 = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
value8 = [
    ('good', atoms_id, student_id),
    ('Well', molekuls_id, student_id),
    ('poor', anatomy_id, student_id),
    ('perfect', botanic_id, student_id)
]
cursor.executemany(query8, value8)

query9 = f'select value from marks where student_id = {student_id}'
cursor.execute(query9)
data_value = cursor.fetchall()
for result in data_value:
    print(result['value'])

query10 = f'select title from books where taken_by_student_id = {student_id}'
cursor.execute(query10)
data_title = cursor.fetchall()
for books_value in data_title:
    print(books_value['title'])

last_query = f'''
SELECT students.name as StudentName,
`groups`.title as GroupTitle,
books.title as BookTitle,
marks.value as MarkValue,
lessons.title as LessonTitle,
subjets.title as SubjectTitle
from students 
join `groups` 
on students.group_id = `groups`.id 
join books 
on students.id = books.taken_by_student_id 
join marks 
on students.id = marks.student_id 
join lessons 
on marks.lesson_id = lessons.id 
join subjets
where students.id = {student_id}
'''
cursor.execute(last_query)
all_data = cursor.fetchall()
for data in all_data:
    print(data['StudentName'],
          data['GroupTitle'],
          data['BookTitle'],
          data['MarkValue'],
          data['LessonTitle'],
          data['SubjectTitle'])


connect.commit()

connect.close()
