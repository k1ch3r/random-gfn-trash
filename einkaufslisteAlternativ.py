OPERATION_LIST = ['Liste anschauen', 'Etwas auf die Liste schreiben', 'Etwas von der Liste entfernen', 'Programm abballern alla!']
OPERATION_SHOW_LIST = 0
OPERATION_ADD_ITEM = 1
OPERATION_REMOVE_ITEM = 2
OPERATION_EXIT = 3

def stringify_array(array):
    return '\n'.join([f'[{index}]: {item}' for index, item in enumerate(array)])

def add_item(item):
    try:
        shopping_list.append(item)
    except:
        print('Fehler beim Hinzufügen des Artikels.')

def remove_item(index):
    try:
        shopping_list.pop(index)
    except:
        print('Fehler beim Entfernen des Artikels.')

operations_string = stringify_array(OPERATION_LIST)
menu_string = f'Willst du:\n{operations_string}\nGib jetzt die entsprechende Zahl ein: '

shopping_list = ['nichts', 'leer']
print('Hallo. Weil eine Einkaufsliste als Python Terminal App super spannend und sinnvoll ist kannst du hier Sachen in eine Liste packen und dir die anschauen.\n')
print('Hier ist deine aktuelle Liste:')
print(stringify_array(shopping_list))

def choose_operation():
    try:
        return int(input(menu_string))
    except ValueError:
        print('Ungültige Eingabe. Bitte gib eine gültige Zahl ein.')
        return -1

def menu_loop():
    while True:
        try:
            operation = choose_operation()

            if operation == OPERATION_SHOW_LIST:
                print('Hier ist deine aktuelle Liste:')
                print(stringify_array(shopping_list))
            elif operation == OPERATION_ADD_ITEM:
                item_to_add = input('Gib den Artikel zum aufschreiben ein: ')
                add_item(item_to_add)
                print('Okay, ', item_to_add, ' wurde aufgeschrieben.')
            elif operation == OPERATION_REMOVE_ITEM:
                item_to_remove_index = int(input('Gib die Nummer des Artikels ein, den du entfernen willst: '))
                if 0 <= item_to_remove_index < len(shopping_list):
                    item_to_remove_name = shopping_list[item_to_remove_index]
                    remove_item(item_to_remove_index)
                    print('Okay, ', item_to_remove_name, ' wurde entfernt.')
                else:
                    print('Ungültige Nummer. Bitte gib eine existierende Nummer ein.')
            elif operation == OPERATION_EXIT:
                print('Schade brudi, werde dich vermissen. HDGDL, baaaaaii')
                break
        except KeyboardInterrupt:
            print('\nCtrl + C pressed. Aborting.')
            break
        except:
            print('AU WEIA! Irgendwas lief schief.')
            break

menu_loop()
