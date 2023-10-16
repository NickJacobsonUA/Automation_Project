data1 = ['Commands','Angular','Veu','Private','Classified','General','Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['commands','angular','veu','private','classified','general','downloads','wordFile','excelFile']

#output данные data1 & data2  при выборе элементов списка чекбоксов должны быть одинаковыми. Нужно привести их к общему виду.
# Для этого используется replace & lower. Так как это массив то нужно обернуть его в строку потому что replace работает только состроками.

print(str(data1).replace(' ','').replace('doc','').replace('.','').lower()) #убераем пробелы, точки, и расширения файла

print(str(data1).replace(' ','').replace('doc','').replace('.','').lower())
print(data2)

data1 = str(data1).replace(' ','').replace('doc','').replace('.','').lower()
data2 = str(data2).replace(' ','').lower()

assert data1 == data2