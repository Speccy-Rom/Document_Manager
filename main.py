# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

def add_documents(document, directorie):
    number_document = input('Введите номер документа: ')
    type_document = input('Введите тип документа: ')
    name_owner = input('Введите имя владельца: ')
    number_shelf = input('Введите номер полки: ')
    if int(number_shelf) <= len(directorie):
        document.append({'type': type_document, 'number': number_document, 'name': name_owner})
        directorie[number_shelf].append(number_document)
        print('Ваши документы добавлены!')
    else:
        print('Такой полки не существует! Попробуйте ещё раз!')

def shelf_by_number(document):
    number1 = input('Введите номер документа: ')
    for key, value in document.items():
        if number1 in value:
            return key

def list_documents(document):
    for list_document in document:
        print(f'{list_document["type"]} "{list_document["number"]}" "{list_document["name"]}"')

def name_by_number(document):
    number = input('Введите номер документа: ')
    for names in document:
        if number == names['number']:
            return names['name']

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            document_owner = name_by_number(documents)
            if document_owner is None:
                print('Документа с таким номером нет в списке!\n'
                      'Если вы хотите добавить документ введите команду "a"')
            else:
                print('Данный документ принадлежит:', document_owner)
        elif user_input == 'l':
            list_documents(documents)
        elif user_input == 's':
            shelf_number = shelf_by_number(directories)
            if shelf_number is None:
                print('Документа с таким номером нет в списке!\n'
                      'Если вы хотите добавить документ введите команду "a"')
            else:
                print('Данный документ находится на полке №', shelf_number)
        elif user_input == 'a':
            add_documents(documents, directories)
        elif user_input == 'help':
            print('Список команд:\np - поиск человека по номеру документа\n'
                  'l - вывести список всех документов\n'
                  's - узнать номер полки на которой находится документ\n'
                  'a - добавить новый документ в каталог и в перечень полок'
                  '(необходимо указать номер документа, тип, имя владельца и номер полки)\n'
                  'q - выход из программы')
        elif user_input == 'q':
            break
        else:
            print('Такой команды не существует\nПосмотреть полный список команд вы можете набрав слово "help"\n'
                  'Для выхода из программы нажмите "q"')

main()
#---------------------------------- По исключениям:

# С помощью исключения KeyError проверяется, есть ли поле "name" и документа. 
def name(list):
  try:
    for i in range(len(documents)):
      if (documents[i]["number"] != '' ) & (documents[i]["name"] != ''):
        print (documents[i]["name"], documents[i]["number"])
  except KeyError:
    print ('got KeyError')