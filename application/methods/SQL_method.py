import sqlite3
import pandas as pd

try:
    con = sqlite3.connect('Invent_3.db')
    cur = con.cursor()
    #print('БД успешно создана')
    try:
        Create = f"""CREATE TABLE IF NOT EXISTS full_table(
        Invent TEXT,
        Name TEXT,
        NumKab INTEGER,
        Count INTEGER); """
        cur.execute(Create)
        con.commit()
    except:
        print('Плохо ')
except Exception as ex:
    print('Ошибка в подключении:  ',ex)


def CreateTable(num_kab):
    Create = f"""CREATE TABLE IF NOT EXISTS {'tab'+str(num_kab)} (
    Invent TEXT,
    Name TEXT,
    NumKab INTEGER,
    Count INTEGER); """
    print(Create)
    cur.execute(Create)
    con.commit()

    #cur.execute("""SELECT * FROM sqlite_master where type='table'""")#Инфа о всех таблицах
    #print(cur.fetchall())

    print('Таблица создана  .|.  ')

def Append(Invent, Name, NumKab, Count):
    try:
        rest = (Invent, Name, NumKab,Count)
        cur.execute(f"INSERT INTO full_table VALUES(?,?,?,?);", rest)
        con.commit()
        print('Данные занесены  .|.  ')
    except Exception as ex:
        print('Ошибка в добавлении: ', ex)

def Show(num_kab):
    try:
        cur.execute(f'SELECT * FROM full_table WHERE NumKab = {num_kab}')
        data = cur.fetchall()
        print(data)
        return data
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def FindInvent(Inv):
    try:
        cur.execute("SELECT * FROM tab1 WHERE Invent = '%s' " % Inv)
        data = cur.fetchall() #Все элементы с инвентарником Inv
        for i in data:
            print(i)
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def DelValue(Inv):
    try:
        cur.execute("DELETE FROM tab1 WHERE Invent = '%s' " % Inv)
        con.commit()
        print('Удаление завершено')
    except Exception as ex:
        print('Ошибка в удалении: ', ex)

def ClearDB():
    try:
        cur.execute("""SELECT * FROM sqlite_master where type='table'""")  # Инфа о всех таблицах
        print()
        for table in cur.fetchall():
            cur.execute(f"DELETE FROM {str(table[1])}")
            con.commit()
        print('Очистка завершена')
    except Exception as ex:
        print('Ошибка в очистке: ', ex)

def UpdateCount(Count,Inv):
    try:
        cur.execute("UPDATE tab1 set Count = '%d' WHERE Invent = '%s' " % (Count, Inv))
        con.commit()
        print('Обновление завершено')
    except Exception as ex:
        print('Ошибка в обновлении: ', ex)


def join_table(file_name_1, file_name_2):
    #
    data = []
    con_1 = sqlite3.connect(file_name_1)
    cur_1 = con_1.cursor()
    cur_1.execute('SELECT * FROM full_table')
    data+=cur_1.fetchall()

    con_2 = sqlite3.connect(file_name_2)
    cur_2 = con_2.cursor()
    cur_2.execute('SELECT * FROM full_table')
    data += cur_2.fetchall() #[(....), (....)]
    df = pd.DataFrame(data=data, columns=['invent', 'name', 'numkab', 'count'])
    print(df)

#join_table('..//Invent.db','..//Invent_2.db')
#ClearDB()



#num_kab_curent =317
#CreateTable(num_kab_curent)
#Append(num_kab_curent, str(269),'Тактический стул',num_kab_curent, 1)
#Append(num_kab_curent, str(290),'Тактический веник',num_kab_curent, 1)
#FindInvent('П0002')
#DelValue('П0003'
#data = Show()
#for i in data:
#    print(i)
#UpdateCount(100,'П0005')
#print()

#ClearDB()
#print(Show())

#Append('666666','Киллер фича',302, 1)

'''
for i in range(22):
    Append(num_kab_curent, str(200+i),'Этот хакатон  мл-инженеров из ВТБ и Дениса Сыропятова, ясно понятно',num_kab_curent, 1)

'''

#con.close()
#Вывод по инвентарнику, удаление, вывод по кабинету, обновление кол-ва предметов
