from datetime import datetime as dt
import csv


with open('scientist.txt', mode='r', encoding='utf-8') as file:
    f = list(csv.reader(file, delimiter='#'))[1:]
    dprep = {}
    prep = list(set([i[1] for i in f]))
    for i in prep:
        dprep[i] = []
        for el in f:
            k = el[2].split('-')
            if el[1] == i:
                dprep[i] += [dt(int(k[0]), int(k[1]), int(k[2]))]

    true_vals = []
    crime=[]
    for key, val in (dprep.items()):
        m = dt.date(min(val))
        for el in f:
            if el[1]==key and el[2]==str(m):
                true_vals.append(el)
            if key=='Аллопуринол' and el[1]==key:
                crime.append([el[0], el[2]])

    crime = sorted(crime, key=lambda x: x[1])
    with open('report.txt', mode='w', encoding='utf-8') as t:
        t.write("Разработчиками Аллопуринола были такие люди:\n")
        for name in sorted(crime, key=lambda x: x[1]):
            t.write(f'{name[0]}-{name[1]}\n')
        t.write(f'Оригинальный рецепт принадлежит: {crime[0][0]}')

    true_vals = sorted(true_vals, key=lambda x: x[2])
    with open('scientist_origin.txt', mode='w', encoding='utf-8') as x:
        x.write('ScientistName preparation date components\n')
        for el in true_vals:
            x.write(f"{' '.join(el)}\n")

    crime = sorted(crime, key=lambda x: x[1])
    print("Разработчиками Аллопуринола были такие люди:")
    for name in sorted(crime, key=lambda x: x[1]):
        print(f'{name[0]}-{name[1]}')
    print(f'Оригинальный рецепт принадлежит: {crime[0][0]}')