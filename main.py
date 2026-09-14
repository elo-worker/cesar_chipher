import string

#алфавиты
alphabet_en_lowercase = string.ascii_lowercase
alphabet_en_uppercase = string.ascii_uppercase
alphabet_rus_lowercase = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet_rus_uppercase = alphabet_rus_lowercase.upper()

text = input("Введите текст:")
task = input('Вы хотите зашифровать или расшифровать сообщение?(з/р)')
language = input("Какой алфавит импользуем?(rus/en)")
step_chifr = int(input("Введите шаг сдвига:"))


if language == 'rus':
     alphabet = alphabet_rus_lowercase
else:
    alphabet = alphabet_en_lowercase

if language == 'rus':
    alphabet_uppercase = alphabet_rus_uppercase
else:
    alphabet_uppercase = alphabet_en_uppercase

def chipher_cesar(text, step_chipher):
    shifr_text = ''
    words = text.split()
    
    
    for word in words:

        # Считаем только буквы в слове для точного сдвига
        # Например, для "Gdb," letters_count будет равно 3 (без запятой)
        letters_count = step_chipher
        
        # Если в «слове» вообще нет букв (например, просто одиночный знак «-»), 
        # сдвиг будет 0, чтобы не делить на ноль и не ломать логику
        if letters_count == 0:
            letters_count = 1 

        shifr_word = ''

        for j in range(len(word)):   
            if word[j].lower() in alphabet:             
                if word[j].islower():
                    shifr_word += alphabet[((alphabet.index(word[j]) + letters_count) % len(alphabet))]
                elif word[j].isupper():
                    shifr_word += alphabet_uppercase[((alphabet_uppercase.index(word[j]) + letters_count) % len(alphabet))]
            else:
                shifr_word += word[j] 

        shifr_text += shifr_word + ' '

    return shifr_text.strip()



if 'з' in task:
    print(chipher_cesar(text, step_chifr))
elif 'р' in task:
    print(chipher_cesar(text, -step_chifr))
