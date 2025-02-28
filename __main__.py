from KeyManager import KeyManager
from Grasshopper import Grasshopper
import Tools

welcome_message = 'Добро пожаловать в программу для работы с шифром Кузнечик!'
message_key = ['Пожалуйста, введите двоичный ключ длиной 256 символов, или 0, чтобы сгенерировать случайный: ',
           'Ваш ключ:', 'Пожалуйста, сохраните ключ и подождите, пока программа инициализируется.',
           'Введен некорректный ключ. Введите двоичный ключ длины 256 или 0 для генерации ключа.']

message_iv = ['Пожалуйста, введите двоичную синхропосылку длиной 256 символов, или 0, чтобы сгенерировать случайную: ',
           'Ваша синхропосылка:', 'Пожалуйста, сохраните её.',
           'Введена некорректная синхропосылка. Введите двоичную синхропосылку длиной 256 символов или 0 для генерации новой.']

operations = ('Выберите операцию:\n'
              '0: Смена ключа\n'
              '1: Смена синхропосылки\n'
              '2: Зашифрование сообщения\n'
              '3: Расшифрование сообщения\n'
              '4: Расшифрование последнего сообщения\n'
              '5: Выход\n')

def input_something(messages):
    while True:
        key = input(messages[0])
        if key == '0':
            key = Tools.generate_key()
            print(f'{messages[1]} {key}\n'
                  f'{messages[2]}')
            return key
        elif len(key) == 256 and Tools.is_binary_string(key):
            return key
        else:
            print(messages[3])

if __name__ == '__main__':
    print(welcome_message)
    key = input_something(message_key)
    grasshopper = Grasshopper(key)
    iv = input_something(message_iv)

    last_encrypted_message = ''

    op = input(operations)
    while op != '5':
        if op == '0':
            key = input_something(message_key)
            grasshopper = Grasshopper(key)
        elif op == '1':
            iv = input_something(message_iv)
        elif op == '2':
            message = input('Введите сообщение: ')
            last_encrypted_message = grasshopper.EncryptText(message, iv)
            print(last_encrypted_message)
        elif op == '3':
            message = input('Введите шифротекст: ')
            print(grasshopper.DecryptText(message, iv))
        elif op == '4':
            print(grasshopper.DecryptText(last_encrypted_message, iv))
        else:
            print('Выбрана неизвестная операция.')

        op = input(operations)
