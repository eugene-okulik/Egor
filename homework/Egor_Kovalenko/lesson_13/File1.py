import os
import datetime

base_path = os.path.dirname(__file__)
# file_path = f'{base_path}/data.txt'
# file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'my_data.txt')
homework_path = os.path.dirname(base_path)
homework_path_1 = os.path.dirname(os.path.dirname(base_path))
hm_file_path = os.path.join(homework_path_1, 'eugene_okulik', 'hw_13', 'data.txt')

with open(hm_file_path, 'r') as new_file:
    lines = new_file.readlines()

new_line_split = lines[0].split()[1:3]
new_line_str = ' '.join(new_line_split)
date_1 = datetime.datetime.strptime(new_line_str, '%Y-%m-%d %H:%M:%S.%f')

print(date_1 + datetime.timedelta(weeks=1))

new_line_split_1 = lines[1].split()[1:3]
new_line_str_1 = ' '.join(new_line_split_1)
date_2 = datetime.datetime.strptime(new_line_str_1, '%Y-%m-%d %H:%M:%S.%f')

print(date_2.day)

new_line_split_2 = lines[2].split()[1:3]
new_line_str_2 = ' '.join(new_line_split_2)
date_3 = datetime.datetime.strptime(new_line_str_2, '%Y-%m-%d %H:%M:%S.%f')

print((datetime.datetime.now() - date_3).days)
