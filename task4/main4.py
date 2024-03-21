from datetime import datetime as dt
import csv
import random


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


    names={}
    for k in f:
        nn = k[0].split()
        login = nn[0]+'_'+nn[1][0]+nn[2][0]
        pas = password()
        names[k[0]] = [login, pas]

    for el in names.keys():
        for i in range(len(f)):
            if f[i][0]==el:
                f[i] = f[i]+names[el]
    with open('scientist_password.csv', mode='w', encoding='utf-8') as x:
        crd = csv.writer(x, delimiter=',', lineterminator='\r')
        crd.writerow(['ScientistName', 'preparation','date','components','login','password'])
        for el in f:
            crd.writerow(el)
