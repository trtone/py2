# Открытие файла
temperature = []


# r помогло задать путь, без него выдвало ошибку 
with open(r'C:\temperture.txt') as t:
    for line in t:
        temperature.append(int(line))
print(temperature)

avg = sum(temperature)/len(temperature)

print('Средняя температура-', avg)