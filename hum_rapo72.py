import csv

f = open('res/0404excel.csv', 'r', encoding='utf8') #습도 붙이기 귀찮아서 이미 있는거 활용
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[4] != '':
        date = row[2]
        temp = float(row[4])
        hum = float(row[9])
        result.append([date, temp, hum])

result.sort(key=lambda x: x[1], reverse=True)
