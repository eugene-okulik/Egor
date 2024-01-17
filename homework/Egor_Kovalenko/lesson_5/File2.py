text = 'результат операции: 42'
text_index = text.index(':')
text_slice = int(text[text_index+2:]) + 10
print(text_slice)

text_2 = 'результат работы программы: 9'
text_index1 = text_2.index(':')
result_2 = int(text_2[text_index1+1:]) + 10
print(result_2)

str_1 = 'результат операции: 514'
my_slice = str_1.index(':')
aa = int(str_1[my_slice+2:]) + 10
print(aa)
