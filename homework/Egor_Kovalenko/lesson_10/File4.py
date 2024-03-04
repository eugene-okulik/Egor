PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_dict_values = {int(x[:-1]) for x in PRICE_LIST.split() if x[:-1].isdigit()}
new_dict_keys = {x for x in PRICE_LIST.split() if not x[:-1].isdigit()}
new_result = dict(zip(new_dict_keys, new_dict_values))
print(new_result)
