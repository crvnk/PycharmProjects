#Перше завдання
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

n = int(input("Введіть число: "))

result = [x for x in numbers if x < n]

print(result)

#Друге завдання
tuple_of_strings = ('apple', 'banana', 'orange')
joined_string = ', '.join(tuple_of_strings)
print(joined_string)

#Третє завдання
books = {
    "Захар Беркут": {"автор": "Іван Франко", "рік": 1890, "сторінок": 432},
    "Тигролови": {"автор": "Іван Багряний", "рік": 1930, "сторінок": 372},
    "Кобзар": {"автор": "Тарас Шевченко", "рік": 1840, "сторінок": 300},
    "Хрестоматія з української літератури": {"автор": "Василь Симоненко", "рік": 1975, "сторінок": 548},
    "Майстер і Маргарита": {"автор": "Михайло Булгаков", "рік": 1967, "сторінок": 480},
    "Поема про море": {"автор": "Микола Вінграновський", "рік": 1975, "сторінок": 112},
    "Тарас Бульба": {"автор": "Микола Гоголь", "рік": 1835, "сторінок": 256},
    "Лісова пісня": {"автор": "Леся Українка", "рік": 1911, "сторінок": 180}
}

book_name = input("Введіть назву книги: ")
if book_name in books:
    book_info = books[book_name]
    print(f"Інформація про книгу {book_name}:")
    print(f"Автор: {book_info['автор']}")
    print(f"Рік видання: {book_info['рік']}")
    print(f"Кількість сторінок: {book_info['сторінок']}")
else:
    print(f"Книга з назвою '{book_name}' не знайдена у бібліотеці")

#Четверте завдання
students = {
    'Петренко': ('Оксана', 20, 'Жінка'),
    'Іваненко': ('Михайло', 21, 'Чоловік'),
    'Коваленко': ('Наталія', 19, 'Жінка'),
    'Сидоренко': ('Ігор', 22, 'Чоловік'),
    'Бойко': ('Тетяна', 20, 'Жінка')
}

student_surname = input("Введіть прізвище студента: ")

if student_surname in students:
    student_info = students[student_surname]
    print(f"Ім'я: {student_info[0]}\nВік: {student_info[1]}\nСтать: {student_info[2]}")
else:
    print("Студента з таким прізвищем не знайдено")

#П'яте завдання
phone_book = {
    'Іван': ['+380987654321', '+380986543210'],
    'Марія': ['+380951234567'],
    'Петро': ['+380937654321', '+380931234567', '+380932345678']
}

def add_phone_number(name, phone_number):
    if name in phone_book:
        phone_book[name].append(phone_number)
    else:
        phone_book[name] = [phone_number]

add_phone_number('Іван', '+380993456789')
add_phone_number('Марія', '+380987654321')

for name, phone_numbers in phone_book.items():
    print(f"{name}: {', '.join(phone_numbers)}")