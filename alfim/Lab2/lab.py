import colors #подключаем написанную библиотеку

# исходные данные
# eat = [[C, M, Y, K, COUNT, TITLE],[]...]
eat = [
    [0, 55, 90, 19, 0, 'Morkovka'],
    [0, 10, 39, 16, 0, 'Kartoshka'],
    [0, 28, 58, 43, 0, 'Kotleta'],
    [0, 62, 75, 64, 0, 'Borch'],
    [0, 18, 71, 9, 0, 'Sok'],
    [0, 8, 32, 12, 0, 'Ris'],
    [0, 21, 46, 40, 0, 'Hleb'],
    [0, 80, 82, 65, 0, 'Kompot'],
    [0, 53, 71, 58, 0, 'Chay']
]
step = 5
dir = 'lab2/'

# новый экзампляр класса
color = colors.Colors(eat, step, dir, 5000, False)

# функция распознавания
color.justdo()