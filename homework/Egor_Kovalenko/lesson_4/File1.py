my_dict = {}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [1, 2, 3, 4, 5]
my_dict['dict'] = {'one': 'value1', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5'}
my_dict['set'] = {1, 2, 3, 4, 5}
print(my_dict['tuple'][-1])
my_dict['list'].append(56)
my_dict['list'].pop(1)
my_dict['i am a tuple'] = 'i am not a value'
my_dict['dict'].pop('one')
my_dict['set'].add('test')
my_dict['set'].remove(2)
print(my_dict)
