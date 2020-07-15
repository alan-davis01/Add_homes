d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
d2 = {}
for key in d.keys():
    d2[f'{key}{len(key)}'] = d[key]
print(d2)