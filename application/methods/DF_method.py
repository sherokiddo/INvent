import pandas as pd
import os, glob

# Удаление (инвенттарник и кабинет) -  сделано
# Кнопка не активны пока не будет сделана инвентаризация
# создание наклейки (инвентарник и кабинет)
# Алерты
# проходимся циклом по всем файлам  -  сделано
# связать функции с кнопкой и алертами

try:
    data = pd.read_csv('comp.csv')

except Exception as ex:
    print('Ошибка в подключении:  ',ex)
    print('Создааём новую базу данных csv')
    data = pd.DataFrame(columns=['invent', 'name', 'num_cab', 'count'])
    data.to_csv('comp.csv', index=False)


def append(invent, name, num_cab, count):
    global data
    try:
        new_row = {'invent': invent, 'name': name, 'num_cab': num_cab, 'count': count}  # append row to the dataframe
        new_row = pd.DataFrame(data=new_row, index=[0])
        data = pd.concat([data, new_row], ignore_index=True)
        print('Данные добавлены .|.')
        data.to_csv('comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в добавлнии', ex)

def show_item(num_cab):
    global data
    try:
        item = data[data['num_cab'] == num_cab]
        return item
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)


def find_invent(inv):
    global data
    try:
        print(data[data['invent'] == inv])
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def update_count(count,inv, num_cab):
    global data
    try:
        data.loc[((data['invent'] == inv) & (data['num_cab'] == num_cab)), ['count']] = count
        data.to_csv('comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в обновлении: ', ex)

def update_cab(new_cab, inv, old_cab):
    global data
    try:
        data.loc[((data['invent'] == inv) & (data['num_cab'] == old_cab)), ['num_cab']] = new_cab
        data.to_csv('comp.csv', index=False)
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
        data.to_csv('comp.csv', index=False)
    except Exception as ex:
        print('Ошибка в удалении: ', ex)


'''
def check_count_cab(phone_line, comp_line):
    global errors
    # проверяем, правильное ли количество
    if phone_line['count'].values[0] != comp_line['count'].values[0]:
        print(f'В кабинете {phone_line["num_cab"].values[0]} неправильное количество предметов.\nДолжно быть:\n'
              f'{comp_line}\nСейчас:\n{phone_line}')
        print('Если вы выберете "исправлю", то нужно будет найти недостающие пердметы или убрать лишние. '
              'Если вы выберете "перезаписать бд", то теперь это число предметов актуально и общая бд перезапишется.')
        answer = input('исправлю/перезаписать бд?') # Allert
        if answer == 'исправлю':
            log_txt.write(
                f'Ошибка № {errors}.\nВ кабинете {phone_line["num_cab"].values[0]} неправильное количество предметов:\nДолжно быть:\n'
                f'{comp_line}\nСейчас:\n{phone_line}\n\n\n')
            errors += 1
        else:
            # вызываем фукцию для замены количества в общей
            update_count(phone_line['count'].values[0], comp_line['invent'].values[0], comp_line['num_cab'].values[0])

    if phone_line['num_cab'].values[0] != comp_line['num_cab'].values[0]:
        print(f'Найден неправильный кабинет.\nДолжно быть:\n{comp_line}\nСейчас:\n{phone_line}')
        print(
            'Если вы выберете "исправлю", перенести предмет/предметы на свое место. Если вы выберете "перезаписать бд", то кабинеты в общей базе данных перезапишутся на текущие.')
        answer = input('исправлю/перезаписать бд?') # Allert
        if answer == 'исправлю':
            log_txt.write(
                f'Ошибка № {errors}.\nНайден неправильный кабинет.\nДолжно быть:\n{comp_line}\nСейчас:\n{phone_line}\n\n\n')
            errors += 1
        else:
            #обновляем кабинет в общей бд
            update_cab(phone_line['num_cab'].values[0], comp_line['invent'].values[0], comp_line['num_cab'].values[0])


def sum_up(comp_data,phone_data):
    global errors
    global last_duplicate
    for invent in comp_data['invent']:
        if invent != last_duplicate:
            # найден ли элемент в локальной бд
            if phone_data.loc[phone_data['invent'] == invent].empty:
                print(f'На кафедре не обнаружен предмет:\n{comp_data.loc[comp_data["invent"] == invent]}') # Allert
                print('Если вы выберете "исправлю", то нужно будет найти и принести предмет на кафедру.'
                      ' Если вы выберете "перезаписать бд", то предмет списан или утерян и теперь не числится на кафедре.')
                answer = input('исправлю/перезаписать бд?')
                if answer == 'исправлю':
                    log_txt.write(f'Ошибка № {errors}.\nНа кафедре не обнаружен предмет:\n{data.loc[data["invent"] == invent]}\n\n\n')
                    errors += 1
                else:
                    # вызываем ф-ию для удаления из общей бд
                    del_values(invent, comp_data.loc[comp_data['invent'] == invent]['num_cab'].values[0])
            else:
                phone_slice = phone_data.loc[phone_data['invent'] == invent].sort_values(by='num_cab').reset_index(drop=True)
                comp_slice = comp_data.loc[comp_data['invent'] == invent].sort_values(by='num_cab').reset_index(drop=True)
                # одна ли строка с этим инвентарником
                if len(phone_slice) == 1:
                    check_count_cab(phone_slice, comp_slice)
                else:
                    for i, j in zip(phone_slice.index, comp_slice.index):
                        check_count_cab(phone_slice.iloc[[i]], comp_slice.iloc[[j]])
                    last_duplicate = invent


comp_data = data.sort_values(by='invent').reset_index(drop=True)
phone_data = join_table('csv_base')

errors = 1
last_duplicate = ''
log_txt = open('log.txt', 'w')

sum_up(comp_data, phone_data)

print('Итоги подведены. Если ошибок не было, то вы можете напечатать ведомость. Если были ошибки, и вы решили их исправить, то они сохранены в log.txt')

log_txt.close()
'''
