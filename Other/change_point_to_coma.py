import pandas as pd

import pandas as pd

# Чтение данных из Excel-файла с явным указанием типа данных для определенных столбцов
dtype_dict = {'ГТД': str}  # Указываем, что столбец 'ГТД' должен интерпретироваться как строковый тип данных

df = pd.read_excel('C:/Users/Мой ПК/Desktop/nds.xlsx', dtype=dtype_dict)

# Замена всех точек на запятые во всех ячейках, кроме столбца 'ГТД'
df.iloc[:, df.columns != 'ГТД'] = df.iloc[:, df.columns != 'ГТД'].applymap(lambda x: str(x).replace('.', ','))

# Сохранение изменений обратно в Excel-файл
df.to_excel('C:/Users/Мой ПК/Desktop/nds.xlsx', index=False, engine='openpyxl')

