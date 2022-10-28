import sqlite3
#from openpyxl import load_workbook

import SQL_method as sql
import WorkShit as exel
from math import ceil
#sql.Append('ПОООООООХУЙ','Суп из 7 залуп', 202, 7)
#con = sql.ConnectDB('Invent.db')
#cur = con.cursor()

# U19   V19    W19

def InputData():

    dataAll = sql.Show()
    Inv = 'U'
    Name = 'V'
    Count = 'W'

    BufCount = 0
    for i in dataAll:
        BufCount+=1
    print(BufCount)
    if BufCount<=40:
        exel.CreateSheet(file, kab, 'Sample')
        sheet = exel.ConnectSheet(file, kab)
        exel.AppendValue(sheet, 'U11', kab)
        count = 19
        for data in dataAll:
            exel.AppendValue(sheet,Inv+str(int(count)),data[0])
            exel.AppendValue(sheet, Name+str(int(count)), data[1])
            exel.AppendValue(sheet, Count+str(int(count)), data[3])
            count+=1

    elif BufCount>40:
        CountList = ceil(BufCount/40)
        print(CountList)
        number = 1
        first = True
        exel.CreateSheet(file, kab+'-'+str(number), 'Sample-1')
        sheet = exel.ConnectSheet(file, kab+'-'+str(number))
        exel.AppendValue(sheet, 'U11', kab)
        CountList-=1
        count=19
        for data in dataAll:
            if count<=58 and first==True:
                exel.AppendValue(sheet, Inv + str(int(count)), data[0])
                exel.AppendValue(sheet, Name + str(int(count)), data[1])
                exel.AppendValue(sheet, Count + str(int(count)), data[3])

            elif count<=40 and first==False:
                exel.AppendValue(sheet,Inv+str(int(count)),data[0])
                exel.AppendValue(sheet, Name+str(int(count)), data[1])
                exel.AppendValue(sheet, Count+str(int(count)), data[3])

            elif count==41 and CountList>1:
                count=1
                CountList-=1
                number+=1

                exel.CreateSheet(file, kab + '-' + str(number), 'Sample-2')
                sheet = exel.ConnectSheet(file, kab + '-' + str(number))
                exel.AppendValue(sheet, Inv + str(int(count)), data[0])
                exel.AppendValue(sheet, Name + str(int(count)), data[1])
                exel.AppendValue(sheet, Count + str(int(count)), data[3])

            elif count==41 and CountList==1:
                count = 1
                CountList -= 1
                number += 1

                exel.CreateSheet(file, kab + '-' + str(number), 'Sample-3')
                sheet = exel.ConnectSheet(file, kab + '-' + str(number))

                exel.AppendValue(sheet, Inv + str(int(count)), data[0])
                exel.AppendValue(sheet, Name + str(int(count)), data[1])
                exel.AppendValue(sheet, Count + str(int(count)), data[3])

            count+=1

            if count==59 and first==True:
                first = False
                count=41

file = exel.Connect()
kab = '269'

InputData()
sql.con.close()
file.save('shit3.xlsx')