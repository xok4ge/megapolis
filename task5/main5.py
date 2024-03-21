from datetime import datetime as dt
import csv
import random

def hash_table():
    """
    :input: None
    Генерирует таблицу перестановок
    использует random для случайного перемешивания чисел
    :return: hash-таблица
    """
    tb = []
    nums = [i for i in range(0, 1023+1)]
    while len(tb)!=1024:
        flg=False
        while True:
            q = random.choice(nums)
            if q not in tb:
                tb.append(q)
                flg=True
            if flg:
                break
    return tb


with open('scientist.txt', mode='r', encoding='utf-8') as file:
    table = hash_table()
    f = list(csv.reader(file, delimiter='#'))[1:]
    dprep = []
    prep = list(set([i[1] for i in f]))

    for i in range(len(f)):  # алгоритм хеширования
        k = ''.join(f[i][0].split())
        qwe = []
        for x in k:
            asci = ord(x)%1024
            qwe.append(table[asci])
        hash = sum(qwe)%2048
        f[i] = [hash] + f[i]

    with open('scientist_with_hash.csv', mode='w', encoding='utf-8') as x:  # загрузка в .csv
        crd = csv.writer(x, delimiter=',', lineterminator='\r')
        crd.writerow(['hash', 'ScientistName', 'preparation','date','components'])
        for el in f:
            crd.writerow(el)