import mysql.connector as mysql
import os
from dotenv import load_dotenv
import csv

load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(base_path)
homework_path_1 = os.path.dirname(os.path.dirname(base_path))
hm_file_path = os.path.join(homework_path_1, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')

lost_data = []

try:
    with open(hm_file_path, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        for row in file_data:
            name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    query = '''
    SELECT students.name as StudentName,
    students.second_name as StudentSecondName,
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
    on lessons.subject_id = subjets.id
    WHERE StudentName = %s
    AND StudentSecondName = %s
    AND GroupTitle = %s
    AND BookTitle = %s
    AND SubjectTitle = %s
    AND LessonTitle = %s
    AND MarkValue = %s;
    '''

    cursor.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    result = cursor.fetchall()
    if not result:
        lost_data.append(row)

except mysql.Error as Error:
    print(f"Ошибка при отправке запроса: {Error}")
    db.rollback()

if lost_data:
    for data in lost_data:
        print("Данные не найдены в базе данных:", data)
else:
    print('Все данные из файла найдены в базе данных')


db.commit()

db.close()
