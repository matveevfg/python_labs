t1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
tsuf = ['дцать', 'десят', 'надцать', 'ста', 'сот', 'тысяч', 'миллиард', 'миллион']

def number_to_words(number):
    print(number)
    result = ''
    milliards = number // 1000000000
    

    # Миллиарды
    # еденицы
    if milliards != 0:
        if len(str(milliards)) == 1 or milliards == 10:
            if (milliards == 1):
                result += t1[milliards - 1] + ' ' + tsuf[6]
                
            elif (2 <= milliards <= 4):
                result += t1[milliards - 1] + ' ' + tsuf[6] + end_word(milliards)
                
            elif (milliards > 4):
                result += t1[milliards - 1] + ' ' + tsuf[6] + end_word(milliards)
            number = int(str(number)[1:])
        #десятки
        elif len(str(milliards)) == 2 and milliards != 10:
            result += tens(milliards) + ' ' + tsuf[6] + end_word(milliards)
            number = int(str(number)[2:])
        #сотни
        elif len(str(milliards)) == 3:
            result += hundreds(milliards) + ' ' + tsuf[6] + end_word(milliards)
            number = int(str(number)[3:])
    
    print(number)
    
    # Миллионы
    millions = number // 1000000
    if millions != 0:
        if len(str(millions)) == 1 or millions == 10:
            if (millions == 1):
                result += t1[millions - 1] + ' ' + tsuf[7]
                number = int(str(number)[1:])
            elif (2 <= millions <= 4):
                result += t1[millions - 1] + ' ' + tsuf[7] + end_word(millions)
                
            elif (millions > 4):
                result += t1[millions - 1] + ' ' + tsuf[7] + end_word(millions)
            number = int(str(number)[1:])
        #десятки
        elif len(str(millions)) == 2 and millions != 10:
            result += tens(millions) + ' ' + tsuf[7] + end_word(millions)
            number = int(str(number)[2:])
        #сотни
        elif len(str(millions)) == 3:
            result += hundreds(millions) + ' ' + tsuf[7] + end_word(millions)
            number = int(str(number)[3:])

    print(number)

    # Тысячи
    print('AAAAAAAAAAAAAAAAAAAAA')
    thousands = number // 1000
    if thousands != 0:
        if len(str(thousands)) == 1 or thousands == 10:
            if (thousands == 1):
                result += 'одна' + ' ' + tsuf[5] + end_word_for_thousent(thousands)
            elif (2 <= thousands <= 4):
                result += t1[thousands - 1] + ' ' + tsuf[5] + end_word_for_thousent(thousands)
            elif (thousands > 4):
                result += t1[thousands - 1] + ' ' + tsuf[5] + end_word_for_thousent(thousands)
            number = int(str(number)[1:])
        #десятки
        elif len(str(thousands)) == 2 and thousands != 10:
            result += tens(thousands) + ' ' + tsuf[5] + end_word_for_thousent(thousands)
            number = int(str(number)[2:])
        #сотни
        elif len(str(thousands)) == 3:
            result += hundreds(thousands) + ' ' + tsuf[5] + end_word_for_thousent(thousands)
            number = int(str(number)[3:])
    print(number)

    # сотни
    if len(str(number)) == 3:
        result += hundreds(number)

    # десятки
    if len(str(number)) == 2:
        result += tens(number)

    # еденицы
    if len(str(number)) == 1:
        result += t1[number-1]

    return result

def tens(number):       
    #1 + x
    if int(str(number)[0]) == 1:
        if int(str(number)[1]) == 1:
            result = t1[int(str(number)[1]) - 1] + tsuf[2]
        if int(str(number)[1]) == 2:
            result = t1[int(str(number)[1]) - 1][:-1] + 'е' + tsuf[2]
        if int(str(number)[1]) == 3:
            result = t1[int(str(number)[1]) - 1] + tsuf[2]
        if int(str(number)[1]) > 3:
            result = t1[int(str(number)[1]) - 1][:-1] + tsuf[2]
    #2/3 + x
    elif 2 <= int(str(number)[0]) <= 3:
        if int(str(number)[1]) == 0:
            result = t1[int(str(number)[0]) - 1] + tsuf[0]
        else:
            result = t1[int(str(number)[0]) - 1] + tsuf[0] + ' ' + t1[int(str(number)[1]) - 1]
    #>3 + x
    elif int(str(number)[0]) > 3 and int(str(number)[0]) != 4 and int(str(number)[0]) != 9:
        if int(str(number)[1]) == 0:
            result = t1[int(str(number)[0]) - 1] + tsuf[1]
        else:
            result = t1[int(str(number)[0]) - 1] + tsuf[1] + ' ' + t1[int(str(number)[1]) - 1]
    elif int(str(number)[0]) == 4:
        if int(str(number)[1]) == 0:
            result = 'сорок'
        else:
            result = 'сорок' + ' ' + t1[int(str(number)[1]) - 1]
    elif int(str(number)[0]) == 9:
        if int(str(number)[1]) == 0:
            result = 'девяносто'
        else:
            result = 'девяносто' + ' ' + t1[int(str(number)[1]) - 1]
    return result

def hundreds(number): 
    if int(str(number)[0]) == 1: 
        if int(str(number)[1]) == 0 and int(str(number)[2]) == 0:
            result = tsuf[3][:-1] + 'о' 
        else:
            result = tsuf[3][:-1] + 'о' + tens(int(str(number)[1:]))
    if int(str(number)[0]) == 2: 
        result =t1[int(str(number)[0]) - 1][:-1] + 'е' + tsuf[3][:-1] + 'и' + ' ' + tens(int(str(number)[1:]))
    if 3 <= int(str(number)[0]) <= 4: 
        result = t1[int(str(number)[0]) - 1] + tsuf[3][:-1] + 'а' + ' ' + tens(int(str(number)[1:])) 
    if int(str(number)[0]) > 4: 
        result = t1[int(str(number)[0]) - 1] + tsuf[4] + ' ' + tens(int(str(number)[1:]))
    return result

def end_word(number):
    if int(str(number)[len(str(number)) - 1]) == 1:
        end_word = ' '
    elif 2 <= int(str(number)[len(str(number)) - 1]) <= 4:
        end_word = 'а '
    elif int(str(number)[len(str(number)) - 1]) > 4:
        end_word = 'ов '
    return end_word

def end_word_for_thousent(number):
    if int(str(number)[len(str(number)) - 1]) == 1:
        end_word = 'а '
    elif 2 <= int(str(number)[len(str(number)) - 1]) <= 4:
        end_word = 'и '
    elif int(str(number)[len(str(number)) - 1]) > 4:
        end_word = ' '
    return end_word

# Ввод числа от пользователя
number = int(input('Введите число (1-999 000 000 000): '))

# Получение словесного представления числа
words = number_to_words(number)

# Вывод словесного представления числа
print(words)