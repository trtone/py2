# Открытие файла
temperature = []

with open('C:/temperature.txt') as t:
    for line in t:
        temperature.append(int(line))
print(temperature)

avg = sum(temperature)/len(temperature)

print('Средняя температура-', avg)