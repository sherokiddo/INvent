import pandas as pd
import os, glob

# Удаление (инвенттарник и кабинет) -  сделано
# Кнопка не активны пока не будет сделана инвентаризация
# создание наклейки (инвентарник и кабинет)
# Алерты
# проходимся циклом по всем файлам  -  сделано
# связать функции с кнопкой и алертами

try:
    data = pd.read_csv('БД компьютера в csv\\comp.csv')

except Exception as ex:
    print('Ошибка в подключении:  ',ex)
    print('Создааём новую базу данных csv')
    data = pd.DataFrame(columns=['invent', 'name', 'num_cab', 'count'])
    data.to_csv('БД компьютера в csv\\comp.csv', index=False)


def append(invent, name, num_cab, count):
    global data
    try:
        new_row = {'invent': invent, 'name': name, 'num_cab': num_cab, 'count': count}  # append row to the dataframe
        new_row = pd.DataFrame(data=new_row, index=[0])
        data = pd.concat([data, new_row], ignore_index=True)
        print('Данные добавлены .|.')
        data.to_csv('БД компьютера в csv\\comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в добавлнии', ex)

def show_item(num_cab):
    global data
    try:
        item = data[data['num_cab'] == num_cab]
        return item
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)


def find_invent(inv, cab):
    global data
    try:
        return data[(data['invent'] == inv) & (data['num_cab'] == cab)].values
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def update_count(count,inv, num_cab):
    global data
    try:
        data.loc[((data['invent'] == inv) & (data['num_cab'] == num_cab)), ['count']] = count
        data.to_csv('БД компьютера в csv\\comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в обновлении: ', ex)

def update_cab(new_cab, inv, old_cab):
    global data
    try:
        data.loc[((data['invent'] == inv) & (data['num_cab'] == old_cab)), ['num_cab']] = new_cab
        data.to_csv('БД компьютера в csv\\comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в обновлении: ', ex)


def join_table(path):
    try:
        full_data = pd.DataFrame(columns=['invent', 'num_cab', 'count'])
        for filename in glob.glob(os.path.join(path, '*.csv')):
            tel_data = pd.read_csv(filename)
            full_data = pd.concat([full_data, tel_data], ignore_index=True)
        return full_data
    except Exception as ex:
        print('Ошибка в объединении: ', ex)


def del_values(inv, num_cab):
    global data
    try:
        data = data[(data['invent'] != inv) | (data['num_cab'] != num_cab)]
        data.to_csv('БД компьютера в csv\\comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в удалении: ', ex)


